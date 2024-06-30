from django.contrib import admin
from .models import Profile, Ticket, KnowledgeBase, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Ticket)
admin.site.register(KnowledgeBase)
admin.site.register(Comment)
