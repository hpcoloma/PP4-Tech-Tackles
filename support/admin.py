from django.contrib import admin
from .models import Ticket, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Ticket)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('subject', 'ticket_id', 'user', 'status', 'created_on')
    search_fields = ['subject', 'description']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'ticket_id': ('subject',)}
    summernote_fields = ('description',)

# Register your models here.
admin.site.register(Comment)