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
        'title_fr': 'Magasin ou concept-store',
        'title_en': 'Store or concept-store',
        'title_ar': 'متجر أو كونسبت ستور',
        'importance_fr': 'Attirer les clients dès la phase de pré-lancement.',
        'importance_en': 'Attract customers from the pre-launch phase.',
        'importance_ar': 'جذب العملاء منذ مرحلة ما قبل الإطلاق.',
        'slug': 'magasin-concept-store',
        'icon': 'fas fa-store',
        'order': 1,
    },
    {
        'title_fr': 'Événementiel',
        'title_en': 'Events',
        'title_ar': 'فعاليات',
        'importance_fr': 'Séduire et engager un public exigeant.',
        'importance_en': 'Attract and engage a demanding audience.',
        'importance_ar': 'جذب وإشراك جمهور متطلب.',
        'slug': 'evenementiel',
        'icon': 'fas fa-calendar-star',
        'order': 2,
    },
    {
        'title_fr': 'Projet immobilier',
        'title_en': 'Real estate project',
        'title_ar': 'مشروع عقاري',
        'importance_fr': 'Les acheteurs veulent se projeter avant d\'investir.',
        'importance_en': 'Buyers want to envision before investing.',
        'importance_ar': 'يريد المشترون التصور قبل الاستثمار.',
        'slug': 'projet-immobilier',
        'icon': 'fas fa-building',
        'order': 3,
    },
    {
        'title_fr': 'Villa en construction',
        'title_en': 'Villa under construction',
        'title_ar': 'فيلا قيد البناء',
        'importance_fr': 'Le client veut visualiser le résultat final pour s\'engager.',
        'importance_en': 'The client wants to visualize the final result before committing.',
        'importance_ar': 'يريد العميل تصور النتيجة النهائية قبل الالتزام.',
        'slug': 'villa-en-construction',
        'icon': 'fas fa-home',
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
        settings.hero_headline_fr = "Donnez vie à votre projet immobilier avant même sa construction — Modélisation 3D & Visites Virtuelles à Tanger"
        settings.hero_headline_en = "Bring your real estate project to life before it's even built — 3D Modeling & Virtual Tours in Tangier"
        settings.hero_headline_ar = "امنح مشروعك العقاري الحياة قبل حتى بنائه — نمذجة ثلاثية الأبعاد وجولات افتراضية في طنجة"
        settings.hero_subheadline_fr = "De la conception 3D à la commercialisation digitale, nous transformons vos projets immobiliers en expériences visuelles capables de séduire, convaincre et générer des prospects."
        settings.hero_subheadline_en = "From 3D design to digital marketing, we transform your real estate projects into visual experiences that attract, convince and generate leads."
        settings.hero_subheadline_ar = "من التصميم ثلاثي الأبعاد إلى التسويق الرقمي، نحول مشاريعكم العقارية إلى تجارب بصرية قادرة على جذب وإقناع وتوليد العملاء المحتملين."
        settings.hero_cta1_label_fr = "Découvrir nos services"
        settings.hero_cta1_label_en = "Discover our services"
        settings.hero_cta1_label_ar = "اكتشف خدماتنا"
        settings.hero_cta1_link = "#services"
        settings.hero_cta2_label_fr = "Nous contacter"
        settings.hero_cta2_label_en = "Contact us"
        settings.hero_cta2_label_ar = "اتصل بنا"
        settings.hero_cta2_link = "/contact/"
        settings.phone = "+212634017762"
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
