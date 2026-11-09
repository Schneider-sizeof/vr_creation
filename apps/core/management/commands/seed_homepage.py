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
        'title_ar': 'شركة ومشروع ناشئ',
        'importance_fr': 'Construire une image de marque forte pour se lancer avec impact.',
        'importance_en': 'Build a strong brand image to launch with impact.',
        'importance_ar': 'بناء صورة علامة تجارية قوية للانطلاق بتأثير.',
        'slug': 'entreprise-startup',
        'icon': 'fas fa-briefcase',
        'order': 1,
    },
    {
        'title_fr': 'Restaurant & commerce',
        'title_en': 'Restaurant & retail',
        'title_ar': 'مطعم وتجارة',
        'importance_fr': 'Attirer les clients avec un visuel professionnel et engageant.',
        'importance_en': 'Attract customers with professional and engaging visuals.',
        'importance_ar': 'جذب العملاء بمرئيات احترافية وجذابة.',
        'slug': 'restaurant-commerce',
        'icon': 'fas fa-store',
        'order': 2,
    },
    {
        'title_fr': 'Professionnel & freelance',
        'title_en': 'Professional & freelancer',
        'title_ar': 'مهني ومستقل',
        'importance_fr': 'Se démarquer avec un portfolio et une présence digitale unique.',
        'importance_en': 'Stand out with a unique portfolio and digital presence.',
        'importance_ar': 'التميز بملف أعمال وحضور رقمي فريد.',
        'slug': 'professionnel-freelance',
        'icon': 'fas fa-user-tie',
        'order': 3,
    },
    {
        'title_fr': 'Événementiel & salons',
        'title_en': 'Events & exhibitions',
        'title_ar': 'فعاليات ومعارض',
        'importance_fr': 'Captiver votre audience avec des visuels et vidéos percutants.',
        'importance_en': 'Captivate your audience with striking visuals and videos.',
        'importance_ar': 'إبهار الجمهور بمرئيات وفيديوهات مؤثرة.',
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
        self.stdout.write('\n— Seeding hero settings —')
        settings = SiteSettings.load()
        settings.hero_headline_fr = "Création visuelle professionnelle à Tanger — Photo, Vidéo, Branding & Web"
        settings.hero_headline_en = "Professional visual creation in Tangier — Photo, Video, Branding & Web"
        settings.hero_headline_ar = "إبداع بصري احترافي في طنجة — تصوير، فيديو، براندينغ وويب"
        settings.hero_subheadline_fr = "Nous accompagnons les entreprises de Tanger et du Nord du Maroc avec des solutions créatives sur mesure : photographie, vidéo, branding et développement web."
        settings.hero_subheadline_en = "We support businesses in Tangier and Northern Morocco with tailored creative solutions: photography, video, branding and web development."
        settings.hero_subheadline_ar = "نرافق الشركات في طنجة وشمال المغرب بحلول إبداعية مخصصة: تصوير، فيديو، براندينغ وتطوير ويب."
        settings.hero_cta1_label_fr = "Découvrir nos services"
        settings.hero_cta1_label_en = "Discover our services"
        settings.hero_cta1_label_ar = "اكتشف خدماتنا"
        settings.hero_cta1_link = "#services"
        settings.hero_cta2_label_fr = "Nous contacter"
        settings.hero_cta2_label_en = "Contact us"
        settings.hero_cta2_label_ar = "اتصل بنا"
        settings.hero_cta2_link = "/contact/"
        settings.phone = "+212 625 07 1498"
        settings.address_fr = "Avenue Ibn Tachfine, bureaux Ibn Battouta, Tanger, Maroc"
        settings.address_en = "Avenue Ibn Tachfine, Ibn Battouta offices, Tangier, Morocco"
        settings.address_ar = "شارع ابن تاشفين، مكاتب ابن بطوطة، طنجة، المغرب"
        settings.save()
        self.stdout.write(self.style.SUCCESS('  ✓ Hero settings seeded'))

        # 2. Seed StrategicSuccess
        self.stdout.write('\n— Seeding Strategic Success Examples —')

        for item in STRATEGIC_EXAMPLES:
            slug = item['slug']
            filename = f"{slug}.jpg"
            existing = StrategicSuccess.objects.filter(title_fr=item['title_fr']).first()

            if existing and not force:
                self.stdout.write(f'  • "{item["title_fr"]}" already exists — skipping (use --force to overwrite)')
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
            self.stdout.write(self.style.SUCCESS(f'  ✓ Saved: {obj.title_fr}'))

        self.stdout.write(self.style.SUCCESS('\n✅ Homepage data seeded successfully!'))
