from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class HomePageTest(TestCase):

    def test_home_page_redirects_for_anonymous(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'support/index.html')

    def test_home_page_for_authenticated_user(self):
        user = User.objects.create_user(username='user', password='userpass', email='user@example.com')
        self.client.login(username='user', password='userpass')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'support/ticket_list.html')
