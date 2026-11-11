"""
Contact views with rate limiting, honeypot and time-based anti-spam protection.
"""
import time
import logging

logger = logging.getLogger(__name__)
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .forms import ContactForm
from .emails import send_contact_submission_emails
from apps.seo.models import PageSEO


def _check_rate_limit(request):
    """Session-based rate limiting for contact form."""
    now = time.time()
    submissions = request.session.get('contact_submissions', [])

    # Remove old entries
    window = settings.CONTACT_RATE_LIMIT_SECONDS
    submissions = [ts for ts in submissions if now - ts < window]

    if len(submissions) >= settings.CONTACT_RATE_LIMIT_MAX:
        return False

    submissions.append(now)
    request.session['contact_submissions'] = submissions
    return True


def contact_view(request):
    """Contact form page with honeypot, timestamp verification and rate limiting."""
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if not _check_rate_limit(request):
            form.add_error(None, _(
                'Vous avez envoyé trop de messages. Veuillez réessayer dans quelques minutes.'
            ))
        elif form.is_valid():
            submission = form.save()

            # Send both Admin Notification and Client Confirmation emails (Modern, text-only HTML + plain-text)
            try:
                send_contact_submission_emails(submission)
            except Exception as e:
                logger.error("Failed to send contact emails: %s", e)

            return redirect(reverse('contact:confirmation'))
    else:
        form = ContactForm()

    try:
        page_seo = PageSEO.objects.get(page_identifier='contact')
    except PageSEO.DoesNotExist:
        page_seo = None

    return render(request, 'contact/contact.html', {
        'form': form,
        'page_seo': page_seo,
        'page_identifier': 'contact',
    })


def contact_confirmation(request):
    """Thank you page after form submission."""
    return render(request, 'contact/confirmation.html', {
        'page_identifier': 'contact_confirmation',
    })
