"""
Modern, text-only HTML & plain-text email builders for VR Creation.
Zero external images or trackers to maximize deliverability and avoid spam filters.
Uses clean inline CSS with system typography and VR Creation brand palette.
"""
import html
import logging
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.translation import get_language

logger = logging.getLogger(__name__)

# Brand colors
PRIMARY = "#3D8EB9"
PRIMARY_DARK = "#2A6A8A"
PRIMARY_LIGHT = "#E8F4F8"
TEXT_DARK = "#1E293B"
TEXT_MUTED = "#64748B"
BORDER_COLOR = "#E2E8F0"
BG_LIGHT = "#F8FAFC"
WHITE = "#FFFFFF"

FONT_STACK = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"


def _base_email_wrapper(content_html, is_rtl=False):
    """Wraps inner content in a responsive, modern card layout with zero images."""
    direction = "rtl" if is_rtl else "ltr"
    align = "right" if is_rtl else "left"

    return f"""<!DOCTYPE html>
<html lang="fr" dir="{direction}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VR Creation</title>
</head>
<body style="margin: 0; padding: 24px 12px; background-color: #F1F5F9; font-family: {FONT_STACK}; -webkit-font-smoothing: antialiased; line-height: 1.6; color: {TEXT_DARK};">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width: 580px; margin: 0 auto; background-color: {WHITE}; border-radius: 16px; overflow: hidden; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.06); border: 1px solid {BORDER_COLOR};">
        <!-- Top Brand Accent Bar -->
        <tr>
            <td style="height: 5px; background: linear-gradient(90deg, {PRIMARY} 0%, {PRIMARY_DARK} 100%); font-size: 0; line-height: 0;">&nbsp;</td>
        </tr>
        <!-- Main Content -->
        <tr>
            <td style="padding: 32px 28px; text-align: {align}; direction: {direction};">
                {content_html}
            </td>
        </tr>
        <!-- Modern Text Footer -->
        <tr>
            <td style="padding: 20px 28px; background-color: {BG_LIGHT}; border-top: 1px solid {BORDER_COLOR}; text-align: center; font-size: 12px; color: {TEXT_MUTED};">
                <div style="font-weight: 700; color: {TEXT_DARK}; margin-bottom: 4px; letter-spacing: 0.5px;">VR CREATION COMPANY</div>
                <div style="margin-bottom: 8px;">Ibn Batouta bureaux, Av. Youssef Ibn Tachfine, Tangier 90000, Maroc</div>
                <div>
                    <a href="https://vrcreationcompany.com" style="color: {PRIMARY}; text-decoration: none; font-weight: 600;">vrcreationcompany.com</a>
                    &nbsp;&bull;&nbsp;
                    <a href="tel:+212625071498" style="color: {TEXT_MUTED}; text-decoration: none;">+212 625 07 1498</a>
                    &nbsp;&bull;&nbsp;
                    <a href="mailto:contact@vrcreationcompany.com" style="color: {TEXT_MUTED}; text-decoration: none;">contact@vrcreationcompany.com</a>
                </div>
            </td>
        </tr>
    </table>
</body>
</html>"""


# =============================================================================
# ADMIN NOTIFICATION EMAIL
# =============================================================================

