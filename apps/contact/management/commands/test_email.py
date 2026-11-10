"""
Management command to test email configuration with the modern HTML template.
Usage:
    python manage.py test_email [optional_recipient] --settings=config.settings.prod
"""
from django.core.management.base import BaseCommand
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from apps.contact.emails import _base_email_wrapper, PRIMARY, TEXT_DARK, TEXT_MUTED, BG_LIGHT, BORDER_COLOR, PRIMARY_LIGHT, PRIMARY_DARK


class Command(BaseCommand):
    help = 'Test SMTP email sending with current settings and modern text-only design'

    def add_arguments(self, parser):
        parser.add_argument(
            'recipient',
            nargs='?',
            default=settings.CONTACT_EMAIL,
            help='Recipient email address (defaults to CONTACT_EMAIL: contact@vrcreationcompany.com)'
        )

    def handle(self, *args, **options):
        recipient = options['recipient']
        self.stdout.write(self.style.MIGRATE_HEADING("=== VR CREATION -- TEST CONFIGURATION EMAIL ==="))
        self.stdout.write(f"- EMAIL_BACKEND     : {settings.EMAIL_BACKEND}")
        self.stdout.write(f"- EMAIL_HOST        : {settings.EMAIL_HOST}")
        self.stdout.write(f"- EMAIL_PORT        : {settings.EMAIL_PORT}")
        self.stdout.write(f"- EMAIL_USE_SSL     : {getattr(settings, 'EMAIL_USE_SSL', False)}")
        self.stdout.write(f"- EMAIL_USE_TLS     : {getattr(settings, 'EMAIL_USE_TLS', False)}")
        self.stdout.write(f"- EMAIL_HOST_USER   : {settings.EMAIL_HOST_USER}")
        self.stdout.write(f"- DEFAULT_FROM_EMAIL: {settings.DEFAULT_FROM_EMAIL}")
        self.stdout.write(f"- CONTACT_EMAIL     : {settings.CONTACT_EMAIL}")
        self.stdout.write(f"- Recipient test    : {recipient}")
        self.stdout.write("--------------------------------------------------")

        if not settings.EMAIL_HOST_PASSWORD and 'console' not in settings.EMAIL_BACKEND.lower():
            self.stdout.write(self.style.WARNING(
                "ATTENTION : EMAIL_HOST_PASSWORD est vide ! Veuillez definir EMAIL_HOST_PASSWORD dans le fichier .env."
            ))

        self.stdout.write("Tentative d'envoi d'un email de test moderne (HTML + texte pur)...")

        plain_text = (
            "VR CREATION -- TEST CONFIGURATION REUSSI\n"
            "============================================================\n\n"
            "Felicitations !\n\n"
            "Votre configuration email pour VR Creation fonctionne parfaitement.\n"
            f"Envoye depuis : {settings.DEFAULT_FROM_EMAIL}\n"
            f"Serveur hote  : {settings.EMAIL_HOST}:{settings.EMAIL_PORT}\n\n"
            "Les notifications et confirmations de contact seront distribuees avec le design moderne (zero image, anti-spam garanti).\n\n"
            "VR CREATION COMPANY -- Tanger, Maroc\n"
            "https://vrcreationcompany.com\n"
        )

        content_html = f"""
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-bottom: 24px;">
            <tr>
                <td>
                    <span style="display: inline-block; font-size: 11px; font-weight: 700; color: #166534; background-color: #DCFCE7; padding: 4px 12px; border-radius: 999px; margin-bottom: 12px;">Configuration Valid&eacute;e &#10003;</span>
                    <h1 style="margin: 0; font-size: 22px; font-weight: 800; color: {TEXT_DARK};">Test de messagerie r&eacute;ussi</h1>
                    <p style="font-size: 14px; color: {TEXT_MUTED}; margin-top: 6px; line-height: 1.6;">
                        Ce message confirme que votre serveur SMTP communique parfaitement avec Django.
                    </p>
                </td>
            </tr>
        </table>

        <!-- Details Card -->
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color: {BG_LIGHT}; border: 1px solid {BORDER_COLOR}; border-radius: 12px; margin-bottom: 24px; font-size: 13px;">
            <tr>
                <td style="padding: 10px 16px; border-bottom: 1px solid {BORDER_COLOR}; color: {TEXT_MUTED}; width: 140px; font-weight: 600;">Serveur SMTP</td>
                <td style="padding: 10px 16px; border-bottom: 1px solid {BORDER_COLOR}; color: {TEXT_DARK}; font-weight: 700;">{settings.EMAIL_HOST}:{settings.EMAIL_PORT}</td>
            </tr>
            <tr>
                <td style="padding: 10px 16px; border-bottom: 1px solid {BORDER_COLOR}; color: {TEXT_MUTED}; font-weight: 600;">Exp&eacute;diteur</td>
                <td style="padding: 10px 16px; border-bottom: 1px solid {BORDER_COLOR}; color: {TEXT_DARK};">{settings.DEFAULT_FROM_EMAIL}</td>
            </tr>
            <tr>
                <td style="padding: 10px 16px; color: {TEXT_MUTED}; font-weight: 600;">Design & Anti-spam</td>
                <td style="padding: 10px 16px; color: #166534; font-weight: 700;">100% texte & CSS (z&eacute;ro image, d&eacute;livrabilit&eacute; maximale)</td>
            </tr>
        </table>

        <div style="background-color: {PRIMARY_LIGHT}; border: 1px solid rgba(61,142,185,0.25); border-radius: 12px; padding: 14px 18px; font-size: 13px; color: {PRIMARY_DARK}; line-height: 1.6;">
            <strong>Pr&ecirc;t pour la production :</strong> Dès qu'un visiteur remplit le formulaire de contact, vous recevrez une notification d&eacute;taill&eacute;e et le client recevra imm&eacute;diatement un accus&eacute; de r&eacute;ception dans sa langue (fran&ccedil;ais, arabe ou anglais).
        </div>
        """

        html_body = _base_email_wrapper(content_html, is_rtl=False)

        try:
            email = EmailMultiAlternatives(
                subject="[TEST] VR Creation -- Configuration Email Validee",
                body=plain_text,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[recipient],
                reply_to=[settings.CONTACT_EMAIL],
            )
            email.attach_alternative(html_body, "text/html")
            email.send(fail_silently=False)

            self.stdout.write(self.style.SUCCESS(
                f"[OK] Email de test envoye avec succes a : {recipient} !"
            ))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"[ERREUR] ECHEC DE L'ENVOI : {e}"))
            self.stdout.write("\nConseils de depannage pour Namecheap cPanel :")
            self.stdout.write("1. Verifiez que EMAIL_HOST=premium69.web-hosting.com (pour eviter l'erreur SSL de certificat).")
            self.stdout.write("2. Verifiez que EMAIL_PORT=465, EMAIL_USE_SSL=True, EMAIL_USE_TLS=False dans .env.")
            self.stdout.write("3. Verifiez que EMAIL_HOST_PASSWORD correspond au mot de passe de la boite contact@vrcreationcompany.com.")
