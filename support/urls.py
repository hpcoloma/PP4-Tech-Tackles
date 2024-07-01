from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('submit_ticket/', views.submit_ticket, name='submit_ticket'),
    path('view_my_tickets/', views.view_my_tickets, name='view_my_tickets'),
]