"""
Contact views with rate limiting and math captcha.
"""
import time
import random
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _, gettext

from .forms import ContactForm
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
    """Contact form page with honeypot, math captcha and rate limiting."""
    if request.method == 'POST':
        # Retrieve the captcha numbers from the session
        num1 = request.session.get('captcha_num1', 0)
        num2 = request.session.get('captcha_num2', 0)
        form = ContactForm(request.POST, captcha_num1=num1, captcha_num2=num2)

        if not _check_rate_limit(request):
            form.add_error(None, _(
                'Vous avez envoyé trop de messages. Veuillez réessayer dans quelques minutes.'
            ))
        elif form.is_valid():
            submission = form.save()

            # Send email notification
            try:
                subject = f"[VR Creation] Nouveau message : {submission.subject}"
                body = (
                    f"Nom : {submission.name}\n"
                    f"Email : {submission.email}\n"
                    f"Téléphone : {submission.phone}\n"
                    f"Secteur : {submission.get_sector_display()}\n"
                    f"Sujet : {submission.subject}\n\n"
                    f"Message :\n{submission.message}\n"
                )
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.CONTACT_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass  # Email failure shouldn't block form submission

            # Clear captcha from session
            request.session.pop('captcha_num1', None)
            request.session.pop('captcha_num2', None)

            return redirect(reverse('contact:confirmation'))
    else:
        # Generate new captcha numbers for GET request
        num1 = random.randint(2, 9)
        num2 = random.randint(1, 9)
        form = ContactForm(captcha_num1=num1, captcha_num2=num2)

    # Store captcha numbers in session
    request.session['captcha_num1'] = form.captcha_num1
    request.session['captcha_num2'] = form.captcha_num2

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
