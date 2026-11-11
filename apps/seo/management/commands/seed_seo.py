"""
Management command to seed initial SEO data with locally-relevant keywords
for Tangier/Morocco VR real estate audience.
All titles ≤ 60 chars, all descriptions ≤ 155 chars, keyword first, zero emojis.
"""
from django.core.management.base import BaseCommand
from apps.seo.models import PageSEO


SEO_DATA = [
    {
        'page_identifier': 'home',
        'meta_title_fr': 'Modélisation 3D & visites 360° à Tanger',
        'meta_title_en': '3D Modeling & Virtual Tours in Tangier',
        'meta_title_ar': 'نمذجة ثلاثية الأبعاد وجولات افتراضية بطنجة',
        'meta_description_fr': 'Agence 3D à Tanger : modélisation 3D, visites virtuelles 360°, drone et marketing immobilier au Maroc. Devis gratuit et accompagnement dédié.',
        'meta_description_en': 'Tangier 3D studio: 3D modeling, 360° virtual tours, drone capture and real estate marketing in Morocco. Free quote & dedicated support.',
        'meta_description_ar': 'استوديو ثلاثي الأبعاد بطنجة: نمذجة ثلاثية الأبعاد، جولات افتراضية 360°، تصوير جوي وتسويق عقاري بالمغرب. عرض أسعار مجاني.',
        'keywords_fr': 'modélisation 3D Tanger, visite virtuelle immobilier Maroc, rendu 3D promoteur, réalité virtuelle Tanger',
        'keywords_en': '3D modeling Tangier, virtual tour Morocco, 3D rendering real estate, virtual reality Tangier',
        'keywords_ar': 'نمذجة ثلاثية الأبعاد طنجة, جولة افتراضية عقارات المغرب, واقع افتراضي طنجة',
    },
    {
        'page_identifier': 'services',
        'meta_title_fr': 'Services 3D, visite virtuelle & branding',
        'meta_title_en': '3D Services, Virtual Tour & Branding',
        'meta_title_ar': 'خدمات ثلاثية الأبعاد وجولات افتراضية بطنجة',
        'meta_description_fr': 'Découvrez nos solutions 3D à Tanger : modélisation 3D, visites 360°, photographie drone, branding et lead generation pour promoteurs immobiliers.',
        'meta_description_en': 'Explore our 3D solutions in Tangier: 3D modeling, 360 tours, drone photography, visual branding and lead generation for property developers.',
        'meta_description_ar': 'اكتشف حلولنا ثلاثية الأبعاد بطنجة: نمذجة 3D، جولات 360، تصوير درون، هوية بصرية وجلب عملاء للمطورين العقاريين.',
        'keywords_fr': 'rendu 3D immobilier Tanger, visite virtuelle 360 Maroc, capture 360 Tanger, branding promoteur immobilier',
        'keywords_en': '3D rendering Tangier, 360 virtual tour Morocco, drone capture Tangier, real estate branding',
        'keywords_ar': 'عرض ثلاثي الأبعاد عقارات طنجة, جولة افتراضية 360 المغرب, تصوير جوي طنجة',
    },
    {
        'page_identifier': 'portfolio',
        'meta_title_fr': 'Réalisations 3D & visites immersives Tanger',
        'meta_title_en': '3D Projects & Virtual Tours Tangier',
        'meta_title_ar': 'مشاريع ثلاثية الأبعاد وجولات غامرة طنجة',
        'meta_description_fr': 'Explorez nos rendus 3D photoréalistes, visites virtuelles immersives et vidéos d’architecture pour promoteurs à Tanger et au Maroc.',
        'meta_description_en': 'Explore our photorealistic 3D renders, immersive virtual tours and architectural videos for property developers in Tangier and Morocco.',
        'meta_description_ar': 'استكشف عروضنا الواقعية ثلاثية الأبعاد وجولاتنا الافتراضية الغامرة للمطورين العقاريين في طنجة والمغرب.',
        'keywords_fr': 'projets 3D immobilier Tanger, réalisations visite virtuelle Maroc, portfolio rendu 3D Tanger',
        'keywords_en': '3D real estate projects Tangier, virtual tour portfolio Morocco, 3D architectural renders',
        'keywords_ar': 'مشاريع ثلاثية الأبعاد عقارات طنجة, معرض جولات افتراضية المغرب',
    },
    {
        'page_identifier': 'about',
        'meta_title_fr': 'Agence 3D & réalité virtuelle à Tanger',
        'meta_title_en': '3D Agency & Virtual Reality in Tangier',
        'meta_title_ar': 'وكالة ثلاثية الأبعاد وواقع افتراضي بطنجة',
        'meta_description_fr': 'VR Creation est le studio de modélisation 3D et de production visuelle haut de gamme à Tanger, dédié aux promoteurs et architectes.',
        'meta_description_en': 'VR Creation is the premium 3D modeling and visual production agency in Tangier, dedicated to architects and real estate developers.',
        'meta_description_ar': 'في آر كرييشن هي الوكالة الرائدة في النمذجة ثلاثية الأبعاد والإنتاج البصري بطنجة لخدمة المهندسين والمطورين العقاريين.',
        'keywords_fr': 'agence 3D Tanger, entreprise réalité virtuelle Maroc, VR Creation Tanger, studio modélisation 3D',
        'keywords_en': '3D agency Tangier, virtual reality company Morocco, VR Creation Tangier, 3D modeling studio',
        'keywords_ar': 'وكالة ثلاثية الأبعاد طنجة, شركة واقع افتراضي المغرب',
    },
    {
        'page_identifier': 'contact',
        'meta_title_fr': 'Contact & devis gratuit à Tanger',
        'meta_title_en': 'Contact & Free Quote in Tangier',
        'meta_title_ar': 'اتصل بنا وعرض أسعار مجاني بطنجة',
        'meta_description_fr': 'Demandez votre devis gratuit sous 24h pour vos projets 3D, visites virtuelles et supports visuels à Tanger. Équipe à votre écoute.',
        'meta_description_en': 'Request your free quote within 24h for 3D renderings, virtual tours and visual assets in Tangier. Dedicated team at your service.',
        'meta_description_ar': 'اطلب عرض أسعار مجاني خلال 24 ساعة لمشاريعك ثلاثية الأبعاد والجولات الافتراضية بطنجة. فريقنا في خدمتكم.',
        'keywords_fr': 'devis modélisation 3D Tanger, contact agence VR Maroc, prix visite virtuelle immobilier',
        'keywords_en': '3D modeling quote Tangier, contact VR agency Morocco, virtual tour price Morocco',
        'keywords_ar': 'عرض أسعار نمذجة ثلاثية الأبعاد طنجة, اتصال وكالة واقع افتراضي',
    },
    {
        'page_identifier': 'blog',
        'meta_title_fr': 'Blog 3D, visite virtuelle & immobilier',
        'meta_title_en': '3D, Virtual Tour & Real Estate Blog',
        'meta_title_ar': 'مدونة ثلاثي الأبعاد والواقع الافتراضي',
        'meta_description_fr': 'Conseils pratiques, tendances 3D, visites virtuelles et stratégies de commercialisation immobilière à Tanger et au Maroc.',
        'meta_description_en': 'Practical advice, 3D trends, virtual tours and property marketing strategies in Tangier and Morocco.',
        'meta_description_ar': 'نصائح عملية واتجاهات النمذجة ثلاثية الأبعاد والجولات الافتراضية والتسويق العقاري في طنجة والمغرب.',
        'keywords_fr': 'actualités immobilier 3D Maroc, blog réalité virtuelle Tanger, conseils marketing immobilier',
        'keywords_en': '3D real estate news Morocco, virtual reality blog Tangier, real estate marketing tips',
        'keywords_ar': 'أخبار عقارات ثلاثية الأبعاد المغرب, مدونة واقع افتراضي طنجة',
    },
    {
        'page_identifier': 'promotions',
        'meta_title_fr': 'Packs marketing promoteur immobilier',
        'meta_title_en': 'Real Estate Marketing Packs Tangier',
        'meta_title_ar': 'باقات تسويق للمطورين العقاريين',
        'meta_description_fr': 'Packs marketing tout-en-un pour promoteurs immobiliers à Tanger : 3D, visites virtuelles, branding et vente sur commission.',
        'meta_description_en': 'All-in-one marketing packs for property developers in Tangier: 3D, virtual tours, branding and commission-based sales.',
        'meta_description_ar': 'باقات تسويقية شاملة للمطورين العقاريين في طنجة: 3D، جولات افتراضية، هوية بصرية وعروض بالعمولة.',
        'keywords_fr': 'pack promoteur immobilier Tanger, offre visite virtuelle Maroc, marketing immobilier commission',
        'keywords_en': 'real estate developer pack Tangier, virtual tour offer Morocco, property marketing package',
        'keywords_ar': 'باقة مطور عقاري طنجة, عرض جولة افتراضية المغرب',
    },
    {
        'page_identifier': 'virtual_tours',
        'meta_title_fr': 'Visites 360° & visites virtuelles Tanger',
        'meta_title_en': '360° Virtual Tours Showcase in Tangier',
        'meta_title_ar': 'جولات افتراضية 360 درجة في طنجة',
        'meta_description_fr': 'Découvrez nos visites virtuelles 360° immersives pour l\'immobilier, showrooms et commerces à Tanger. Expérience interactive haut de gamme.',
        'meta_description_en': 'Explore our immersive 360° virtual tours for real estate, showrooms and shops in Tangier. High-end interactive experience.',
        'meta_description_ar': 'اكتشف جولاتنا الافتراضية 360° الغامرة للعقارات والمعارض والمحلات التجارية في طنجة. تجربة تفاعلية متميزة.',
        'keywords_fr': 'visite virtuelle 360 Tanger, visite 360 immobilier Maroc, showroom virtuel Tanger',
        'keywords_en': '360 virtual tour Tangier, property virtual tour Morocco, virtual showroom Tangier',
        'keywords_ar': 'جولة افتراضية 360 طنجة, جولة عقارية افتراضية المغرب',
    },
    {
        'page_identifier': 'case_studies',
        'meta_title_fr': 'Études de cas & résultats 3D à Tanger',
        'meta_title_en': 'Case Studies & 3D Results in Tangier',
        'meta_title_ar': 'دراسات الحالة ونتائج المشاريع في طنجة',
        'meta_description_fr': 'Découvrez comment nos visuels 3D et visites virtuelles ont boosté les ventes de nos clients promoteurs immobiliers à Tanger.',
        'meta_description_en': 'Discover how our 3D renderings and virtual tours boosted property sales for real estate developers in Tangier.',
        'meta_description_ar': 'اكتشف كيف ساهمت عروضنا ثلاثية الأبعاد وجولاتنا الافتراضية في تسريع مبيعات المطورين العقاريين في طنجة.',
        'keywords_fr': 'études de cas 3D Tanger, ROI visite virtuelle immobilier, succès marketing immobilier Maroc',
        'keywords_en': '3D case studies Tangier, virtual tour ROI real estate, property marketing success Morocco',
        'keywords_ar': 'دراسات حالة ثلاثية الأبعاد طنجة, عائد الاستثمار جولة افتراضية',
    },
    {
        'page_identifier': 'sitemap',
        'meta_title_fr': 'Plan du site & architecture de navigation',
        'meta_title_en': 'HTML Sitemap & Navigation Index',
        'meta_title_ar': 'خريطة الموقع وهيكل التصفح',
        'meta_description_fr': 'Consultez le plan du site VR Creation à Tanger : accès direct à tous nos services 3D, visites virtuelles, projets et articles.',
        'meta_description_en': 'Explore the VR Creation sitemap in Tangier: direct access to all our 3D services, virtual tours, portfolio and articles.',
        'meta_description_ar': 'تصفح خريطة موقع في آر كرييشن بطنجة: وصول مباشر لجميع خدماتنا ثلاثية الأبعاد وجولاتنا ومشاريعنا ومقالاتنا.',
        'keywords_fr': 'plan du site VR Creation, architecture site 3D Tanger',
        'keywords_en': 'sitemap VR Creation, navigation index Tangier',
        'keywords_ar': 'خريطة الموقع في آر كرييشن طنجة',
    },
]


class Command(BaseCommand):
    help = 'Seed SEO data with strict character limits (title ≤ 60, desc ≤ 155) for all major pages.'

    def handle(self, *args, **options):
        created_count = 0
        updated_count = 0

        for item in SEO_DATA:
            page_id = item['page_identifier']
            defaults = {k: v for k, v in item.items() if k != 'page_identifier'}
            obj, created = PageSEO.objects.update_or_create(
                page_identifier=page_id,
                defaults=defaults,
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'  + Created SEO: {page_id}'))
            else:
                updated_count += 1
                self.stdout.write(self.style.WARNING(f'  ~ Updated SEO: {page_id}'))

        self.stdout.write(self.style.SUCCESS(
            f'\nDone! {created_count} created, {updated_count} updated.'
        ))
