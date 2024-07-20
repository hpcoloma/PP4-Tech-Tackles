from django.test import TestCase
from .forms import CommentForm, TicketForm

class CommentFormTest(TestCase):

    def test_valid_comment_form(self):
        form_data = {'comment': 'This is a comment'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_comment_form(self):
        form_data = {'comment': ''}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())

class TicketFormTest(TestCase):

    def test_valid_ticket_form(self):
        form_data = {'subject': 'Test Subject', 'description': 'Test description'}
        form = TicketForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_ticket_form(self):
        form_data = {'subject': '', 'description': 'Test description'}
        form = TicketForm(data=form_data)
        self.assertFalse(form.is_valid())