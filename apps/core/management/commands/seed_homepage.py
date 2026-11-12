"""
Seed homepage data: hero settings + 4 StrategicSuccess examples.
Usage: python manage.py seed_homepage
"""
import os
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from apps.core.models import SiteSettings, StrategicSuccess

# Tiny 1x1 pixel black JPEG image
TINY_JPEG = (
    b'\xff\xd8\xff\xdb\x00\x43\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07'
    b'\t\t\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f'
    b'\x1e\x1d\x1a\x1c\x1c$&\',#\x1c\x1f(15),+(B7\xff\xc0'
    b'\x00\x0b\x08\x00\x01\x00\x01\x01\x01\x11\x00\xff\xc4\x00\x15\x00\x01'
    b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09'
    b'\xff\xc4\x00\x14\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\xff\xda\x00\x0c\x01\x01\x00\x00\x3f\x00\xbf\x80'
    b'\x00\x01\xff\xd9'
)

STRATEGIC_EXAMPLES = [
    {
        'title_fr': 'Entreprise & startup',
        'title_en': 'Business & startup',
        'title_ar': 'Ø´Ø±ÙƒØ© ÙˆÙ…Ø´Ø±ÙˆØ¹ Ù†Ø§Ø´Ø¦',
        'importance_fr': 'Construire une image de marque forte pour se lancer avec impact.',
        'importance_en': 'Build a strong brand image to launch with impact.',
        'importance_ar': 'Ø¨Ù†Ø§Ø¡ ØµÙˆØ±Ø© Ø¹Ù„Ø§Ù…Ø© ØªØ¬Ø§Ø±ÙŠØ© Ù‚ÙˆÙŠØ© Ù„Ù„Ø§Ù†Ø·Ù„Ø§Ù‚ Ø¨ØªØ£Ø«ÙŠØ±.',
        'slug': 'entreprise-startup',
        'icon': 'fas fa-briefcase',
        'order': 1,
    },
    {
        'title_fr': 'Restaurant & commerce',
        'title_en': 'Restaurant & retail',
        'title_ar': 'Ù…Ø·Ø¹Ù… ÙˆØªØ¬Ø§Ø±Ø©',
        'importance_fr': 'Attirer les clients avec un visuel professionnel et engageant.',
        'importance_en': 'Attract customers with professional and engaging visuals.',
        'importance_ar': 'Ø¬Ø°Ø¨ Ø§Ù„Ø¹Ù…Ù„Ø§Ø¡ Ø¨Ù…Ø±Ø¦ÙŠØ§Øª Ø§Ø­ØªØ±Ø§ÙÙŠØ© ÙˆØ¬Ø°Ø§Ø¨Ø©.',
        'slug': 'restaurant-commerce',
        'icon': 'fas fa-store',
        'order': 2,
    },
    {
        'title_fr': 'Professionnel & freelance',
        'title_en': 'Professional & freelancer',
        'title_ar': 'Ù…Ù‡Ù†ÙŠ ÙˆÙ…Ø³ØªÙ‚Ù„',
        'importance_fr': 'Se dÃ©marquer avec un portfolio et une prÃ©sence digitale unique.',
        'importance_en': 'Stand out with a unique portfolio and digital presence.',
        'importance_ar': 'Ø§Ù„ØªÙ…ÙŠØ² Ø¨Ù…Ù„Ù Ø£Ø¹Ù…Ø§Ù„ ÙˆØ­Ø¶ÙˆØ± Ø±Ù‚Ù…ÙŠ ÙØ±ÙŠØ¯.',
        'slug': 'professionnel-freelance',
        'icon': 'fas fa-user-tie',
        'order': 3,
    },
    {
        'title_fr': 'Ã‰vÃ©nementiel & salons',
        'title_en': 'Events & exhibitions',
        'title_ar': 'ÙØ¹Ø§Ù„ÙŠØ§Øª ÙˆÙ…Ø¹Ø§Ø±Ø¶',
        'importance_fr': 'Captiver votre audience avec des visuels et vidÃ©os percutants.',
        'importance_en': 'Captivate your audience with striking visuals and videos.',
        'importance_ar': 'Ø¥Ø¨Ù‡Ø§Ø± Ø§Ù„Ø¬Ù…Ù‡ÙˆØ± Ø¨Ù…Ø±Ø¦ÙŠØ§Øª ÙˆÙÙŠØ¯ÙŠÙˆÙ‡Ø§Øª Ù…Ø¤Ø«Ø±Ø©.',
        'slug': 'evenementiel-salons',
        'icon': 'fas fa-calendar-star',
        'order': 4,
    },
]

