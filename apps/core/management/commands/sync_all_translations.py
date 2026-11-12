"""
Management command to sync and populate all missing EN and AR database translations
for Services, ServiceImages, ProjectImages, and SiteSettings.
Run via: python manage.py sync_all_translations
"""
from django.core.management.base import BaseCommand
from apps.core.models import SiteSettings
from apps.services.models import Service, ServiceImage
from apps.portfolio.models import ProjectImage


class Command(BaseCommand):
    help = "Populate missing EN and AR translations for database models"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Syncing database model translations..."))

        # 1. SiteSettings address_en (fix Tangier -> Tanger)
        s = SiteSettings.objects.first()
        if s:
            if "Tangier" in (s.address_en or ""):
                s.address_en = s.address_en.replace("Tangier", "Tanger")
                s.save(update_fields=['address_en'])
                self.stdout.write(self.style.SUCCESS("✓ Fixed SiteSettings address_en: Tangier -> Tanger"))

        # 2. Services missing full_description_ar / en
        try:
            s_web = Service.objects.filter(slug_fr='site-web-experience-digitale').first()
            if not s_web:
                s_web = Service.objects.filter(title_fr__icontains='Site Web').first()
            if s_web:
                s_web.full_description_ar = "نصمم منصات عقارية حديثة تدمج عروض العقارات، الجولات الافتراضية التفاعلية، الاستمارات الذكية، وتوليد العملاء المحتملين المؤهلين."
                s_web.save(update_fields=['full_description_ar'])
                self.stdout.write(self.style.SUCCESS(f"✓ Updated AR description for service: {s_web.title_fr}"))
        except Exception as e:
            self.stdout.write(self.style.WARNING(f"Service Web update error: {e}"))

        try:
            s_mkt = Service.objects.filter(slug_fr='marketing-digital-lead-generation').first()
            if not s_mkt:
                s_mkt = Service.objects.filter(title_fr__icontains='Marketing digital').first()
            if s_mkt:
                s_mkt.full_description_ar = """<p class="mb-4">ترافق VR Creation المطورين العقاريين والشركات في إعداد منظومات استقطاب عملاء محتملين عالية الجودة. بفضل التكامل بين تصاميمنا ثلاثية الأبعاد الاستثنائية واستراتيجيات الإعلانات الموجهة، نحول اهتمام الزوار إلى مواعيد تجارية ملموسة.</p>
<h3 class="text-xl font-bold text-dark mt-6 mb-3">ما تتضمنه هذه الخدمة:</h3>
<ul class="list-disc list-inside space-y-2 mb-6 text-gray-600">
    <li><strong>إنشاء صفحات هبوط تفاعلية:</strong> صفحات تحويل محسّنة تتضمن تصاميم ثلاثية الأبعاد، جولات افتراضية واستمارات تفاعلية.</li>
    <li><strong>حملات إعلانية مستهدفة:</strong> إعلانات ممولة على ميتا (إنستغرام، فيسبوك)، إعلانات جوجل، ولينكد إن تستهدف المشترين المحليين ومغاربة العالم.</li>
    <li><strong>تأهيل ومتابعة العملاء المحتملين:</strong> فرز مسبق للطلبات ومزامنة مباشرة مع فريقكم التجاري أو نظام إدارة علاقات العملاء (CRM).</li>
    <li><strong>تقارير وتحسين مستمر:</strong> لوحات تحكم فورية لقياس تكلفة كل عميل محتمل وتعظيم العائد على الاستثمار.</li>
</ul>"""
                s_mkt.full_description_en = """<p class="mb-4">VR Creation supports real estate developers and companies in implementing high-quality lead acquisition systems. Through synergy between our exceptional 3D visuals and targeted media strategies, we transform visitor interest into concrete sales appointments.</p>
<h3 class="text-xl font-bold text-dark mt-6 mb-3">What this service includes:</h3>
<ul class="list-disc list-inside space-y-2 mb-6 text-gray-600">
    <li><strong>Immersive landing page creation:</strong> Optimized conversion pages integrating 3D visuals, virtual tours, and interactive forms.</li>
    <li><strong>Targeted advertising campaigns:</strong> Sponsored distribution on Meta (Instagram, Facebook), Google Ads, and LinkedIn targeting domestic buyers and Moroccan expats.</li>
    <li><strong>Lead qualification & follow-up:</strong> Upstream request filtering and direct synchronization with your sales team or CRM.</li>
    <li><strong>Reporting & continuous optimization:</strong> Real-time dashboards to measure cost per lead and maximize return on investment.</li>
</ul>"""
                s_mkt.save(update_fields=['full_description_ar', 'full_description_en'])
                self.stdout.write(self.style.SUCCESS(f"✓ Updated AR/EN description for service: {s_mkt.title_fr}"))
        except Exception as e:
            self.stdout.write(self.style.WARNING(f"Service Marketing update error: {e}"))

        # 3. Image Alt texts translation mapping
        alt_translations = {
            "Modélisation 3D d'Espaces Bureaux Professionnels": (
                "3D Modeling of Professional Office Spaces",
                "نمذجة ثلاثية الأبعاد لمساحات المكاتب المهنية"
            ),
            "Visite virtuelle interactive - Salon & Séjour": (
                "Interactive Virtual Tour - Living Room & Lounge",
                "جولة افتراضية تفاعلية - صالون وغرفة معيشة"
            ),
            "Capture 360° réelle - Espace de réception & Bureau": (
                "Real 360° Capture - Reception Area & Office",
                "تصوير حقيقي 360 درجة - منطقة الاستقبال والمكتب"
            ),
            "Rendu 3D Villa Individuelle Haut de Gamme": (
                "High-End Luxury Villa 3D Rendering",
                "رندر ثلاثي الأبعاد لفيلا فاخرة راقية"
            ),
            "Projection dans l'espace & circulation fluide": (
                "Spatial Projection & Seamless Circulation",
                "تصور للمساحة وحركة سلسة"
            ),
            "Showroom d'exposition interactif de luxe": (
                "Interactive Luxury Exhibition Showroom",
                "صالة عرض تفاعلية فاخرة"
            ),
            "Visualisation 3D Promotion Immobilière / Résidence": (
                "3D Visualization for Real Estate Development / Residence",
                "تصور ثلاثي الأبعاد لمشروع عقاري / مجمع سكني"
            ),
            "Test d'aménagement intérieur & mobilier": (
                "Interior Layout & Furniture Simulation",
                "محاكاة التصميم الداخلي والأثاث"
            ),
            "Espace commercial & retail connecté": (
                "Connected Commercial & Retail Space",
                "مساحة تجارية متصلة للمحلات والمتاجر"
            ),
            "Design 3D Store & Showroom Retail": (
                "3D Store & Retail Showroom Design",
                "تصميم ثلاثي الأبعاد للمتاجر وصالات العرض"
            ),
            "Simulation de luminosité & perspectives réelles": (
                "Lighting Simulation & Realistic Perspectives",
                "محاكاة الإضاءة والزوايا الواقعية"
            ),
            "Visite virtuelle de bureaux d'entreprise": (
                "Corporate Office Virtual Tour",
                "جولة افتراضية لمكاتب الشركات"
            ),
            "Conception 3D Stand Événementiel & Salon": (
                "3D Design for Exhibition & Event Booths",
                "تصميم ثلاثي الأبعاد لأجنحة المعارض والفعاليات"
            ),
            "Visualisation immersive chambre & suite parentale": (
                "Immersive Visualization of Master Bedroom & Suite",
                "تصور غامر لغرفة النوم والجناح الرئيسي"
            ),
            "Immersion complète en agence immobilière": (
                "Complete Immersion in Real Estate Agency",
                "محاكاة غامرة كاملة للوكالة العقارية"
            ),
            "Parcours client immersif & interactif 360°": (
                "360° Immersive & Interactive Customer Journey",
                "مسار عميل غامر وتفاعلي 360 درجة"
            ),
            "Parcours magasin interactif pour e-commerce": (
                "Interactive Store Tour for E-commerce",
                "جولة متجر تفاعلية للتجارة الإلكترونية"
            ),
            "Numérisation 3D d'espace professionnel": (
                "3D Scanning of Professional Space",
                "مسح ثلاثي الأبعاد للمساحات المهنية"
            ),
            "Captation 360° événementielle & salon d'exposition": (
                "360° Event & Exhibition Hall Capture",
                "تصوير 360 درجة للفعاليات وقاعات المعارض"
            ),
            "Villa Méditerranée - Rendu 3D extérieur": (
                "Villa Méditerranée - Exterior 3D Rendering",
                "فيلا البحر الأبيض المتوسط - رندر خارجي ثلاثي الأبعاد"
            ),
            "Résidence Azure - Rendu 3D immeuble moderne": (
                "Résidence Azure - Modern Building 3D Rendering",
                "إقامة أزور - رندر ثلاثي الأبعاد لمبنى حديث"
            ),
            "Concept Store Lumière - Design intérieur & Showroom": (
                "Concept Store Lumière - Interior Design & Showroom",
                "كونسبت ستور لوميير - تصميم داخلي وصالة عرض"
            ),
        }

        updated_si = 0
        for img in ServiceImage.objects.all():
            alt_fr = (img.alt_text_fr or "").strip()
            if alt_fr in alt_translations:
                en_val, ar_val = alt_translations[alt_fr]
                img.alt_text_en = en_val
                img.alt_text_ar = ar_val
                img.save(update_fields=['alt_text_en', 'alt_text_ar'])
                updated_si += 1
        self.stdout.write(self.style.SUCCESS(f"✓ Updated {updated_si} ServiceImage alt texts."))

        updated_pi = 0
        for img in ProjectImage.objects.all():
            alt_fr = (img.alt_text_fr or "").strip()
            if alt_fr in alt_translations:
                en_val, ar_val = alt_translations[alt_fr]
                img.alt_text_en = en_val
                img.alt_text_ar = ar_val
                img.save(update_fields=['alt_text_en', 'alt_text_ar'])
                updated_pi += 1
        self.stdout.write(self.style.SUCCESS(f"✓ Updated {updated_pi} ProjectImage alt texts."))

        self.stdout.write(self.style.SUCCESS("All model translations synced successfully!"))
