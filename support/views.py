from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Ticket
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import CommentForm



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

    
    



