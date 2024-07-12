from django import forms
from .models import Comment, Ticket

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['subject','description']
    
    def clean(self):
        cleaned_data = super().clean()
    