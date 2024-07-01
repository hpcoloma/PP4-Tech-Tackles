from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('submit_ticket/', views.submit_ticket, name='submit_ticket'),
    path('view_my_tickets/', views.view_my_tickets, name='view_my_tickets'),
    path('edit_ticket/<int:ticket_id>/', views.edit_ticket, name='edit_ticket'),
    path('delete_ticket/<int:ticket_id>/', views.delete_ticket, name='delete_ticket'),
    path('add_comment/<int:ticket_id>/', views.add_comment, name='add_comment'),
    path('view_all_tickets/<int:ticket_id>/', views.view_all_tickets, name='view_all_tickets'),
    path('update_ticket_status/<int:ticket_id>/', views.update_ticket_status, name='update_ticket_status'),
]