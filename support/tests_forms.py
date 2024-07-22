from django.test import TestCase
from django.contrib.auth.models import User
from .forms import CommentForm, TicketForm, TicketUpdateForm, StatusFilterForm
from .models import Ticket, Comment


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
        form_data = {
            'subject': 'Test Subject',
            'description': 'Test description'
        }
        form = TicketForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_ticket_form(self):
        form_data = {
            'subject': '',
            'description': 'Test description'
        }
        form = TicketForm(data=form_data)
        self.assertFalse(form.is_valid())


class TicketUpdateFormTest(TestCase):

    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username='admin',
            password='adminpass',
            email='admin@example.com'
        )
        self.staff_user = User.objects.create_user(
            username='staff',
            password='staffpass',
            email='staff@example.com',
            is_staff=True
        )
        self.regular_user = User.objects.create_user(
            username='user',
            password='userpass',
            email='user@example.com'
        )
        self.ticket = Ticket.objects.create(
            subject='Test Subject',
            description='Test description',
            status='Open',
            user=self.regular_user
        )

    def test_admin_permissions(self):
        form_data = {
            'subject': 'Updated Subject',
            'description': 'Updated description',
            'status': 'Closed'
        }
        form = TicketUpdateForm(
            data=form_data, instance=self.ticket, user=self.admin_user
        )
        self.assertTrue(form.is_valid())
        self.assertFalse(form.fields['subject'].disabled)
        self.assertFalse(form.fields['description'].disabled)
        self.assertFalse(form.fields['status'].disabled)

    def test_staff_permissions(self):
        form_data = {
            'subject': 'Updated Subject',
            'description': 'Updated description',
            'status': 'Closed'
        }
        form = TicketUpdateForm(
            data=form_data, instance=self.ticket, user=self.staff_user
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.fields['subject'].disabled)
        self.assertTrue(form.fields['description'].disabled)
        self.assertFalse(form.fields['status'].disabled)

    def test_regular_user_permissions(self):
        form_data = {
            'subject': 'Updated Subject',
            'description': 'Updated description',
            'status': 'Closed'
        }
        form = TicketUpdateForm(
            data=form_data, instance=self.ticket, user=self.regular_user
        )
        self.assertTrue(form.is_valid())
        self.assertFalse(form.fields['subject'].disabled)
        self.assertFalse(form.fields['description'].disabled)
        self.assertTrue(form.fields['status'].disabled)


class StatusFilterFormTest(TestCase):

    def test_all_statuses(self):
        form_data = {'status': ''}
        form = StatusFilterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_open_status(self):
        form_data = {'status': 'Open'}
        form = StatusFilterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_status(self):
        form_data = {'status': 'InvalidStatus'}
        form = StatusFilterForm(data=form_data)
        self.assertFalse(form.is_valid())
