from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Ticket, KnowledgeBase, Comment
from django.contrib.auth.models import User



# Create your views here.
def register(request):
    if requested.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'support/register.html', {'form': form})

@login_required
def submit_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid()
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('view_my_tickets')
    else:
        form = TicketForm()
    return render(request, 'support/submit_ticket.html', {'form': form})

@login_required
def view_my_tickets(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'support/view_my_tickets.html', {'tickets': tickets})
