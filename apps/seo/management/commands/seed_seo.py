"""
Management command to seed initial SEO data with locally-relevant keywords
for Tangier/Morocco VR real estate audience.

Keyword Strategy per Page:
=========================
- home:       Brand + core services + location (Tanger/Tangier)
- services:   Service types + real estate + 3D/VR technology + location
- portfolio:  Project types + results + location
- about:      Company identity + expertise + location
- contact:    Lead-intent keywords + quote requests + location
- blog:       Content/industry keywords + location
- promotions: Pack/offer keywords + promoter-specific terms
"""
from django.core.management.base import BaseCommand
from apps.seo.models import PageSEO


SEO_DATA = [
    {
        'page_identifier': 'home',
        'meta_title_fr': 'VR Creation — Modélisation 3D & Visites Virtuelles à Tanger',
        'meta_title_en': 'VR Creation — 3D Modeling & Virtual Tours in Tangier',
        'meta_title_ar': 'في آر كرييشن — نمذجة ثلاثية الأبعاد وجولات افتراضية في طنجة',
        'meta_description_fr': 'VR Creation Company à Tanger : modélisation 3D, visites virtuelles 360°, branding et marketing digital pour promoteurs immobiliers au Maroc.',
        'meta_description_en': 'VR Creation Company in Tangier: 3D modeling, 360° virtual tours, branding and digital marketing for real estate developers in Morocco.',
        'meta_description_ar': 'شركة في آر كرييشن في طنجة: نمذجة ثلاثية الأبعاد، جولات افتراضية 360°، هوية بصرية وتسويق رقمي للمطورين العقاريين في المغرب.',
        'keywords_fr': 'modélisation 3D Tanger, visite virtuelle immobilier Maroc, VR Creation Tangier, rendu 3D promoteur immobilier, réalité virtuelle Tanger, marketing immobilier Maroc',
        'keywords_en': '3D modeling Tangier, virtual tour Morocco real estate, VR Creation Tangier, 3D rendering real estate, virtual reality Morocco, real estate marketing Tangier',
        'keywords_ar': 'نمذجة ثلاثية الأبعاد طنجة, جولة افتراضية عقارات المغرب, واقع افتراضي طنجة, تسويق عقاري المغرب',
    },
    {
        'page_identifier': 'services',
        'meta_title_fr': 'Nos Services — Rendu 3D, Visite Virtuelle 360°, Branding à Tanger',
        'meta_title_en': 'Our Services — 3D Rendering, 360° Virtual Tour, Branding in Tangier',
        'meta_title_ar': 'خدماتنا — عرض ثلاثي الأبعاد، جولة افتراضية 360°، هوية بصرية في طنجة',
        'meta_description_fr': "Découvrez nos services : modélisation 3D, visites virtuelles 360°, captures drone, branding visuel, site web et lead generation pour l'immobilier à Tanger.",
        'meta_description_en': 'Discover our services: 3D modeling, 360° virtual tours, drone captures, visual branding, websites and lead generation for real estate in Tangier.',
        'meta_description_ar': 'اكتشف خدماتنا: نمذجة ثلاثية الأبعاد، جولات افتراضية 360°، تصوير بالطائرات، هوية بصرية، مواقع إلكترونية في طنجة.',
        'keywords_fr': 'rendu 3D immobilier Tanger, visite virtuelle 360 Maroc, capture 360 Tanger, branding promoteur immobilier, site web immobilier Maroc, lead generation immobilier',
        'keywords_en': '3D rendering real estate Tangier, 360 virtual tour Morocco, drone capture Tangier, real estate branding, property website Morocco, lead generation real estate',
        'keywords_ar': 'عرض ثلاثي الأبعاد عقارات طنجة, جولة افتراضية 360 المغرب, تصوير جوي طنجة, هوية بصرية مطور عقاري',
    },
    {
        'page_identifier': 'portfolio',
        'meta_title_fr': 'Portfolio — Projets 3D & Visites Virtuelles Immobilières | Tanger',
        'meta_title_en': 'Portfolio — 3D Projects & Real Estate Virtual Tours | Tangier',
        'meta_title_ar': 'معرض الأعمال — مشاريع ثلاثية الأبعاد وجولات افتراضية عقارية | طنجة',
        'meta_description_fr': 'Explorez nos réalisations : rendus 3D photoréalistes, visites virtuelles immersives et campagnes digitales pour promoteurs immobiliers à Tanger et au Maroc.',
        'meta_description_en': 'Explore our work: photorealistic 3D renders, immersive virtual tours and digital campaigns for real estate developers in Tangier and Morocco.',
        'meta_description_ar': 'استكشف أعمالنا: عروض ثلاثية الأبعاد واقعية، جولات افتراضية غامرة وحملات رقمية للمطورين العقاريين في طنجة والمغرب.',
        'keywords_fr': 'projets 3D immobilier Tanger, réalisations visite virtuelle Maroc, portfolio rendu 3D, exemples visite virtuelle promoteur',
        'keywords_en': '3D real estate projects Tangier, virtual tour portfolio Morocco, 3D rendering examples, property virtual tour showcase',
        'keywords_ar': 'مشاريع ثلاثية الأبعاد عقارات طنجة, معرض جولات افتراضية المغرب',
    },
    {
        'page_identifier': 'about',
        'meta_title_fr': 'À Propos — VR Creation Company, Agence 3D à Tanger',
        'meta_title_en': 'About Us — VR Creation Company, 3D Agency in Tangier',
        'meta_title_ar': 'من نحن — في آر كرييشن، وكالة ثلاثية الأبعاد في طنجة',
        'meta_description_fr': 'VR Creation est une agence spécialisée en modélisation 3D et réalité virtuelle à Tanger, au service des promoteurs immobiliers au Maroc.',
        'meta_description_en': 'VR Creation is an agency specializing in 3D modeling and virtual reality in Tangier, serving real estate developers in Morocco.',
        'meta_description_ar': 'في آر كرييشن وكالة متخصصة في النمذجة ثلاثية الأبعاد والواقع الافتراضي في طنجة، تخدم المطورين العقاريين في المغرب.',
        'keywords_fr': 'agence 3D Tanger, entreprise réalité virtuelle Maroc, VR Creation company, équipe modélisation 3D Tanger',
        'keywords_en': '3D agency Tangier, virtual reality company Morocco, VR Creation company, 3D modeling team Tangier',
        'keywords_ar': 'وكالة ثلاثية الأبعاد طنجة, شركة واقع افتراضي المغرب, فريق نمذجة ثلاثية الأبعاد',
    },
    {
        'page_identifier': 'contact',
        'meta_title_fr': 'Contact — Devis Gratuit Modélisation 3D & Visite Virtuelle | Tanger',
        'meta_title_en': 'Contact — Free Quote 3D Modeling & Virtual Tour | Tangier',
        'meta_title_ar': 'اتصل بنا — عرض أسعار مجاني نمذجة ثلاثية الأبعاد وجولة افتراضية | طنجة',
        'meta_description_fr': 'Demandez un devis gratuit pour vos projets de modélisation 3D, visites virtuelles et marketing immobilier à Tanger. Réponse sous 24h.',
        'meta_description_en': 'Request a free quote for your 3D modeling, virtual tour and real estate marketing projects in Tangier. Response within 24h.',
        'meta_description_ar': 'اطلب عرض أسعار مجاني لمشاريعك في النمذجة ثلاثية الأبعاد والجولات الافتراضية والتسويق العقاري في طنجة. رد خلال 24 ساعة.',
        'keywords_fr': 'devis modélisation 3D Tanger, contact agence VR Maroc, prix visite virtuelle immobilier, devis rendu 3D promoteur',
        'keywords_en': '3D modeling quote Tangier, contact VR agency Morocco, virtual tour pricing, 3D rendering quote real estate',
        'keywords_ar': 'عرض أسعار نمذجة ثلاثية الأبعاد طنجة, اتصال وكالة واقع افتراضي المغرب',
    },
    {
        'page_identifier': 'blog',
        'meta_title_fr': 'Blog — Actualités 3D, VR & Marketing Immobilier | VR Creation',
        'meta_title_en': 'Blog — 3D, VR & Real Estate Marketing News | VR Creation',
        'meta_title_ar': 'المدونة — أخبار ثلاثية الأبعاد والواقع الافتراضي والتسويق العقاري | في آر كرييشن',
        'meta_description_fr': "Articles et conseils sur la modélisation 3D, les visites virtuelles et le marketing digital pour l'immobilier à Tanger et au Maroc.",
        'meta_description_en': 'Articles and tips on 3D modeling, virtual tours and digital marketing for real estate in Tangier and Morocco.',
        'meta_description_ar': 'مقالات ونصائح حول النمذجة ثلاثية الأبعاد والجولات الافتراضية والتسويق الرقمي للعقارات في طنجة والمغرب.',
        'keywords_fr': 'actualités immobilier 3D Maroc, blog réalité virtuelle Tanger, conseils marketing immobilier, tendances visite virtuelle',
        'keywords_en': '3D real estate news Morocco, virtual reality blog Tangier, real estate marketing tips, virtual tour trends',
        'keywords_ar': 'أخبار عقارات ثلاثية الأبعاد المغرب, مدونة واقع افتراضي طنجة',
    },
    {
        'page_identifier': 'promotions',
        'meta_title_fr': 'Nos Offres & Packs — Solutions Marketing Immobilier | Tanger',
        'meta_title_en': 'Our Offers & Packs — Real Estate Marketing Solutions | Tangier',
        'meta_title_ar': 'عروضنا وباقاتنا — حلول تسويق عقاري | طنجة',
        'meta_description_fr': 'Découvrez nos packs marketing pour promoteurs immobiliers à Tanger : 3D, visites virtuelles, branding, site web et gestion commerciale. Offre sur commission disponible.',
        'meta_description_en': 'Discover our marketing packs for real estate developers in Tangier: 3D, virtual tours, branding, websites and sales management. Commission-based offer available.',
        'meta_description_ar': 'اكتشف باقاتنا التسويقية للمطورين العقاريين في طنجة: ثلاثي الأبعاد، جولات افتراضية، هوية بصرية، مواقع إلكترونية. عرض بالعمولة متاح.',
        'keywords_fr': 'pack promoteur immobilier Tanger, offre visite virtuelle Maroc, marketing immobilier commission, solution 3D promoteur Tanger',
        'keywords_en': 'real estate developer pack Tangier, virtual tour offer Morocco, commission marketing real estate, 3D solution promoter Tangier',
        'keywords_ar': 'باقة مطور عقاري طنجة, عرض جولة افتراضية المغرب, تسويق عقاري بالعمولة',
    },
]


class Command(BaseCommand):
    help = 'Seed SEO data with Tangier/Morocco-relevant keywords for all major pages.'

    def handle(self, *args, **options):
        created_count = 0
        updated_count = 0

        for entry in SEO_DATA:
            page_id = entry.pop('page_identifier')
            obj, created = PageSEO.objects.update_or_create(
                page_identifier=page_id,
                defaults=entry,
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
