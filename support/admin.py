from django.contrib import admin
from .models import Ticket, Comment, Profile
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Ticket)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('subject', 'ticket_id', 'user', 'status', 'created_on')
    search_fields = ['subject', 'description']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'ticket_id': ('subject',)}
    summernote_fields = ('description',)

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('formatted_ticket_id', 'ticket_status', 'user', 'created_on')
    list_filter = ('created_on',)

    def formatted_ticket_id(self, obj):
        if obj.ticket:
            return obj.ticket.ticket_id  # Replace with your actual ticket ID attribute
        else:
            return '-'  # Handle case where no ticket is associated 

    def ticket_status(self, obj):
        return obj.ticket.status if obj.ticket else '-'  # Display status if ticket exists, else '-'

    formatted_ticket_id.admin_order_field = 'ticket__id'  # Allow sorting by ticket ID
    ticket_status.admin_order_field = 'ticket__status'  # Allow sorting by ticket status

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('ticket', 'user')
