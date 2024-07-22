from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Ticket, Comment
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()


class TicketViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='user',
            password='userpass',
            email='user@example.com'
        )
        self.staff_user = User.objects.create_user(
            username='staff',
            password='staffpass',
            email='staff@example.com',
            is_staff=True
        )
        self.superuser = User.objects.create_superuser(
            username='admin',
            password='adminpass'
        )
        self.ticket = Ticket.objects.create(
            subject='Test Ticket',
            description='Test description',
            user=self.user
        )

    def test_home_page_redirects_for_anonymous(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'support/index.html')

    def test_home_page_for_authenticated_user(self):
        self.client.login(username='user', password='userpass')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'support/ticket_list.html')

    def test_ticket_list_view_for_authenticated_user(self):
        self.client.login(username='user', password='userpass')
        response = self.client.get(reverse('ticket_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'support/ticket_list.html')
        self.assertContains(response, 'Test Ticket')

    def test_ticket_detail_view_for_staff(self):
        self.client.login(username='staff', password='staffpass')
        response = self.client.get(
            reverse('ticket_detail', kwargs={'pk': self.ticket.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'support/ticket_detail.html')

    def test_ticket_detail_view_for_owner(self):
        self.client.login(username='user', password='userpass')
        response = self.client.get(
            reverse('ticket_detail', kwargs={'pk': self.ticket.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'support/ticket_detail.html')

    def test_ticket_detail_view_for_non_owner(self):
        other_user = User.objects.create_user(
            username='other_user',
            password='otherpass'
        )
        self.client.login(username='other_user', password='otherpass')
        response = self.client.get(
            reverse('ticket_detail', kwargs={'pk': self.ticket.pk})
        )
        self.assertRedirects(response, reverse('no_access'))

    def test_ticket_create_view(self):
        self.client.login(username='user', password='userpass')
        response = self.client.post(
            reverse('ticket_create'),
            {'subject': 'New Ticket', 'description': 'New description'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Ticket.objects.filter(subject='New Ticket').exists())

    def test_ticket_update_view(self):
        self.client.login(username='user', password='userpass')
        response = self.client.post(
            reverse('ticket_edit', kwargs={'pk': self.ticket.pk}),
            {'subject': 'Updated Ticket', 'description': 'Updated description'}
        )
        self.assertEqual(response.status_code, 302)
        self.ticket.refresh_from_db()
        self.assertEqual(self.ticket.subject, 'Updated Ticket')

    def test_ticket_delete_view(self):
        self.client.login(username='user', password='userpass')
        response = self.client.post(
            reverse('ticket_delete', kwargs={'pk': self.ticket.pk})
        )
        self.assertEqual(response.status_code, 302)  # Redirect to ticketlist
        self.assertFalse(Ticket.objects.filter(pk=self.ticket.pk).exists())

    def test_add_comment_view(self):
        self.client.login(username='user', password='userpass')
        response = self.client.post(
            reverse('add_comment', kwargs={'pk': self.ticket.pk}),
            {'comment': 'New comment'}
        )
        self.assertEqual(response.status_code, 302)  # Redirect to ticketdetail
        self.assertTrue(Comment.objects.filter(comment='New comment').exists())

    def test_edit_comment_view(self):
        self.client.login(username='user', password='userpass')
        comment = Comment.objects.create(
            ticket=self.ticket, user=self.user, comment='Old comment'
        )
        response = self.client.post(
            reverse('edit_comment'),
            {'comment_id': comment.id, 'comment': 'Updated comment'}
        )
        self.assertEqual(response.status_code, 302)  # Redirect to ticketdetail
        comment.refresh_from_db()
        self.assertEqual(comment.comment, 'Updated comment')

    def test_delete_comment_view(self):
        self.client.login(username='user', password='userpass')
        comment = Comment.objects.create(
            ticket=self.ticket,
            user=self.user,
            comment='Comment to delete'
        )
        response = self.client.post(
            reverse('delete_comment', kwargs={'comment_id': comment.id})
        )
        self.assertEqual(response.status_code, 302)  # Redirect to ticketdetail
        self.assertFalse(Comment.objects.filter(id=comment.id).exists())

    def test_no_access_view(self):
        response = self.client.get(reverse('no_access'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'support/no_access.html')


class CustomLoginViewTest(TestCase):

    def setUp(self):
        # Create a test user
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )
        self.login_url = reverse('custom_login')

    def test_login_page_renders_correctly(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')
        self.assertIsInstance(response.context['form'], AuthenticationForm)

    def test_successful_login_redirects(self):
        response = self.client.post(
            self.login_url, {
                'username': self.username,
                'password': self.password
            }
        )
        self.assertRedirects(response, reverse('ticket_list'))

    def test_invalid_login_shows_error(self):
        response = self.client.post(
            self.login_url, {
                'username': self.username,
                'password': 'wrongpassword'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')
        self.assertContains(
            response, 'Please enter a correct username and password.'
        )

    def test_invalid_login_no_user(self):
        response = self.client.post(
            self.login_url, {'username': 'nouser', 'password': 'nopassword'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')
        self.assertContains(
            response, 'Please enter a correct username and password.'
        )
