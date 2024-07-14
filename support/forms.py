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


class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['subject', 'description', 'status']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Determine field permissions based on user role
        if self.user.is_staff:
            # Staff can change status only
            self.fields['subject'].disabled = True
            self.fields['description'].disabled = True
        else:
            # Regular users can edit subject and description only
            self.fields['status'].disabled = True


class StatusFilterForm(forms.Form):
    STATUS_OPTIONS = (
        ('', 'All'),
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    )
    status = forms.ChoiceField(choices=STATUS_OPTIONS, required=False, label='Filter by Status')
            