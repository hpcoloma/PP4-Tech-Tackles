from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Ticket, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, TicketForm, TicketUpdateForm, StatusFilterForm
from django.http import HttpResponseForbidden
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login



# Create your views here.
# @login_required
def home_page(request):
    form = StatusFilterForm(request.GET)
    tickets = Ticket.objects.all().order_by('-created_on')
    paginate_by = 10  # Show 10 tickets per page

    if request.user.is_authenticated:
        if request.user.is_staff:
            tickets = tickets.order_by('-created_on')
        else:
            tickets = tickets.filter(user=request.user).order_by('-created_on')

        # Apply filter
        if form.is_valid():
            status = form.cleaned_data.get('status')
            if status:
                tickets = tickets.filter(status=status)

        return render(request, 'support/ticket_list.html', {
            'object_list': tickets,
            'filter_form': form
        })
    return render(request, 'support/index.html')


def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse('ticket_list'))  # Redirect to ticket list after login
    else:
        form = AuthenticationForm()

    return render(request, 'account/login.html', {'form': form})


class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    context_object_name = 'tickets'
    paginate_by = 10  # Show 10 tickets per page

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status')

        if self.request.user.is_staff:
            queryset = Ticket.objects.all()
        else:
            queryset = Ticket.objects.filter(user=self.request.user)

        if status:
            queryset = queryset.filter(status=status)

        return queryset.order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = StatusFilterForm(self.request.GET)
        return context
        

class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket
    template_name = 'support/ticket_detail.html'
    context_object_name = 'ticket'

    def dispatch(self, request, *args, **kwargs):
        try:
            # Get the ticket object to check permissions
            obj = self.get_object()
        except Http404:
            # If ticket is not found
            return render(request, 'support/404.html', status=404)
        
        logged_user = self.request.user

        # Check if the logged-in user is not the ticket owner and is not staff
        if obj.user != logged_user and not (logged_user.is_staff or logged_user.groups.filter(name='tech_support').exists()):
            return redirect('no_access')  # Redirect to the no access page

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Adds comments and comment form to the context.
        """
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().order_by('-created_on')
        context['comment_form'] = CommentForm()
        return context


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'support/ticket_form.html'
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Ticket was created successfully!")
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('ticket_detail', kwargs={'pk': self.object.pk})


class TicketUpdateView(LoginRequiredMixin, UpdateView):
    model = Ticket
    form_class = TicketUpdateForm
    template_name = 'support/ticket_form.html'
    success_message = "Ticket was updated successfully!"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff or self.request.user.is_superuser:
            return Ticket.objects.all()
        return Ticket.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user to the form
        return kwargs

    def form_valid(self, form):
        messages.success(self.request, self.success_message)  # Set success message
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('ticket_detail', kwargs={'pk': self.object.pk})
    


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


@login_required
def edit_comment(request):
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        new_comment_text = request.POST.get('comment')
        comment = get_object_or_404(Comment, id=comment_id)

        if request.user == comment.user or request.user.is_staff:
            comment.comment = new_comment_text
            comment.save()
            messages.success(request, 'Comment was updated successfully!')  # Add success message
            return redirect('ticket_detail', pk=comment.ticket.id)
        else:
            return HttpResponseForbidden()
    return redirect('ticket_list')


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    ticket_id = comment.ticket.id
    if request.user == comment.user or request.user.is_staff:
        comment.delete()
        messages.success(request, 'Comment was deleted successfully!')  # Add success message
    return redirect(reverse('ticket_detail', kwargs={'pk': ticket_id}))


class NoAccessView(TemplateView):
    template_name = 'support/no_access.html'