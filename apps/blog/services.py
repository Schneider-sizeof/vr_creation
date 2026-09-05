"""
AI Service for Blog Post Generation using Google Gemini 2.0 Flash REST API.
"""
import json
import logging
import re
import requests
from django.conf import settings

logger = logging.getLogger(__name__)


class GeminiError(Exception):
    """Base exception for Gemini AI service errors."""
    pass


class GeminiAPIKeyMissingError(GeminiError):
    """Raised when the Gemini API key is not configured."""
    pass


class GeminiTimeoutError(GeminiError):
    """Raised when the API request times out."""
    pass


class GeminiRateLimitError(GeminiError):
    """Raised when the API rate limit is exceeded (HTTP 429)."""
    pass


class GeminiResponseError(GeminiError):
    """Raised when Gemini returns an invalid or unparseable response."""
    pass


class GeminiAPIError(GeminiError):
    """Raised when the API returns an HTTP error code."""
    pass


def _clean_json_text(raw_text: str) -> str:
    """
    Remove markdown code fences and trim whitespace to obtain raw JSON.
    """
    cleaned = raw_text.strip()

    code_block_match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', cleaned, re.IGNORECASE)
    if code_block_match:
        cleaned = code_block_match.group(1).strip()
    elif cleaned.startswith('```') and cleaned.endswith('```'):
        cleaned = re.sub(r'^```(?:json)?\s*', '', cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r'\s*```$', '', cleaned)

    return cleaned.strip()


