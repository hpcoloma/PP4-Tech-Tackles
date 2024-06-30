from django.contrib import admin
from .models import Profile, Ticket, KnowledgeBase, Comment
# from django_summernote.admin import SummernoteModelAdmin


# class PostAdmin(SummernoteModelAdmin):
#     list_display = ('subject', 'ticket_id', 'status')
#     search_fields = ('ticket_id')
#     list_filter = ('status')
#     summernote_fields = ('content')

# Register your models here.
admin.site.register(Profile)
admin.site.register(Ticket)
admin.site.register(KnowledgeBase)
admin.site.register(Comment)
