from django.test import TestCase
from django.urls import reverse


class Custom404ViewTest(TestCase):

    def test_custom_404_view(self):
        response = self.client.get('/nonexistent-page/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'support/404.html')