def generate_blog_post_with_gemini(
    topic: str,
    tone: str = 'professionnel',
    length: str = 'moyen',
    language: str = 'fr',
    category_name: str = None,
    target_audience: str = 'Entreprises, Promoteurs, Commerces et Professionnels',
) -> dict:
    """
    Calls Google Gemini 2.0 Flash REST API to generate a structured blog article.

    Returns a dict with:
        - title: str
        - excerpt: str (summary ~150-300 chars, max 500)
        - content: str (markdown formatted article, 500-800 words)

    Raises:
        GeminiAPIKeyMissingError: If GEMINI_API_KEY is not configured
        GeminiTimeoutError: If the request times out
        GeminiRateLimitError: If rate limit is hit (429)
        GeminiAPIError: If API returns an error status
        GeminiResponseError: If the returned JSON cannot be parsed or lacks required fields
    """
    api_key = getattr(settings, 'GEMINI_API_KEY', '') or ''
    if not api_key:
        raise GeminiAPIKeyMissingError(
            "La clé API Google Gemini (GEMINI_API_KEY) n'est pas configurée. "
            "Veuillez définir GEMINI_API_KEY dans votre fichier .env ou vos variables d'environnement."
        )

    model = getattr(settings, 'GEMINI_MODEL', 'gemini-2.0-flash')
    timeout_seconds = getattr(settings, 'GEMINI_TIMEOUT_SECONDS', 25)
    endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"

    length_guidelines = {
        'court': 'environ 400 à 600 mots',
        'moyen': 'environ 600 à 800 mots',
        'long': 'environ 800 à 1200 mots',
    }
    word_count_text = length_guidelines.get(length, 'environ 500 à 800 mots')

    tone_descriptions = {
        'professionnel': 'professionnel, expert, crédible et axé sur les résultats',
        'engageant': 'dynamique, captivant, moderne et chaleureux',
        'informatif': 'pédagogique, clair, structuré avec des conseils concrets',
        'technique': 'approfondi, précis, mettant en avant les technologies 3D, VR et digitales',
        'persuasif': 'orienté conversion, mettant en avant les avantages concurrentiels et le ROI',
        'storytelling': 'narratif, inspirant, avec des exemples immersifs',
    }
    tone_text = tone_descriptions.get(tone, 'professionnel et engageant')

    lang_instructions = {
        'fr': "Rédige l'intégralité du contenu en Français de haute qualité.",
        'en': "Write the entire content in high-quality professional English.",
        'ar': "اكتب المحتوى بالكامل باللغة العربية الفصحى الاحترافية والواضحة.",
    }
    lang_instruction = lang_instructions.get(language, "Rédige l'intégralité du contenu en Français.")

    system_prompt = f"""Tu es un rédacteur web expert et stratège de contenu pour **VR CREATION** (Studio leader en production digitale, modélisation 3D, visites virtuelles 360°, branding visuel, création de sites web et solutions digitales innovantes).

DIRECTIVES DE RÉDACTION :
1. Sujet / Mots-clés : {topic}
2. Catégorie thématique : {category_name or 'Général'}
3. Ton de rédaction : {tone_text}
4. Longueur cible : {word_count_text}
5. Langue : {lang_instruction}
6. Public cible : {target_audience}

STRUCTURE DU CONTENU (Markdown) :
- Titre percutant et optimisé SEO (sans préfixe inutile).
- Extrait concis et accrocheur (2 à 3 phrases, max 400 caractères) résumant l'essentiel de l'article.
- Corps de l'article structuré en Markdown avec :
  • Introduction engageante posant la problématique ou la tendance
  • Titres de sections H2 (`## Titre`) et sous-titres H3 (`### Sous-titre`) clairs
  • Listes à puces ou à numéros pour faciliter la lecture
  • Conseils pratiques, chiffres ou exemples concrets
  • Conclusion inspirante avec un appel à l'action invitant à découvrir les solutions de VR CREATION (devis gratuit, contact).

RÈGLE ABSOLUE DE FORMAT :
Tu dois répondre UNIQUEMENT avec un objet JSON valide contenant exactement ces 3 clés :
{{
  "title": "Titre optimisé de l'article",
  "excerpt": "Court résumé accrocheur pour la liste des articles",
  "content": "Corps complet de l'article au format Markdown..."
}}
Ne fournis AUCUN texte d'introduction ni de conclusion avant ou après le JSON.
"""

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": system_prompt}
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 3500,
            "responseMimeType": "application/json"
        }
    }

    logger.info("Gemini AI blog generation initiated for topic: '%s' (tone=%s, length=%s, lang=%s)", topic, tone, length, language)

    try:
        response = requests.post(
            endpoint,
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=timeout_seconds,
        )
    except requests.exceptions.Timeout as exc:
        logger.error("Gemini API request timed out after %ds for topic '%s'", timeout_seconds, topic)
        raise GeminiTimeoutError(
            f"La génération par l'IA a expiré après {timeout_seconds} secondes. "
            "Le service Google Gemini est peut-être temporairement lent. Veuillez réessayer."
        ) from exc
    except requests.exceptions.RequestException as exc:
        logger.error("Gemini API connection error: %s", exc)
        raise GeminiAPIError(
            f"Erreur de connexion avec l'API Google Gemini : {str(exc)}"
        ) from exc

    if response.status_code == 429:
        logger.warning("Gemini API rate limit reached (HTTP 429)")
        raise GeminiRateLimitError(
            "Limite de requêtes atteinte sur l'API Google Gemini (Erreur 429). "
            "Veuillez patienter quelques instants avant de relancer une nouvelle génération."
        )
    elif response.status_code != 200:
        error_detail = ""
        try:
            err_json = response.json()
            error_detail = err_json.get('error', {}).get('message', response.text)
        except Exception:
            error_detail = response.text[:200]
        logger.error("Gemini API returned error %d: %s", response.status_code, error_detail)
        raise GeminiAPIError(
            f"L'API Google Gemini a renvoyé une erreur ({response.status_code}) : {error_detail}"
        )

    try:
        resp_data = response.json()
        candidates = resp_data.get('candidates', [])
        if not candidates:
            raise GeminiResponseError("L'API Gemini n'a retourné aucun contenu.")

        first_candidate = candidates[0]
        content_obj = first_candidate.get('content', {})
        parts = content_obj.get('parts', [])
        if not parts:
            raise GeminiResponseError("Le format de réponse de Gemini est vide ou incomplet.")

        raw_text = parts[0].get('text', '')
        cleaned_json_str = _clean_json_text(raw_text)

        parsed_json = json.loads(cleaned_json_str)

        title = parsed_json.get('title', '').strip()
        excerpt = parsed_json.get('excerpt', '').strip()
        content = parsed_json.get('content', '').strip()

        if not title or not content:
            raise GeminiResponseError("La réponse générée ne contient pas de titre ou de contenu valide.")

        if not excerpt:
            clean_lines = [l.strip() for l in content.split('\n') if l.strip() and not l.startswith('#')]
            excerpt = (clean_lines[0] if clean_lines else title)[:400]
        elif len(excerpt) > 500:
            excerpt = excerpt[:497] + '...'

        logger.info("Gemini AI successfully generated article: '%s' (%d words)", title, len(content.split()))

        return {
            'title': title,
            'excerpt': excerpt,
            'content': content,
        }

    except json.JSONDecodeError as exc:
        logger.error("Failed to parse Gemini response as JSON. Raw text: %s", raw_text if 'raw_text' in locals() else '')
        raise GeminiResponseError(
            f"Impossible de décoder la réponse JSON de Gemini. Détail : {str(exc)}"
        ) from exc
    except GeminiResponseError:
        raise
    except Exception as exc:
        logger.error("Unexpected error parsing Gemini response: %s", exc)
        raise GeminiResponseError(f"Erreur inattendue lors du traitement de la réponse IA : {str(exc)}") from exc
