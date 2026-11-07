"""
Tests for Core app - Home page and Strategic Successes.
"""
from django.test import TestCase, Client
from django.urls import reverse
from apps.core.models import StrategicSuccess


class StrategicSuccessTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage_with_db_strategic_successes(self):
        # We seeded 4 strategic successes via migration 0016
        self.assertTrue(StrategicSuccess.objects.filter(is_active=True).exists())
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Exemples de succès stratégiques')
        self.assertContains(response, 'Projet immobilier')
        self.assertContains(response, 'Villa en construction')
        self.assertContains(response, 'Magasin ou concept-store')

    def test_homepage_fallback_when_empty_db(self):
        StrategicSuccess.objects.all().delete()
        self.assertEqual(StrategicSuccess.objects.count(), 0)

        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Exemples de succès stratégiques')
        # Even with empty DB, fallback strategic successes are displayed!
        self.assertContains(response, 'Projet immobilier')
        self.assertContains(response, 'Villa en construction')
        self.assertContains(response, 'Magasin ou concept-store')

    def test_multilingual_homepage_strategic_successes(self):
        # English
        resp_en = self.client.get('/en/')
        self.assertEqual(resp_en.status_code, 200)

        # Arabic
        resp_ar = self.client.get('/ar/')
        self.assertEqual(resp_ar.status_code, 200)
