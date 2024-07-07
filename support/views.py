from django.shortcuts import render
from django.views import generic
from .models import Ticket


# Create your views here.
class TicketList(generic.ListView):
    # model = Ticket
    queryset = Ticket.objects.all()
    template_name = "support/index.html"
    paginated_by = 5
    



