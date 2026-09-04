from django.db import migrations

def update_site_settings_and_services(apps, schema_editor):
    SiteSettings = apps.get_model('core', 'SiteSettings')
    Service = apps.get_model('services', 'Service')

    # 1. Update SiteSettings
    s = SiteSettings.objects.first()
    if s:
        s.site_name_fr = "VR Creation Company"
        s.site_name_en = "VR Creation Company"
        s.site_name_ar = "في آر كرييشن"

        s.tagline_fr = "L'innovation en action"
        s.tagline_en = "Innovation in Action"
        s.tagline_ar = "الابتكار في العمل"

        s.hero_headline_fr = "Donnez vie à votre projet immobilier avant même sa construction — Modélisation 3D & Visites Virtuelles à Tanger"
        s.hero_headline_en = "Bring your real estate project to life before it's even built — 3D Modeling & Virtual Tours in Tangier"
        s.hero_headline_ar = "امنح مشروعك العقاري الحياة قبل حتى بنائه — نمذجة ثلاثية الأبعاد وجولات افتراضية في طنجة"

        s.hero_subheadline_fr = "De la conception 3D à la commercialisation digitale, nous transformons vos projets immobiliers en expériences visuelles capables de séduire, convaincre et générer des prospects."
        s.hero_subheadline_en = "From 3D design to digital marketing, we transform your real estate projects into visual experiences capable of seducing, convincing and generating leads."
        s.hero_subheadline_ar = "من التصميم ثلاثي الأبعاد إلى التسويق الرقمي، نحول مشاريعكم العقارية إلى تجارب بصرية قادرة على جذب وإقناع وجلب العملاء المحتملين."

        s.hero_cta1_label_fr = "Découvrir nos solutions"
        s.hero_cta1_label_en = "Discover Our Solutions"
        s.hero_cta1_label_ar = "اكتشف حلولنا"
        s.hero_cta1_link = "#services"

        s.hero_cta2_label_fr = "Nous contacter"
        s.hero_cta2_label_en = "Contact Us"
        s.hero_cta2_label_ar = "اتصل بنا"
        s.hero_cta2_link = "/contact/"

        s.phone = "+212634017762"
        s.email = "Vrcreation.company@gmail.com"
        s.address_fr = "Avenue Ibn Tachfine, bureaux Ibn Battouta, Tanger, Maroc"
        s.address_en = "Avenue Ibn Tachfine, Ibn Battouta offices, Tangier, Morocco"
        s.address_ar = "شارع ابن تاشفين، مكاتب ابن بطوطة، طنجة، المغرب"

        s.footer_text_fr = "VR Creation Company — Agence de modélisation 3D et visites virtuelles à Tanger, Maroc. Nous allions esthétique et technologie de pointe pour transformer vos projets en expériences visuelles immersives et inoubliables."
        s.footer_text_en = "VR Creation Company — 3D modeling and virtual tour agency in Tangier, Morocco. We combine aesthetics and cutting-edge technology to transform your projects into immersive and unforgettable visual experiences."
        s.footer_text_ar = "شركة في آر كرييشن — وكالة متخصصة في النمذجة ثلاثية الأبعاد والجولات الافتراضية في طنجة، المغرب. نجمع بين الجمالية والتكنولوجيا المتطورة لتحويل مشاريعك إلى تجارب بصرية غامرة لا تُنسى."

        s.save()

    # 2. Update Service SEO & Translations
    SERVICES_DATA = {
        'modelisation-3d': {
            'title_fr': "Conception & Modélisation 3D",
            'title_en': "3D Design & Modeling",
            'title_ar': "التصميم والنمذجة ثلاثية الأبعاد",
            'meta_title_fr': "Conception & Modélisation 3D | Tanger & Maroc",
            'meta_title_en': "3D Design & Modeling | Tangier & Morocco",
            'meta_title_ar': "تصميم ونمذجة ثلاثية الأبعاد | طنجة والمغرب",
            'meta_description_fr': "Modélisation 3D architecturale et rendus photoréalistes pour projets immobiliers à Tanger, Rabat et Casablanca. Valorisez vos espaces avant construction.",
            'meta_description_en': "Architectural 3D modeling and photorealistic renderings for real estate developments in Tangier and across Morocco. Showcase spaces before construction.",
            'meta_description_ar': "نمذجة معمارية ثلاثية الأبعاد وإظهار واقعي للمشاريع العقارية في طنجة، الرباط والدار البيضاء. أبرز جمال مشروعك قبل البناء.",
        },
        'visites-virtuelles': {
            'title_fr': "Capture 360° & Visites Immersives",
            'title_en': "360° Capture & Immersive Tours",
            'title_ar': "تصوير 360 درجة وجولات افتراضية",
            'meta_title_fr': "Visites Virtuelles Immersives 360° | Immobilier Tanger",
            'meta_title_en': "360° Immersive Virtual Tours | Real Estate Tangier",
            'meta_title_ar': "جولات افتراضية غامرة 360 درجة | عقارات طنجة",
            'meta_description_fr': "Visites virtuelles interactives 360° et expériences immersives pour valoriser et vendre vos biens immobiliers à Tanger et au Maroc.",
            'meta_description_en': "Interactive 360° virtual tours and immersive experiences to showcase and sell real estate properties in Tangier and across Morocco.",
            'meta_description_ar': "جولات افتراضية تفاعلية 360 درجة وتجارب غامرة لترويج وبيع العقارات في طنجة وجميع أنحاء المغرب.",
        },
        'captures-360': {
            'title_fr': "Captures 360° Réelles",
            'title_en': "360° Real Captures",
            'title_ar': "تصوير 360 درجة حقيقي",
            'meta_title_fr': "Captures 360° Réelles Haute Définition | Tanger",
            'meta_title_en': "High-Definition Real 360° Captures | Tangier",
            'meta_title_ar': "تصوير حقيقي 360 درجة عالي الدقة | طنجة",
            'meta_description_fr': "Numérisation et captures 360° photoréalistes d'espaces existants et chantiers immobiliers à Tanger et au Maroc.",
            'meta_description_en': "High-resolution 360° space digitization and real captures for real estate in Tangier and across Morocco.",
            'meta_description_ar': "مسح وتصوير احترافي 360 درجة للمساحات القائمة والمشاريع العقارية في طنجة وجميع أنحاء المغرب.",
        },
        'branding-visuel': {
            'title_fr': "Branding Immobilier",
            'title_en': "Real Estate Branding",
            'title_ar': "الهوية البصرية العقارية",
            'meta_title_fr': "Branding Immobilier & Identité Visuelle | Tanger",
            'meta_title_en': "Real Estate Branding & Visual Identity | Tangier",
            'meta_title_ar': "الهوية البصرية والتسويق العقاري | طنجة",
            'meta_description_fr': "Création d'identité visuelle, logos, brochures et univers de marque pour promoteurs et projets immobiliers à Tanger et au Maroc.",
            'meta_description_en': "Brand identity, naming, commercial brochures and marketing materials for property developers in Tangier, Morocco.",
            'meta_description_ar': "تصميم الهوية البصرية، الكتيبات التجارية، والاستراتيجية التسويقية للمشاريع العقارية في طنجة والمغرب.",
        },
        'site-web-digital': {
            'title_fr': "Site Web & Expérience Digitale",
            'title_en': "Website & Digital Experience",
            'title_ar': "موقع إلكتروني وتجربة رقمية",
            'meta_title_fr': "Site Web Immobilier & Expérience Digitale | Tanger",
            'meta_title_en': "Real Estate Websites & Digital Experience | Tangier",
            'meta_title_ar': "مواقع إلكترونية عقارية وتجارب رقمية | طنجة",
            'meta_description_fr': "Conception de sites web sur-mesure pour projets immobiliers intégrant visites 360°, plans 3D interactifs et génération de leads.",
            'meta_description_en': "Custom real estate website development with integrated 3D virtual tours, interactive plans, and lead generation in Morocco.",
            'meta_description_ar': "تصميم وتطوير مواقع إلكترونية مخصصة للمشاريع العقارية مدمجة بجولات 360 درجة ونماذج ثلاثية الأبعاد واستقطاب الزبناء.",
        },
        'lead-generation': {
            'title_fr': "Lead Generation & Suivi",
            'title_en': "Lead Generation & Tracking",
            'title_ar': "توليد ومتابعة العملاء المحتملين",
            'meta_title_fr': "Lead Generation & Marketing Immobilier | Tanger",
            'meta_title_en': "Real Estate Lead Generation & Marketing | Tangier",
            'meta_title_ar': "جذب العملاء المحتملين والتسويق العقاري | طنجة",
            'meta_description_fr': "Acquisition de prospects qualifiés, tunnels de conversion et campagnes publicitaires ciblées pour promoteurs immobiliers au Maroc.",
            'meta_description_en': "Qualified lead acquisition, digital conversion funnels, and targeted marketing campaigns for real estate in Morocco.",
            'meta_description_ar': "استقطاب مشترين مؤهلين، مسارات تحويل رقمية وإدارة الحملات الإعلانية للعقارات في طنجة والمغرب.",
        },
        'photographie': {
            'title_fr': "Photographie Professionnelle & Drone",
            'title_en': "Professional Photography & Drone",
            'title_ar': "تصوير فوتوغرافي احترافي وجوي",
            'meta_title_fr': "Photographie Immobilière & Drone | Tanger",
            'meta_title_en': "Real Estate Photography & Drone | Tangier",
            'meta_title_ar': "تصوير فوتوغرافي عقاري وجوي بالدرون | طنجة",
            'meta_description_fr': "Reportages photographiques professionnels et prises de vue par drone pour sublimer vos réalisations immobilières à Tanger.",
            'meta_description_en': "Professional real estate photography and aerial drone shots to elevate architectural projects in Tangier, Morocco.",
            'meta_description_ar': "جلسات تصوير احترافية وتصوير جوي بالدرون لإبراز جمال وتفاصيل المشاريع العقارية في طنجة.",
        },
        'animation-motion-design': {
            'title_fr': "Animation 3D & Motion Design",
            'title_en': "3D Animation & Motion Design",
            'title_ar': "رسوم متحركة ثلاثية الأبعاد وموشن ديزاين",
            'meta_title_fr': "Animation 3D & Motion Design Immobilier | Tanger",
            'meta_title_en': "3D Animation & Motion Design | Tangier",
            'meta_title_ar': "رسوم متحركة ثلاثية الأبعاد وفيديو سينمائي | طنجة",
            'meta_description_fr': "Films d'animation 3D, vidéos cinématiques et motion design pour présenter vos futurs programmes immobiliers à Tanger.",
            'meta_description_en': "3D architectural animation, cinematic video walkthroughs, and motion graphics for real estate developments in Morocco.",
            'meta_description_ar': "أفلام رسوم متحركة ثلاثية الأبعاد وجولات سينمائية لإبراز المشاريع العقارية المستقبلية في طنجة.",
        },
    }

    for slug, fields in SERVICES_DATA.items():
        svc = Service.objects.filter(slug=slug).first()
        if not svc:
            svc = Service.objects.filter(slug_fr=slug).first()
        if svc:
            for k, v in fields.items():
                if hasattr(svc, k):
                    setattr(svc, k, v)
            svc.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_promotion_video'),
        ('services', '0002_service_meta_description_service_meta_description_ar_and_more'),
    ]

    operations = [
        migrations.RunPython(update_site_settings_and_services, reverse_code=migrations.RunPython.noop),
    ]
