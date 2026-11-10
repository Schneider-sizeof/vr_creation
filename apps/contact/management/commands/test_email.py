"""
Management command to test email configuration.
Usage:
    python manage.py test_email [optional_recipient] --settings=config.settings.prod
"""
from django.core.management.base import BaseCommand
from django.core.mail import EmailMessage, get_connection
from django.conf import settings


class Command(BaseCommand):
    help = 'Test SMTP email sending with current settings'

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

        self.stdout.write("Tentative d'envoi d'un email de test...")

        try:
            email = EmailMessage(
                subject="[TEST] VR Creation -- Configuration Email Reussie",
                body=(
                    "Felicitations !\n\n"
                    "Votre configuration email pour VR Creation fonctionne parfaitement.\n"
                    f"Envoye depuis : {settings.DEFAULT_FROM_EMAIL}\n"
                    f"Serveur hote  : {settings.EMAIL_HOST}:{settings.EMAIL_PORT}\n\n"
                    "Les notifications de contact et les emails de confirmation clients seront bien distribues.\n"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[recipient],
                reply_to=[settings.CONTACT_EMAIL],
            )
            email.send(fail_silently=False)

            self.stdout.write(self.style.SUCCESS(
                f"[OK] Email de test envoye avec succes a : {recipient} !"
            ))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"[ERREUR] ECHEC DE L'ENVOI : {e}"))
            self.stdout.write("\nConseils de depannage pour Namecheap cPanel :")
            self.stdout.write("1. Verifiez que la boite email 'contact@vrcreationcompany.com' existe bien dans cPanel > Email Accounts.")
            self.stdout.write("2. Verifiez que le mot de passe dans .env correspond exactement au mot de passe de cette boite.")
            self.stdout.write("3. Si EMAIL_PORT=465 : mettez EMAIL_USE_SSL=True et EMAIL_USE_TLS=False dans .env.")
            self.stdout.write("4. Si EMAIL_PORT=587 : mettez EMAIL_USE_SSL=False et EMAIL_USE_TLS=True dans .env.")
            self.stdout.write("5. Pour l'hote, essayez 'mail.vrcreationcompany.com' ou le hostname cPanel (ex: premium69.web-hosting.com).")
