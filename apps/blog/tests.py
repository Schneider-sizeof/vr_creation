"""
Tests for Blog AI post generator, model, and admin views.
"""
import json
from unittest.mock import patch, MagicMock
import requests
from django.test import TestCase, Client, override_settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from apps.blog.models import Article, Category
from apps.blog.services import (
    generate_blog_post_with_gemini,
    _clean_json_text,
    GeminiError,
    GeminiAPIKeyMissingError,
    GeminiTimeoutError,
    GeminiRateLimitError,
    GeminiResponseError,
    GeminiAPIError,
)

User = get_user_model()


class AIJsonCleanTestCase(TestCase):
    def test_clean_json_text_with_fences(self):
        raw = "```json\n{\"title\": \"Mon Titre\", \"excerpt\": \"Mon extrait\", \"content\": \"Mon contenu\"}\n```"
        cleaned = _clean_json_text(raw)
        data = json.loads(cleaned)
        self.assertEqual(data["title"], "Mon Titre")

    def test_clean_json_text_plain(self):
        raw = "{\"title\": \"Titre 2\", \"excerpt\": \"Extrait\", \"content\": \"Contenu\"}"
        cleaned = _clean_json_text(raw)
        data = json.loads(cleaned)
        self.assertEqual(data["title"], "Titre 2")


class AIServiceTestCase(TestCase):
    @override_settings(GEMINI_API_KEY="")
    def test_missing_api_key_raises_error(self):
        with self.assertRaises(GeminiAPIKeyMissingError):
            generate_blog_post_with_gemini(topic="Test 3D")

    @override_settings(GEMINI_API_KEY="fake-test-key")
    @patch("apps.blog.services.requests.post")
    def test_timeout_raises_timeout_error(self, mock_post):
        mock_post.side_effect = requests.exceptions.Timeout("Timed out")
        with self.assertRaises(GeminiTimeoutError):
            generate_blog_post_with_gemini(topic="Test 3D")

    @override_settings(GEMINI_API_KEY="fake-test-key")
    @patch("apps.blog.services.requests.post")
    def test_rate_limit_raises_rate_limit_error(self, mock_post):
        mock_resp = MagicMock()
        mock_resp.status_code = 429
        mock_post.return_value = mock_resp
        with self.assertRaises(GeminiRateLimitError):
            generate_blog_post_with_gemini(topic="Test 3D")

    @override_settings(GEMINI_API_KEY="fake-test-key")
    @patch("apps.blog.services.requests.post")
    def test_successful_generation(self, mock_post):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {
                                "text": "```json\n{\"title\": \"L'Avenir de la 3D\", \"excerpt\": \"Découvrez la 3D pour l'immobilier.\", \"content\": \"## Introduction\\n\\nLa 3D transforme l'architecture...\"}\n```"
                            }
                        ]
                    }
                }
            ]
        }
        mock_post.return_value = mock_resp

        result = generate_blog_post_with_gemini(topic="L'Avenir de la 3D", tone="professionnel")
        self.assertEqual(result["title"], "L'Avenir de la 3D")
        self.assertEqual(result["excerpt"], "Découvrez la 3D pour l'immobilier.")
        self.assertIn("La 3D transforme", result["content"])


class ArticleModelTestCase(TestCase):
    def test_article_status_sync(self):
        article = Article.objects.create(
            title="Article Test",
            slug="article-test",
            excerpt="Extrait",
            content="Contenu test " * 100,
            published_date="2026-09-05 20:00:00",
            status="draft",
        )
        self.assertFalse(article.is_published)
        self.assertFalse(article.ai_generated)

        # Update to published
        article.status = "published"
        article.save()
        self.assertTrue(article.is_published)


class AdminAIGenerateViewTestCase(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username="admin_test",
            email="admin@example.com",
            password="adminpassword123"
        )
        self.client = Client()
        self.client.login(username="admin_test", password="adminpassword123")

    def test_admin_generate_ai_view_get(self):
        url = reverse("admin:blog_article_generate_ai")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Générateur d'articles")

    @override_settings(GEMINI_API_KEY="fake-test-key")
    @patch("apps.blog.admin.generate_blog_post_with_gemini")
    def test_admin_generate_ai_view_post_success(self, mock_gen):
        mock_gen.return_value = {
            "title": "Article Généré par IA",
            "excerpt": "Court résumé de test",
            "content": "## Titre Section\n\nCorps de l'article avec 500 mots..."
        }

        url = reverse("admin:blog_article_generate_ai")
        post_data = {
            "topic": "Modélisation 3D pour l'immobilier",
            "tone": "professionnel",
            "length": "moyen",
            "language": "fr",
            "author": "VR Creation AI",
        }

        response = self.client.post(url, post_data, follow=True)
        self.assertEqual(response.status_code, 200)

        # Check article was created as draft with ai_generated=True
        article = Article.objects.get(title="Article Généré par IA")
        self.assertEqual(article.status, "draft")
        self.assertFalse(article.is_published)
        self.assertTrue(article.ai_generated)
        self.assertEqual(article.author, "VR Creation AI")