def build_admin_notification(submission):
    """Generates plain text and HTML for admin notification."""
    name = html.escape(submission.name or "")
    email = html.escape(submission.email or "")
    phone = html.escape(submission.phone or "Non renseigné")
    sector = html.escape(submission.get_sector_display() or "Non spécifié")
    subject = html.escape(submission.subject or "Demande de contact")
    created_str = submission.created_at.strftime('%d/%m/%Y à %H:%M') if submission.created_at else ''
    raw_message = submission.message or ""
    message_html = html.escape(raw_message).replace("\n", "<br>")

    # Plain text version
    plain_text = (
        f"VR CREATION — NOUVELLE DEMANDE DE CONTACT\n"
        f"============================================================\n\n"
        f"Une nouvelle demande a été envoyée depuis le site web :\n\n"
        f"• Nom / Prénom  : {submission.name}\n"
        f"• Email         : {submission.email}\n"
        f"• Téléphone     : {phone}\n"
        f"• Secteur       : {sector}\n"
        f"• Sujet         : {submission.subject}\n"
        f"• Reçu le       : {created_str}\n\n"
        f"------------------------------------------------------------\n"
        f"MESSAGE DU CLIENT :\n"
        f"------------------------------------------------------------\n"
        f"{raw_message}\n\n"
        f"============================================================\n"
        f"Pour répondre au client, cliquez simplement sur 'Répondre' dans votre boîte mail ({submission.email}).\n"
    )

    # Modern HTML version (clean CSS, cards, zero images)
    content_html = f"""
    <!-- Header with badge -->
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-bottom: 24px;">
        <tr>
            <td>
                <span style="display: inline-block; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: {PRIMARY_DARK}; background-color: {PRIMARY_LIGHT}; padding: 4px 10px; border-radius: 999px; margin-bottom: 8px;">Nouveau Message Web</span>
                <h1 style="margin: 0; font-size: 22px; font-weight: 800; color: {TEXT_DARK}; letter-spacing: -0.5px;">Demande de contact reçue</h1>
                <div style="font-size: 13px; color: {TEXT_MUTED}; margin-top: 4px;">Reçu le {created_str}</div>
            </td>
        </tr>
    </table>

    <!-- Sender Details Table -->
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color: {BG_LIGHT}; border: 1px solid {BORDER_COLOR}; border-radius: 12px; margin-bottom: 24px; font-size: 14px;">
        <tr>
            <td style="padding: 10px 16px; border-bottom: 1px solid {BORDER_COLOR}; color: {TEXT_MUTED}; width: 120px; font-weight: 600;">Client</td>
            <td style="padding: 10px 16px; border-bottom: 1px solid {BORDER_COLOR}; color: {TEXT_DARK}; font-weight: 700;">{name}</td>
        </tr>
        <tr>
            <td style="padding: 10px 16px; border-bottom: 1px solid {BORDER_COLOR}; color: {TEXT_MUTED}; font-weight: 600;">Email</td>
            <td style="padding: 10px 16px; border-bottom: 1px solid {BORDER_COLOR};">
                <a href="mailto:{email}" style="color: {PRIMARY}; text-decoration: none; font-weight: 600;">{email}</a>
            </td>
        </tr>
        <tr>
            <td style="padding: 10px 16px; border-bottom: 1px solid {BORDER_COLOR}; color: {TEXT_MUTED}; font-weight: 600;">Téléphone</td>
            <td style="padding: 10px 16px; border-bottom: 1px solid {BORDER_COLOR}; color: {TEXT_DARK};">{phone}</td>
        </tr>
        <tr>
            <td style="padding: 10px 16px; border-bottom: 1px solid {BORDER_COLOR}; color: {TEXT_MUTED}; font-weight: 600;">Secteur</td>
            <td style="padding: 10px 16px; border-bottom: 1px solid {BORDER_COLOR}; color: {TEXT_DARK};">{sector}</td>
        </tr>
        <tr>
            <td style="padding: 10px 16px; color: {TEXT_MUTED}; font-weight: 600;">Sujet</td>
            <td style="padding: 10px 16px; color: {TEXT_DARK}; font-weight: 700;">{subject}</td>
        </tr>
    </table>

    <!-- Message Callout -->
    <div style="font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: {TEXT_MUTED}; margin-bottom: 8px;">Message transmis :</div>
    <div style="background-color: {WHITE}; border-left: 4px solid {PRIMARY}; border-top: 1px solid {BORDER_COLOR}; border-right: 1px solid {BORDER_COLOR}; border-bottom: 1px solid {BORDER_COLOR}; border-radius: 0 10px 10px 0; padding: 18px 20px; font-size: 14px; line-height: 1.7; color: {TEXT_DARK}; margin-bottom: 24px;">
        {message_html}
    </div>

    <!-- Quick Action Button -->
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
        <tr>
            <td align="center">
                <a href="mailto:{email}?subject=Re:%20{subject}" style="display: inline-block; background-color: {PRIMARY}; color: {WHITE}; font-size: 14px; font-weight: 700; text-decoration: none; padding: 12px 28px; border-radius: 8px; box-shadow: 0 2px 6px rgba(61, 142, 185, 0.35);">
                    Répondre au client ({name})
                </a>
            </td>
        </tr>
    </table>
    """

    return plain_text, _base_email_wrapper(content_html, is_rtl=False)


