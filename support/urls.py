from . import views
from django.urls import path
from support.views import home_page, TicketListView, TicketDetailView, add_comment

urlpatterns = [
    path('', views.home_page, name='home'),
    path('tickets/', TicketListView.as_view(), name='ticket_list'),
    path('ticket/<int:pk>/', TicketDetailView.as_view(), name='ticket_detail'),
    path('ticket/<int:pk>/comment/', add_comment, name='add_comment'),
]


