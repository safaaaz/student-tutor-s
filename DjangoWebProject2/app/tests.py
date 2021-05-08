"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase
from django.urls import reverse

# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_home(self):
        """Tests the home page."""
        response = self.client.get(reverse("home"))
        self.assertContains(response.status_code, 200)

    def test_contact(self):
        """Tests the contact page."""
        response = self.client.get('/contact/')
        self.assertContains(response, 'Contact', 3, 200)

    def test_about(self):
        """Tests the about page."""
        response = self.client.get('/about/')
        self.assertContains(response, 'About', 3, 200)


    def test_login(self):
        """Tests the contact page."""
        response = self.client.get(reverse('login'))
        self.assertContains(response.status_code, 200)

    def test_show(self):
        response = self.client.get(reverse("show"))
        self.assertEquals(response.status_code, 200)

    def test_studentsignup(self):
        """Tests the about page."""
        response = self.client.get(reverse('studentsignup'))
        self.assertEquals(response.status_code, 200)

    def test_checkout(self):
        response = self.client.get(reverse("CheckOut"))
        self.assertEquals(response.status_code, 200)

    def test_tutorstud(self):
        response = self.client.get(reverse("tutorstud"))
        self.assertEquals(response.status_code, 200)

    def test_ourcart(self):
        response = self.client.get(reverse("ourcart"))
        self.assertEquals(response.status_code, 200)

    def test_addchart(self):
        response = self.client.get(reverse("addchart"))
        self.assertEquals(response.status_code, 200)

    def test_back(self):
        response = self.client.get(reverse("back"))
        self.assertEquals(response.status_code, 200)