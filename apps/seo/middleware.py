"""
Canonical domain redirect & host shield middleware.
- 301-redirects www.vrcreationcompany.com to https://vrcreationcompany.com
- 301-redirects http to https
- returns a plain 404 (not a redirect, not the site) for any other Host header
"""
from django.conf import settings
from django.http import HttpResponseNotFound, HttpResponsePermanentRedirect


class CanonicalDomainMiddleware:
    """
    Middleware that enforces canonical domain and shields against host leakage:
    - Rejects foreign host headers (e.g. medicentersperformance.com, raw IP) with a plain 404
    - 301 redirects www.vrcreationcompany.com to https://vrcreationcompany.com
    - 301 redirects http to https
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        canonical_domain = getattr(settings, 'CANONICAL_DOMAIN', 'vrcreationcompany.com')
        canonical_protocol = getattr(settings, 'SITE_PROTOCOL', 'https')

        # Read host directly from META to intercept before DisallowedHost validation
        raw_host = (request.META.get('HTTP_HOST') or '').split(':')[0].strip().lower()

        # In dev mode (DEBUG=True), allow localhost / 127.0.0.1 / testserver
        is_debug = getattr(settings, 'DEBUG', False)
        valid_dev_hosts = {'localhost', '127.0.0.1', 'testserver'}

        # Allowed host set
        valid_hosts = {canonical_domain, f"www.{canonical_domain}"}
        if is_debug:
            valid_hosts.update(valid_dev_hosts)

        # Host shield: any host outside valid_hosts returns plain 404 text response
        if not raw_host or raw_host not in valid_hosts:
            return HttpResponseNotFound("Not Found", content_type="text/plain")

        # 301 redirect www to canonical apex domain
        if raw_host == f"www.{canonical_domain}":
            return HttpResponsePermanentRedirect(f"{canonical_protocol}://{canonical_domain}{request.get_full_path()}")

        # 301 redirect HTTP to HTTPS in production
        proto = request.META.get('HTTP_X_FORWARDED_PROTO', request.scheme or 'http').lower()
        if not is_debug and proto != 'https':
            return HttpResponsePermanentRedirect(f"https://{canonical_domain}{request.get_full_path()}")

        return self.get_response(request)
