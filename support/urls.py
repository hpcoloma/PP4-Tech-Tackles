from . import views
from django.urls import path
from support.views import home_page, TicketListView

urlpatterns = [
    path('', views.home_page, name='home'),
    path('tickets/', TicketListView.as_view(), name='ticket_list'),
]