class Command(BaseCommand):
    help = 'Seed homepage data: hero settings and 4 strategic success examples.'

    def add_arguments(self, parser):
        parser.add_argument('--force', action='store_true',
                            help='Overwrite existing strategic successes')

    def handle(self, *args, **options):
        force = options.get('force', False)

        # 1. Seed hero settings into SiteSettings
        self.stdout.write('\nâ€” Seeding hero settings â€”')
        settings = SiteSettings.load()
        settings.hero_headline_fr = "CrÃ©ation visuelle professionnelle Ã  Tanger â€” Photo, VidÃ©o, Branding & Web"
        settings.hero_headline_en = "Professional visual creation in Tanger â€” Photo, Video, Branding & Web"
        settings.hero_headline_ar = "Ø¥Ø¨Ø¯Ø§Ø¹ Ø¨ØµØ±ÙŠ Ø§Ø­ØªØ±Ø§ÙÙŠ ÙÙŠ Ø·Ù†Ø¬Ø© â€” ØªØµÙˆÙŠØ±ØŒ ÙÙŠØ¯ÙŠÙˆØŒ Ø¨Ø±Ø§Ù†Ø¯ÙŠÙ†Øº ÙˆÙˆÙŠØ¨"
        settings.hero_subheadline_fr = "Nous accompagnons les entreprises de Tanger et du Nord du Maroc avec des solutions crÃ©atives sur mesure : photographie, vidÃ©o, branding et dÃ©veloppement web."
        settings.hero_subheadline_en = "We support businesses in Tanger and Northern Morocco with tailored creative solutions: photography, video, branding and web development."
        settings.hero_subheadline_ar = "Ù†Ø±Ø§ÙÙ‚ Ø§Ù„Ø´Ø±ÙƒØ§Øª ÙÙŠ Ø·Ù†Ø¬Ø© ÙˆØ´Ù…Ø§Ù„ Ø§Ù„Ù…ØºØ±Ø¨ Ø¨Ø­Ù„ÙˆÙ„ Ø¥Ø¨Ø¯Ø§Ø¹ÙŠØ© Ù…Ø®ØµØµØ©: ØªØµÙˆÙŠØ±ØŒ ÙÙŠØ¯ÙŠÙˆØŒ Ø¨Ø±Ø§Ù†Ø¯ÙŠÙ†Øº ÙˆØªØ·ÙˆÙŠØ± ÙˆÙŠØ¨."
        settings.hero_cta1_label_fr = "DÃ©couvrir nos services"
        settings.hero_cta1_label_en = "Discover our services"
        settings.hero_cta1_label_ar = "Ø§ÙƒØªØ´Ù Ø®Ø¯Ù…Ø§ØªÙ†Ø§"
        settings.hero_cta1_link = "#services"
        settings.hero_cta2_label_fr = "Nous contacter"
        settings.hero_cta2_label_en = "Contact us"
        settings.hero_cta2_label_ar = "Ø§ØªØµÙ„ Ø¨Ù†Ø§"
        settings.hero_cta2_link = "/contact/"
        settings.phone = "+212 625 07 1498"
        settings.address_fr = "Avenue Ibn Tachfine, bureaux Ibn Battouta, Tanger, Maroc"
        settings.address_en = "Avenue Ibn Tachfine, Ibn Battouta offices, Tanger, Morocco"
        settings.address_ar = "Ø´Ø§Ø±Ø¹ Ø§Ø¨Ù† ØªØ§Ø´ÙÙŠÙ†ØŒ Ù…ÙƒØ§ØªØ¨ Ø§Ø¨Ù† Ø¨Ø·ÙˆØ·Ø©ØŒ Ø·Ù†Ø¬Ø©ØŒ Ø§Ù„Ù…ØºØ±Ø¨"
        settings.save()
        self.stdout.write(self.style.SUCCESS('  âœ“ Hero settings seeded'))

        # 2. Seed StrategicSuccess
        self.stdout.write('\nâ€” Seeding Strategic Success Examples â€”')

        for item in STRATEGIC_EXAMPLES:
            slug = item['slug']
            filename = f"{slug}.jpg"
            existing = StrategicSuccess.objects.filter(title_fr=item['title_fr']).first()

            if existing and not force:
                self.stdout.write(f'  â€¢ "{item["title_fr"]}" already exists â€” skipping (use --force to overwrite)')
                continue

            obj = existing or StrategicSuccess()
            obj.title_fr = item['title_fr']
            obj.title_en = item['title_en']
            obj.title_ar = item['title_ar']
            obj.importance_fr = item['importance_fr']
            obj.importance_en = item['importance_en']
            obj.importance_ar = item['importance_ar']
            obj.icon = item['icon']
            obj.order = item['order']
            obj.is_active = True

            # Create placeholder JPEG file if none exists
            if not obj.image:
                obj.image = ContentFile(TINY_JPEG, name=filename)

            obj.save()
            self.stdout.write(self.style.SUCCESS(f'  âœ“ Saved: {obj.title_fr}'))

        self.stdout.write(self.style.SUCCESS('\nâœ… Homepage data seeded successfully!'))