# =============================================================================
# CLIENT CONFIRMATION EMAIL (MULTILINGUAL: FR, EN, AR)
# =============================================================================

def build_user_confirmation(submission, lang=None):
    """Generates multilingual confirmation email for the client."""
    if not lang:
        lang = get_language() or 'fr'

    name = html.escape(submission.name or "")
    subject = html.escape(submission.subject or "")
    phone = html.escape(submission.phone or "")
    sector = html.escape(submission.get_sector_display() or "")
    raw_message = submission.message or ""
    message_html = html.escape(raw_message).replace("\n", "<br>")

    # --- ARABIC ---
    if lang.startswith('ar'):
        email_subject = f"VR CREATION — تأكيد استلام رسالتكم"
        is_rtl = True

        plain_text = (
            f"VR CREATION\n"
            f"============================================================\n"
            f"تأكيد استلام رسالتكم بنجاح\n"
            f"============================================================\n\n"
            f"مرحباً {submission.name}،\n\n"
            f"نشكركم على تواصلكم مع شركة VR CREATION في طنجة.\n\n"
            f"لقد تم استلام طلبكم بخصوص \"{submission.subject}\" بنجاح.\n"
            f"يقوم فريقنا حالياً بمراجعة تفاصيل مشروعكم وسيتواصل معكم أحد مستشارينا في أقرب وقت (خلال 24 ساعة عمل).\n\n"
            f"------------------------------------------------------------\n"
            f"ملخص طلبكم :\n"
            f"------------------------------------------------------------\n"
            f"• الاسم : {submission.name}\n"
            f"• الموضوع : {submission.subject}\n"
            f"• المجال : {sector or 'غير محدد'}\n"
            f"• نص الرسالة : {raw_message}\n\n"
            f"------------------------------------------------------------\n"
            f"إذا كنتم ترغبون في إضافة أي معلومات أخرى، يمكنكم الرد مباشرة على هذا البريد الإلكتروني.\n\n"
            f"مع أطيب التحيات،\n"
            f"فريق VR CREATION\n"
            f"الهاتف / واتساب : +212 625 07 1498\n"
            f"الموقع الإلكتروني : https://vrcreationcompany.com\n"
        )

        content_html = f"""
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-bottom: 20px;">
            <tr>
                <td style="text-align: right;">
                    <span style="display: inline-block; font-size: 11px; font-weight: 700; color: #166534; background-color: #DCFCE7; padding: 4px 12px; border-radius: 999px; margin-bottom: 12px;">تم الاستلام بنجاح &#10003;</span>
                    <h1 style="margin: 0; font-size: 22px; font-weight: 800; color: {TEXT_DARK};">مرحباً {name}،</h1>
                    <p style="font-size: 15px; color: {TEXT_MUTED}; margin-top: 8px; line-height: 1.7;">
                        نشكركم على تواصلكم مع <strong>VR CREATION</strong>. لقد تلقينا رسالتكم بخصوص <strong>"{subject}"</strong> بنجاح.
                    </p>
                </td>
            </tr>
        </table>

        <!-- Commitment Card -->
        <div style="background-color: {PRIMARY_LIGHT}; border: 1px solid rgba(61,142,185,0.25); border-radius: 12px; padding: 16px 20px; margin-bottom: 24px; text-align: right;">
            <div style="font-size: 14px; color: {PRIMARY_DARK}; font-weight: 700; margin-bottom: 4px;">التزامنا بالجودة والسرعة :</div>
            <div style="font-size: 13px; color: {TEXT_DARK}; line-height: 1.6;">
                يقوم مستشارونا حالياً بدراسة طلبكم وسنتواصل معكم باقتراح ملائم أو عرض أسعار مخصص <strong>خلال أقل من 24 ساعة عمل</strong>.
            </div>
        </div>

        <!-- Request Summary -->
        <div style="font-size: 12px; font-weight: 700; text-transform: uppercase; color: {TEXT_MUTED}; margin-bottom: 8px; text-align: right;">ملخص رسالتكم :</div>
        <div style="background-color: {BG_LIGHT}; border: 1px solid {BORDER_COLOR}; border-radius: 12px; padding: 16px 20px; font-size: 14px; line-height: 1.7; color: {TEXT_DARK}; margin-bottom: 24px; text-align: right;">
            <div style="margin-bottom: 6px;"><strong>الموضوع :</strong> {subject}</div>
            {f'<div style="margin-bottom: 6px;"><strong>المجال :</strong> {sector}</div>' if sector else ''}
            <div><strong>نص الرسالة :</strong></div>
            <div style="margin-top: 6px; padding-top: 6px; border-top: 1px dashed {BORDER_COLOR}; color: #334155;">{message_html}</div>
        </div>

        <!-- Note -->
        <p style="font-size: 13px; color: {TEXT_MUTED}; line-height: 1.6; text-align: right; margin-bottom: 0;">
            إذا كنتم ترغبون في إرفاق ملفات أو تفاصيل إضافية، يمكنكم الرد مباشرة على هذا البريد الإلكتروني.
        </p>
        """

    # --- ENGLISH ---
    elif lang.startswith('en'):
        email_subject = f"VR CREATION — Confirmation of your message receipt"
        is_rtl = False

        plain_text = (
            f"VR CREATION\n"
            f"============================================================\n"
            f"Thank you for reaching out to us!\n"
            f"============================================================\n\n"
            f"Hello {submission.name},\n\n"
            f"Thank you for contacting VR CREATION in Tangier.\n"
            f"We have successfully received your inquiry regarding \"{submission.subject}\".\n\n"
            f"Our team is currently reviewing your project details. A dedicated specialist will reach back to you shortly (typically within 24 business hours).\n\n"
            f"------------------------------------------------------------\n"
            f"INQUIRY SUMMARY:\n"
            f"------------------------------------------------------------\n"
            f"• Subject : {submission.subject}\n"
            f"• Sector  : {sector or 'Not specified'}\n"
            f"• Message : {raw_message}\n\n"
            f"------------------------------------------------------------\n"
            f"If you have additional details or files to share, simply reply directly to this email.\n\n"
            f"Best regards,\n"
            f"The VR CREATION Team\n"
            f"Phone / WhatsApp: +212 625 07 1498\n"
            f"Website: https://vrcreationcompany.com\n"
        )

        content_html = f"""
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-bottom: 20px;">
            <tr>
                <td>
                    <span style="display: inline-block; font-size: 11px; font-weight: 700; color: #166534; background-color: #DCFCE7; padding: 4px 12px; border-radius: 999px; margin-bottom: 12px;">Successfully Received &#10003;</span>
                    <h1 style="margin: 0; font-size: 22px; font-weight: 800; color: {TEXT_DARK};">Hello {name},</h1>
                    <p style="font-size: 15px; color: {TEXT_MUTED}; margin-top: 8px; line-height: 1.7;">
                        Thank you for contacting <strong>VR CREATION</strong>. We have received your message regarding <strong>"{subject}"</strong>.
                    </p>
                </td>
            </tr>
        </table>

        <!-- Commitment Card -->
        <div style="background-color: {PRIMARY_LIGHT}; border: 1px solid rgba(61,142,185,0.25); border-radius: 12px; padding: 16px 20px; margin-bottom: 24px;">
            <div style="font-size: 14px; color: {PRIMARY_DARK}; font-weight: 700; margin-bottom: 4px;">Our Commitment :</div>
            <div style="font-size: 13px; color: {TEXT_DARK}; line-height: 1.6;">
                Our team is currently evaluating your request. A dedicated specialist will get back to you with tailored recommendations <strong>within 24 business hours</strong>.
            </div>
        </div>

        <!-- Request Summary -->
        <div style="font-size: 12px; font-weight: 700; text-transform: uppercase; color: {TEXT_MUTED}; margin-bottom: 8px;">Summary of your message:</div>
        <div style="background-color: {BG_LIGHT}; border: 1px solid {BORDER_COLOR}; border-radius: 12px; padding: 16px 20px; font-size: 14px; line-height: 1.7; color: {TEXT_DARK}; margin-bottom: 24px;">
            <div style="margin-bottom: 6px;"><strong>Subject:</strong> {subject}</div>
            {f'<div style="margin-bottom: 6px;"><strong>Sector:</strong> {sector}</div>' if sector else ''}
            <div><strong>Message:</strong></div>
            <div style="margin-top: 6px; padding-top: 6px; border-top: 1px dashed {BORDER_COLOR}; color: #334155;">{message_html}</div>
        </div>

        <!-- Note -->
        <p style="font-size: 13px; color: {TEXT_MUTED}; line-height: 1.6; margin-bottom: 0;">
            Need to add more details or attachments? Simply reply directly to this email.
        </p>
        """

    # --- FRENCH (Default) ---
    else:
        email_subject = f"VR CREATION — Confirmation de réception de votre message"
        is_rtl = False

        plain_text = (
            f"VR CREATION\n"
            f"============================================================\n"
            f"Confirmation de réception de votre message\n"
            f"============================================================\n\n"
            f"Bonjour {submission.name},\n\n"
            f"Nous vous remercions d'avoir contacté VR CREATION à Tanger.\n"
            f"Nous avons bien reçu votre demande concernant : \"{submission.subject}\".\n\n"
            f"Notre équipe étudie actuellement votre projet avec attention. Un conseiller dédié vous répondra dans les plus brefs délais (généralement sous 24h ouvrées).\n\n"
            f"------------------------------------------------------------\n"
            f"RÉCAPITULATIF DE VOTRE DEMANDE :\n"
            f"------------------------------------------------------------\n"
            f"• Sujet   : {submission.subject}\n"
            f"• Secteur : {sector or 'Non spécifié'}\n"
            f"• Message : {raw_message}\n\n"
            f"------------------------------------------------------------\n"
            f"Si vous souhaitez apporter des éléments complémentaires, vous pouvez répondre directement à cet email.\n\n"
            f"Bien cordialement,\n"
            f"L'équipe VR CREATION\n"
            f"Téléphone / WhatsApp : +212 625 07 1498\n"
            f"Site web : https://vrcreationcompany.com\n"
        )

        content_html = f"""
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-bottom: 20px;">
            <tr>
                <td>
                    <span style="display: inline-block; font-size: 11px; font-weight: 700; color: #166534; background-color: #DCFCE7; padding: 4px 12px; border-radius: 999px; margin-bottom: 12px;">Bien reçu &#10003;</span>
                    <h1 style="margin: 0; font-size: 22px; font-weight: 800; color: {TEXT_DARK};">Bonjour {name},</h1>
                    <p style="font-size: 15px; color: {TEXT_MUTED}; margin-top: 8px; line-height: 1.7;">
                        Nous vous remercions d'avoir contacté <strong>VR CREATION</strong>. Nous avons bien reçu votre demande concernant <strong>"{subject}"</strong>.
                    </p>
                </td>
            </tr>
        </table>

        <!-- Commitment Card -->
        <div style="background-color: {PRIMARY_LIGHT}; border: 1px solid rgba(61,142,185,0.25); border-radius: 12px; padding: 16px 20px; margin-bottom: 24px;">
            <div style="font-size: 14px; color: {PRIMARY_DARK}; font-weight: 700; margin-bottom: 4px;">Notre engagement :</div>
            <div style="font-size: 13px; color: {TEXT_DARK}; line-height: 1.6;">
                Notre équipe étudie actuellement les spécificités de votre projet. Un conseiller dédié vous répondra <strong>sous 24h ouvrées</strong> avec un retour adapté.
            </div>
        </div>

        <!-- Request Summary -->
        <div style="font-size: 12px; font-weight: 700; text-transform: uppercase; color: {TEXT_MUTED}; margin-bottom: 8px;">Récapitulatif de votre message :</div>
        <div style="background-color: {BG_LIGHT}; border: 1px solid {BORDER_COLOR}; border-radius: 12px; padding: 16px 20px; font-size: 14px; line-height: 1.7; color: {TEXT_DARK}; margin-bottom: 24px;">
            <div style="margin-bottom: 6px;"><strong>Sujet :</strong> {subject}</div>
            {f'<div style="margin-bottom: 6px;"><strong>Secteur :</strong> {sector}</div>' if sector else ''}
            <div><strong>Message :</strong></div>
            <div style="margin-top: 6px; padding-top: 6px; border-top: 1px dashed {BORDER_COLOR}; color: #334155;">{message_html}</div>
        </div>

        <!-- Note -->
        <p style="font-size: 13px; color: {TEXT_MUTED}; line-height: 1.6; margin-bottom: 0;">
            Si vous souhaitez apporter des documents ou des précisions complémentaires, vous pouvez répondre directement à cet email.
        </p>
        """

    return email_subject, plain_text, _base_email_wrapper(content_html, is_rtl=is_rtl)


