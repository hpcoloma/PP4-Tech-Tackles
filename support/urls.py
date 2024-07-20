from . import views
from django.urls import path
from .views import (
    home_page, 
    TicketListView, 
    TicketDetailView, 
    TicketCreateView, 
    add_comment, 
    TicketUpdateView, 
    TicketDeleteView, 
    edit_comment, 
    delete_comment, 
    NoAccessView
)

urlpatterns = [
    path('', home_page, name='home'),
    path('tickets/', TicketListView.as_view(), name='ticket_list'),
    path('ticket/<int:pk>/', TicketDetailView.as_view(), name='ticket_detail'),
    path('no_access/', NoAccessView.as_view(), name='no_access'),
    path('ticket/<int:pk>/comment/', add_comment, name='add_comment'),
    path('edit_comment/', edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('ticket/new/', TicketCreateView.as_view(), name='ticket_create'),
    path('ticket/<int:pk>/edit/', TicketUpdateView.as_view(), name='ticket_edit'),
    path('ticket/<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket_delete'),
]


