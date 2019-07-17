"""
Here are all the tests for the django-perfect404 application.

"""

from django.test import TestCase


class DemoTest(TestCase):
    """Just a sanity check that the single page of the demo website loads correctly."""

    def test_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class NotFoundTest(TestCase):

    def test_get(self):
        response = self.client.get('/bad-page/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'perfect404.html')