# =============================================================================
# SEND CONTROLLER FUNCTION
# =============================================================================

def send_contact_submission_emails(submission):
    """
    Sends both Admin Notification and Client Confirmation emails using multipart/alternative
    (both plain text and modern text-only HTML) for optimal spam filter delivery.
    """
    # 1. Admin Notification Email
    try:
        admin_subject = f"[VR CREATION] Nouveau message de contact : {submission.subject}"
        admin_plain, admin_html = build_admin_notification(submission)

        admin_msg = EmailMultiAlternatives(
            subject=admin_subject,
            body=admin_plain,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.CONTACT_EMAIL],
            reply_to=[submission.email],
        )
        admin_msg.attach_alternative(admin_html, "text/html")
        admin_msg.send(fail_silently=False)
        logger.info("Admin notification email sent successfully for submission #%s", getattr(submission, 'pk', '?'))
    except Exception as e:
        logger.error("Failed to send admin notification email for submission #%s: %s", getattr(submission, 'pk', '?'), e, exc_info=True)

    # 2. Client Confirmation Email
    try:
        lang = get_language() or 'fr'
        user_subject, user_plain, user_html = build_user_confirmation(submission, lang=lang)

        user_msg = EmailMultiAlternatives(
            subject=user_subject,
            body=user_plain,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[submission.email],
            reply_to=[settings.CONTACT_EMAIL],
        )
        user_msg.attach_alternative(user_html, "text/html")
        user_msg.send(fail_silently=False)
        logger.info("User confirmation email sent successfully to %s for submission #%s", getattr(submission, 'email', '?'), getattr(submission, 'pk', '?'))
    except Exception as e:
        logger.error("Failed to send user confirmation email to %s: %s", getattr(submission, 'email', '?'), e, exc_info=True)
