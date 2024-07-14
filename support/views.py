from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ticket, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, TicketForm, TicketUpdateForm


# Create your views here.
def home_page(request):
    if request.user.is_authenticated:
        return redirect('ticket_list')
    return render(request, 'support/index.html')


class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'support/ticket_list.html'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Ticket.objects.all().order_by('ticket_id')
        else:
            return Ticket.objects.filter(user=self.request.user).order_by('ticket_id')


class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket
    template_name = 'support/ticket_detail.html'
    # comment_form = CommentForm()

  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ticket = self.get_object()
        context['comments'] = ticket.comments.all().order_by('-created_on')
        context['comment_form'] = CommentForm()
        return context

    

class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'support/ticket_form.html'
    success_url = reverse_lazy('ticket_list')

    def form_valid(self, form, *args, **kwargs):
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
def add_comment(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ticket = ticket
            comment.user = request.user
            comment.save()
            return redirect('ticket_detail', pk=ticket.pk)
    else:
        form = CommentForm()
    return render(request, 'support/add_comment.html', {'form': form})


class TicketUpdateView(LoginRequiredMixin, UpdateView):
    model = Ticket
    form_class = TicketUpdateForm
    template_name = 'support/ticket_form.html'
    success_url = reverse_lazy('ticket_list')
    success_message = "Ticket was updated successfully!"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return Ticket.objects.all()
        return Ticket.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user to the form
        return kwargs

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class TicketDeleteView(DeleteView):
    model = Ticket
    success_url = reverse_lazy('ticket_list')
    success_message = 'Ticket was deleted successfully!'

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)
        return qs

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
    
    



