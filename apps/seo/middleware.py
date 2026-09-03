"""
Canonical domain redirect middleware.
301-redirects non-canonical requests to the canonical domain.
Controlled by settings:
    CANONICAL_DOMAIN = 'vrcreation.com'
    CANONICAL_DOMAIN_REDIRECT_ENABLED = False  # Enable after domain migration
"""
from django.conf import settings
from django.http import HttpResponsePermanentRedirect


class CanonicalDomainMiddleware:
    """
    Middleware that enforces canonical domain:
    - Redirects www to non-www
    - Redirects http to https
    - Redirects old PythonAnywhere subdomain to new domain
    
    Only active when CANONICAL_DOMAIN_REDIRECT_ENABLED = True in settings.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not getattr(settings, 'CANONICAL_DOMAIN_REDIRECT_ENABLED', False):
            return self.get_response(request)

        canonical_domain = getattr(settings, 'CANONICAL_DOMAIN', 'vrcreation.com')
        canonical_protocol = getattr(settings, 'SITE_PROTOCOL', 'https')
        host = request.get_host().split(':')[0].lower()

        needs_redirect = False

        # Check if host is not the canonical domain
        if host != canonical_domain:
            needs_redirect = True

        # Check protocol (via X-Forwarded-Proto header)
        protocol = request.META.get('HTTP_X_FORWARDED_PROTO', 'http')
        if protocol != canonical_protocol:
            needs_redirect = True

        if needs_redirect:
            new_url = f"{canonical_protocol}://{canonical_domain}{request.get_full_path()}"
            return HttpResponsePermanentRedirect(new_url)

        return self.get_response(request)
