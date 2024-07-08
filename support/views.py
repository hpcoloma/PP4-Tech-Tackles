from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Ticket
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
def home_page(request):
    if request.user.is_authenticated:
        return redirect('ticket_list')
    return render(request, 'support/index.html')

class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'support/ticket_list.html'

    def get_queryset(self):
        if self.request.user == 'tech_support':
            return Ticket.objects.all()
        else:
            return Ticket.objects.filter(user=self.request.user)
    



