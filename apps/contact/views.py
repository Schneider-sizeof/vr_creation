"""
Contact views with rate limiting and math captcha.
"""
import time
import random
from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _, gettext, get_language

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

            # Send email notification to Admin (vrcreation.company@gmail.com)
            try:
                admin_subject = f"[VR CREATION] Nouveau message de contact : {submission.subject}"
                created_str = submission.created_at.strftime('%d/%m/%Y %H:%M') if submission.created_at else ''
                admin_body = (
                    f"VR CREATION — NOUVEAU MESSAGE DE CONTACT\n"
                    f"============================================================\n\n"
                    f"Une nouvelle demande de contact a été reçue via le site web :\n\n"
                    f"• Nom / Prénom      : {submission.name}\n"
                    f"• Adresse Email     : {submission.email}\n"
                    f"• Téléphone         : {submission.phone or 'Non renseigné'}\n"
                    f"• Secteur           : {submission.get_sector_display()}\n"
                    f"• Sujet             : {submission.subject}\n"
                    f"• Date d'envoi      : {created_str}\n\n"
                    f"------------------------------------------------------------\n"
                    f"MESSAGE DU CLIENT :\n"
                    f"------------------------------------------------------------\n"
                    f"{submission.message}\n\n"
                    f"============================================================\n"
                    f"VR CREATION — Studio de production digitale & 3D\n"
                    f"Astuce : Cliquez simplement sur 'Répondre' dans votre boîte mail pour répondre directement au client ({submission.email}).\n"
                )
                admin_msg = EmailMessage(
                    subject=admin_subject,
                    body=admin_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[settings.CONTACT_EMAIL],
                    reply_to=[submission.email],
                )
                admin_msg.send(fail_silently=True)
            except Exception:
                pass

            # Send automatic confirmation email to Sender (User)
            try:
                lang = get_language() or 'fr'
                if lang.startswith('ar'):
                    user_subject = f"VR CREATION — تأكيد استلام رسالتكم"
                    user_body = (
                        f"VR CREATION\n"
                        f"============================================================\n"
                        f"تأكيد استلام رسالتكم\n"
                        f"============================================================\n\n"
                        f"مرحباً {submission.name}،\n\n"
                        f"شكراً لتواصلكم مع VR CREATION.\n\n"
                        f"لقد تم استلام رسالتكم بخصوص \"{submission.subject}\" بنجاح.\n"
                        f"يقوم فريقنا بمراجعة طلبكم وسيقوم أحد مستشارينا بالرد عليكم في أقرب وقت ممكن (خلال 24 ساعة عمل).\n\n"
                        f"------------------------------------------------------------\n"
                        f"ملخص طلبكم :\n"
                        f"------------------------------------------------------------\n"
                        f"• الاسم : {submission.name}\n"
                        f"• البريد الإلكتروني : {submission.email}\n"
                        f"• الهاتف : {submission.phone or 'غير محدد'}\n"
                        f"• المجال : {submission.get_sector_display()}\n"
                        f"• الموضوع : {submission.subject}\n\n"
                        f"نص الرسالة :\n"
                        f"{submission.message}\n\n"
                        f"------------------------------------------------------------\n"
                        f"إذا كنتم ترغبون في إضافة أي تفاصيل أخرى، يمكنكم الرد مباشرة على هذه الرسالة.\n\n"
                        f"مع أطيب التحيات،\n"
                        f"فريق VR CREATION\n"
                        f"البريد الإلكتروني : vrcreation.company@gmail.com\n"
                        f"الموقع الإلكتروني : https://vrcreationn.pythonanywhere.com\n"
                        f"============================================================\n"
                    )
                elif lang.startswith('en'):
                    user_subject = f"VR CREATION — Confirmation of your message receipt"
                    user_body = (
                        f"VR CREATION\n"
                        f"============================================================\n"
                        f"Message Confirmation\n"
                        f"============================================================\n\n"
                        f"Hello {submission.name},\n\n"
                        f"Thank you for contacting VR CREATION.\n\n"
                        f"We have successfully received your inquiry regarding \"{submission.subject}\".\n"
                        f"Our team is currently reviewing your request and a specialist will get back to you promptly (typically within 24 business hours).\n\n"
                        f"------------------------------------------------------------\n"
                        f"SUMMARY OF YOUR INQUIRY:\n"
                        f"------------------------------------------------------------\n"
                        f"• Name: {submission.name}\n"
                        f"• Email: {submission.email}\n"
                        f"• Phone: {submission.phone or 'Not provided'}\n"
                        f"• Sector: {submission.get_sector_display()}\n"
                        f"• Subject: {submission.subject}\n\n"
                        f"Message:\n"
                        f"{submission.message}\n\n"
                        f"------------------------------------------------------------\n"
                        f"If you have additional details or files to add, simply reply directly to this email.\n\n"
                        f"Best regards,\n"
                        f"The VR CREATION Team\n"
                        f"Email: vrcreation.company@gmail.com\n"
                        f"Website: https://vrcreationn.pythonanywhere.com\n"
                        f"============================================================\n"
                    )
                else:  # Default French
                    user_subject = f"VR CREATION — Confirmation de réception de votre message"
                    user_body = (
                        f"VR CREATION\n"
                        f"============================================================\n"
                        f"Confirmation de réception de votre message\n"
                        f"============================================================\n\n"
                        f"Bonjour {submission.name},\n\n"
                        f"Nous vous remercions d'avoir contacté VR CREATION.\n\n"
                        f"Nous avons bien reçu votre demande concernant : \"{submission.subject}\".\n"
                        f"Notre équipe étudie actuellement votre message et un conseiller dédié vous répondra dans les plus brefs délais (généralement sous 24h ouvrées).\n\n"
                        f"------------------------------------------------------------\n"
                        f"RÉCAPITULATIF DE VOTRE DEMANDE :\n"
                        f"------------------------------------------------------------\n"
                        f"• Nom / Prénom : {submission.name}\n"
                        f"• Email : {submission.email}\n"
                        f"• Téléphone : {submission.phone or 'Non renseigné'}\n"
                        f"• Secteur : {submission.get_sector_display()}\n"
                        f"• Sujet : {submission.subject}\n\n"
                        f"Message transmis :\n"
                        f"{submission.message}\n\n"
                        f"------------------------------------------------------------\n"
                        f"Si vous souhaitez apporter des éléments complémentaires, vous pouvez répondre directement à cet email.\n\n"
                        f"Bien cordialement,\n"
                        f"L'équipe VR CREATION\n"
                        f"Email : vrcreation.company@gmail.com\n"
                        f"Site web : https://vrcreationn.pythonanywhere.com\n"
                        f"============================================================\n"
                    )

                user_msg = EmailMessage(
                    subject=user_subject,
                    body=user_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[submission.email],
                    reply_to=[settings.CONTACT_EMAIL],
                )
                user_msg.send(fail_silently=True)
            except Exception:
                pass

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
