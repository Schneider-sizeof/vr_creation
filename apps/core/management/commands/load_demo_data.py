"""
Management command to populate realistic demo data in all 3 languages (FR/EN/AR).
No Lorem Ipsum — all content is professionally written.
"""
from datetime import date
from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.core.models import SiteSettings, TeamMember, Value, Strength, ProcessStep
from apps.services.models import Service
from apps.portfolio.models import Sector, Project, CaseStudy
from apps.blog.models import Category, Article
from apps.seo.models import PageSEO


class Command(BaseCommand):
    help = 'Charge le contenu de démonstration réaliste en FR/EN/AR'

    def handle(self, *args, **options):
        self.stdout.write('[...] Chargement des donnees de demonstration...')

        self._create_site_settings()
        self._create_values()
        self._create_strengths()
        self._create_process_steps()
        self._create_team()
        self._create_sectors()
        self._create_services()
        self._create_projects()
        self._create_case_studies()
        self._create_blog()
        self._create_page_seo()

        self.stdout.write(self.style.SUCCESS('[OK] Donnees de demonstration chargees avec succes !'))

    def _create_site_settings(self):
        settings, _ = SiteSettings.objects.get_or_create(pk=1)
        settings.site_name_fr = 'VR Creation Company'
        settings.site_name_en = 'VR Creation Company'
        settings.site_name_ar = 'في آر كرييشن'
        settings.tagline_fr = "L'innovation en action"
        settings.tagline_en = 'Innovation in Action'
        settings.tagline_ar = 'الابتكار في العمل'
        settings.email = 'contact@vrcreation.com'
        settings.phone = '+33 1 23 45 67 89'
        settings.address_fr = '75 Avenue des Champs-Élysées, 75008 Paris, France'
        settings.address_en = '75 Champs-Élysées Avenue, 75008 Paris, France'
        settings.address_ar = '75 شارع الشانزليزيه، 75008 باريس، فرنسا'
        settings.social_linkedin = 'https://linkedin.com/company/vrcreation'
        settings.social_instagram = 'https://instagram.com/vrcreation'
        settings.google_maps_embed_url = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2624.9916256937604!2d2.292292615674889!3d48.85837360866272!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47e66e2964e34e2d%3A0x8ddca9ee380ef7e0!2sTour%20Eiffel!5e0!3m2!1sfr!2sfr!4v1234567890'
        settings.footer_text_fr = "Nous allions esthetique et technologie de pointe pour transformer vos projets en experiences visuelles immersives et inoubliables."
        settings.footer_text_en = "We combine aesthetics and cutting-edge technology to transform your projects into immersive and unforgettable visual experiences."
        settings.footer_text_ar = "نجمع بين الجمالية والتكنولوجيا المتطورة لتحويل مشاريعك إلى تجارب بصرية غامرة لا تُنسى."
        settings.copyright_text_fr = "(c) 2026 VR Creation Company. Tous droits reserves."
        settings.copyright_text_en = "(c) 2026 VR Creation Company. All rights reserved."
        settings.copyright_text_ar = "(c) 2026 في آر كرييشن. جميع الحقوق محفوظة."
        settings.social_whatsapp = '+33612345678'
        settings.social_tiktok = 'https://tiktok.com/@vrcreation'
        settings.social_behance = 'https://behance.net/vrcreation'
        
        # Hero translations
        settings.hero_headline_fr = "DONNEZ VIE À VOTRE PROJET IMMOBILIER, AVANT MÊME SA CONSTRUCTION."
        settings.hero_headline_en = "BRING YOUR REAL ESTATE PROJECT TO LIFE, EVEN BEFORE ITS CONSTRUCTION."
        settings.hero_headline_ar = "امنح الحياة لمشروعك العقاري، حتى قبل بنائه."
        settings.hero_subheadline_fr = "De la conception 3D à la commercialisation digitale, nous transformons vos projets immobiliers en expériences visuelles capables de séduire, convaincre et générer des prospects."
        settings.hero_subheadline_en = "From 3D design to digital marketing, we transform your real estate projects into visual experiences capable of seducing, convincing and generating leads."
        settings.hero_subheadline_ar = "من التصميم ثلاثي الأبعاد إلى التسويق الرقمي، نحول مشاريعكم العقارية إلى تجارب بصرية قادرة على جذب وإقناع وجلب العملاء المحتملين."
        
        settings.save()
        self.stdout.write('  [+] Paramètres du site')

    def _create_values(self):
        data = [
            {
                'title_fr': 'Créativité', 'title_en': 'Creativity', 'title_ar': 'الإبداع',
                'description_fr': "Chaque projet est une toile vierge. Nous repoussons les limites créatives pour concevoir des visuels qui surprennent et marquent les esprits.",
                'description_en': 'Every project is a blank canvas. We push creative boundaries to design visuals that surprise and leave lasting impressions.',
                'description_ar': 'كل مشروع هو لوحة فارغة. نحن ندفع الحدود الإبداعية لتصميم مرئيات تفاجئ وتترك انطباعات دائمة.',
                'icon': '🎨', 'order': 1,
            },
            {
                'title_fr': 'Précision', 'title_en': 'Precision', 'title_ar': 'الدقة',
                'description_fr': "Le souci du détail est notre signature. Chaque texture, chaque lumière, chaque proportion est calibrée pour atteindre un réalisme saisissant.",
                'description_en': 'Attention to detail is our signature. Every texture, light, and proportion is calibrated for striking realism.',
                'description_ar': 'الاهتمام بالتفاصيل هو توقيعنا. كل نسيج وضوء ونسبة تم معايرتها لتحقيق واقعية مذهلة.',
                'icon': '🎯', 'order': 2,
            },
            {
                'title_fr': 'Innovation', 'title_en': 'Innovation', 'title_ar': 'الابتكار',
                'description_fr': "Nous adoptons les technologies de pointe — réalité virtuelle, captures 360°, IA — pour offrir des expériences toujours à l'avant-garde.",
                'description_en': 'We embrace cutting-edge technologies — virtual reality, 360° captures, AI — to deliver experiences always at the forefront.',
                'description_ar': 'نحن نتبنى التقنيات المتطورة — الواقع الافتراضي، التصوير 360 درجة، الذكاء الاصطناعي — لتقديم تجارب دائمًا في الطليعة.',
                'icon': '💡', 'order': 3,
            },
            {
                'title_fr': 'Excellence', 'title_en': 'Excellence', 'title_ar': 'التميز',
                'description_fr': "Notre engagement qualité est total : respect des délais, livrables irréprochables et accompagnement dédié à chaque étape du projet.",
                'description_en': 'Our commitment to quality is total: deadlines respected, impeccable deliverables, and dedicated support at every project stage.',
                'description_ar': 'التزامنا بالجودة كامل: احترام المواعيد النهائية، مخرجات لا تشوبها شائبة، ودعم مخصص في كل مرحلة من مراحل المشروع.',
                'icon': '⭐', 'order': 4,
            },
        ]
        for d in data:
            Value.objects.get_or_create(title_fr=d['title_fr'], defaults=d)
        self.stdout.write('  [+] Valeurs')

    def _create_strengths(self):
        # Clear existing strengths
        Strength.objects.all().delete()
        
        data = [
            {
                'title_fr': 'Créativité',
                'title_en': 'Creativity',
                'title_ar': 'الإبداع',
                'description_fr': 'Sublimer vos projets par des approches visuelles innovantes et esthétiques.',
                'description_en': 'Enhance your projects with innovative and aesthetic visual approaches.',
                'description_ar': 'تحسين مشاريعك بأساليب بصرية مبتكرة وجمالية.',
                'icon': 'fas fa-palette',
                'order': 1
            },
            {
                'title_fr': 'Précision',
                'title_en': 'Precision',
                'title_ar': 'الدقة',
                'description_fr': 'Un souci du détail minutieux pour des rendus ultra-réalistes.',
                'description_en': 'Meticulous attention to detail for ultra-realistic renders.',
                'description_ar': 'اهتمام دقيق بالتفاصيل لتصييرات فائقة الواقعية.',
                'icon': 'fas fa-crosshairs',
                'order': 2
            },
            {
                'title_fr': 'Professionnalisme',
                'title_en': 'Professionalism',
                'title_ar': 'الاحترافية',
                'description_fr': 'Respect des délais et accompagnement sur-mesure à chaque étape.',
                'description_en': 'On-time delivery and custom support at every stage.',
                'description_ar': 'اللتزام بالمواعيد والمرافقة المخصصة في كل مرحلة.',
                'icon': 'fas fa-briefcase',
                'order': 3
            },
            {
                'title_fr': 'Innovation',
                'title_en': 'Innovation',
                'title_ar': 'الابتكار',
                'description_fr': 'Utilisation des dernières technologies pour accélérer vos ventes.',
                'description_en': 'Using the latest technologies to accelerate your sales.',
                'description_ar': 'استخدام أحدث التقنيات لتسريع مبيعاتك.',
                'icon': 'fas fa-rocket',
                'order': 4
            },
        ]
        for d in data:
            Strength.objects.create(**d)
        self.stdout.write('  [+] Points forts')

    def _create_process_steps(self):
        data = [
            {'title_fr': 'Analyse & planification', 'title_en': 'Analysis & Planning', 'title_ar': 'التحليل والتخطيط',
             'description_fr': "Nous étudions vos plans, vos objectifs et votre univers de marque. Ensemble, nous définissons le périmètre du projet et les livrables attendus.",
             'description_en': 'We study your plans, objectives and brand universe. Together, we define the project scope and expected deliverables.',
             'description_ar': 'ندرس خططك وأهدافك وعالم علامتك التجارية. معًا نحدد نطاق المشروع والمخرجات المتوقعة.',
             'order': 1},
            {'title_fr': 'Structuration des espaces', 'title_en': 'Space Structuring', 'title_ar': 'هيكلة المساحات',
             'description_fr': "Nos architectes et designers modélisent les volumes, définissent les circulations et préparent les bases de la visualisation 3D.",
             'description_en': 'Our architects and designers model volumes, define circulations and prepare the foundations for 3D visualization.',
             'description_ar': 'يقوم المهندسون والمصممون لدينا بنمذجة الأحجام وتحديد الحركة وإعداد أسس التصور ثلاثي الأبعاد.',
             'order': 2},
            {'title_fr': 'Développement conceptuel', 'title_en': 'Conceptual Development', 'title_ar': 'التطوير المفاهيمي',
             'description_fr': "L'équipe créative donne vie au projet : textures, éclairages, mobilier, ambiance générale — chaque détail est travaillé pour refléter votre vision.",
             'description_en': 'The creative team brings the project to life: textures, lighting, furniture, general ambiance — every detail crafted to reflect your vision.',
             'description_ar': 'يعطي الفريق الإبداعي الحياة للمشروع: الأنسجة، الإضاءة، الأثاث، الأجواء العامة — كل تفصيل مصمم ليعكس رؤيتك.',
             'order': 3},
            {'title_fr': 'Échanges & ajustements', 'title_en': 'Review & Adjustments', 'title_ar': 'المراجعة والتعديلات',
             'description_fr': "Nous présentons les premières versions et intégrons vos retours. Un processus itératif qui garantit un résultat conforme à vos attentes.",
             'description_en': 'We present first drafts and incorporate your feedback. An iterative process ensuring results that meet your expectations.',
             'description_ar': 'نقدم النسخ الأولى وندمج ملاحظاتك. عملية تكرارية تضمن نتائج تلبي توقعاتك.',
             'order': 4},
            {'title_fr': 'Finalisation & livraison', 'title_en': 'Finalization & Delivery', 'title_ar': 'الإنهاء والتسليم',
             'description_fr': "Le rendu final est peaufiné, optimisé et livré dans les formats requis : visuels HD, visites virtuelles, vidéos, fichiers sources.",
             'description_en': 'The final render is polished, optimized and delivered in required formats: HD visuals, virtual tours, videos, source files.',
             'description_ar': 'يتم صقل العرض النهائي وتحسينه وتسليمه بالتنسيقات المطلوبة: مرئيات عالية الدقة، جولات افتراضية، فيديوهات، ملفات المصدر.',
             'order': 5},
        ]
        for d in data:
            ProcessStep.objects.get_or_create(title_fr=d['title_fr'], defaults=d)
        self.stdout.write('  [+] Étapes du processus')

    def _create_team(self):
        data = [
            {'name_fr': 'Alexandre Moreau', 'name_en': 'Alexandre Moreau', 'name_ar': 'ألكسندر مورو',
             'role_fr': 'Directeur créatif', 'role_en': 'Creative Director', 'role_ar': 'المدير الإبداعي',
             'bio_fr': 'Plus de 15 ans dans la direction artistique et la visualisation architecturale.',
             'bio_en': 'Over 15 years in art direction and architectural visualization.',
             'bio_ar': 'أكثر من 15 عامًا في الإخراج الفني والتصور المعماري.',
             'order': 1},
            {'name_fr': 'Sophie Laurent', 'name_en': 'Sophie Laurent', 'name_ar': 'صوفي لوران',
             'role_fr': 'Architecte 3D senior', 'role_en': 'Senior 3D Architect', 'role_ar': 'مهندسة ثلاثية الأبعاد أولى',
             'bio_fr': 'Spécialiste de la modélisation photoréaliste et des environnements immersifs.',
             'bio_en': 'Specialist in photorealistic modeling and immersive environments.',
             'bio_ar': 'متخصصة في النمذجة الواقعية والبيئات الغامرة.',
             'order': 2},
            {'name_fr': 'Karim Benali', 'name_en': 'Karim Benali', 'name_ar': 'كريم بن علي',
             'role_fr': 'Développeur VR / 360°', 'role_en': 'VR / 360° Developer', 'role_ar': 'مطور الواقع الافتراضي / 360 درجة',
             'bio_fr': 'Expert en développement de visites virtuelles interactives multi-plateformes.',
             'bio_en': 'Expert in developing multi-platform interactive virtual tours.',
             'bio_ar': 'خبير في تطوير الجولات الافتراضية التفاعلية متعددة المنصات.',
             'order': 3},
            {'name_fr': 'Emma Dubois', 'name_en': 'Emma Dubois', 'name_ar': 'إيما دوبوا',
             'role_fr': 'Chef de projet', 'role_en': 'Project Manager', 'role_ar': 'مديرة المشاريع',
             'bio_fr': 'Coordonne les projets avec rigueur pour garantir qualité et respect des délais.',
             'bio_en': 'Coordinates projects rigorously to ensure quality and timeline adherence.',
             'bio_ar': 'تنسق المشاريع بدقة لضمان الجودة والالتزام بالمواعيد النهائية.',
             'order': 4},
        ]
        for d in data:
            TeamMember.objects.get_or_create(name_fr=d['name_fr'], defaults=d)
        self.stdout.write('  [+] Équipe')

    def _create_sectors(self):
        data = [
            {'name_fr': 'Immobilier', 'name_en': 'Real Estate', 'name_ar': 'العقارات', 'slug': 'immobilier', 'order': 1},
            {'name_fr': 'Retail', 'name_en': 'Retail', 'name_ar': 'البيع بالتجزئة', 'slug': 'retail', 'order': 2},
            {'name_fr': 'Architecture', 'name_en': 'Architecture', 'name_ar': 'الهندسة المعمارية', 'slug': 'architecture', 'order': 3},
            {'name_fr': 'Tourisme', 'name_en': 'Tourism', 'name_ar': 'السياحة', 'slug': 'tourisme', 'order': 4},
            {'name_fr': 'Événementiel', 'name_en': 'Events', 'name_ar': 'الفعاليات', 'slug': 'evenementiel', 'order': 5},
        ]
        for d in data:
            slug = d.pop('slug')
            Sector.objects.get_or_create(slug=slug, defaults={**d, 'slug': slug})
        self.stdout.write('  [+] Secteurs')

    def _create_services(self):
        data = [
            {
                'title_fr': 'Conception & Modélisation 3D',
                'title_en': '3D Design & Modeling',
                'title_ar': 'التصميم والنمذجة ثلاثية الأبعاد',
                'slug': 'modelisation-3d',
                'icon': '🏗️',
                'short_description_fr': "Des rendus 3D photoréalistes et des maquettes virtuelles sur mesure qui donnent vie à vos projets avant même leur construction.",
                'short_description_en': 'Photorealistic 3D renders and custom virtual models that bring your projects to life before construction.',
                'short_description_ar': 'عروض ثلاثية الأبعاد واقعية ونماذج افتراضية مخصصة تضفي الحياة على مشاريعك قبل البناء.',
                'full_description_fr': "Notre service de modélisation 3D transforme vos plans architecturaux en visuels d'une qualité photographique saisissante. Grâce à nos technologies de rendu avancées, nous créons des représentations fidèles de vos espaces — intérieurs comme extérieurs — avec un niveau de détail qui permet à vos clients de se projeter immédiatement.\n\nChaque texture, chaque jeu de lumière, chaque matériau est reproduit avec une précision qui repousse les frontières du virtuel. Nos maquettes numériques interactives offrent une compréhension spatiale intuitive, idéale pour la commercialisation sur plan ou la validation de concepts architecturaux.",
                'full_description_en': "Our 3D modeling service transforms your architectural plans into visuals of stunning photographic quality. Using advanced rendering technologies, we create faithful representations of your spaces — both interior and exterior — with a level of detail that allows your clients to immediately envision themselves.\n\nEvery texture, every play of light, every material is reproduced with precision that pushes the boundaries of virtual reality. Our interactive digital models offer intuitive spatial understanding, ideal for off-plan sales or architectural concept validation.",
                'full_description_ar': "تحول خدمة النمذجة ثلاثية الأبعاد لدينا مخططاتك المعمارية إلى مرئيات بجودة تصويرية مذهلة. باستخدام تقنيات العرض المتقدمة، نقوم بإنشاء تمثيلات وفية لمساحاتك — الداخلية والخارجية — بمستوى من التفاصيل يسمح لعملائك بتصور أنفسهم فورًا.\n\nكل نسيج، كل لعب ضوء، كل مادة يتم إعادة إنتاجها بدقة تدفع حدود الواقع الافتراضي.",
                'order': 1,
            },
            {
                'title_fr': 'Visites virtuelles interactives',
                'title_en': 'Interactive Virtual Tours',
                'title_ar': 'الجولات الافتراضية التفاعلية',
                'slug': 'visites-virtuelles',
                'icon': '🥽',
                'short_description_fr': "Offrez à vos clients une immersion totale dans vos espaces grâce à des visites virtuelles navigables sur tous les appareils.",
                'short_description_en': 'Give your clients total immersion in your spaces with virtual tours navigable on all devices.',
                'short_description_ar': 'امنح عملائك انغماسًا كاملاً في مساحاتك من خلال جولات افتراضية قابلة للتنقل على جميع الأجهزة.',
                'full_description_fr': "Nos visites virtuelles interactives permettent à vos prospects d'explorer chaque recoin de vos espaces depuis leur écran — ordinateur, tablette ou smartphone. Grâce à une navigation fluide et intuitive, l'utilisateur se déplace librement, zoom sur les détails et découvre l'ambiance réelle du lieu.\n\nIdéales pour l'immobilier, l'hôtellerie, le retail ou l'événementiel, ces visites remplacent efficacement les déplacements physiques et accélèrent la prise de décision.",
                'full_description_en': "Our interactive virtual tours allow your prospects to explore every corner of your spaces from their screen — desktop, tablet or smartphone. With fluid and intuitive navigation, users move freely, zoom into details and discover the true ambiance of the place.\n\nIdeal for real estate, hospitality, retail or events, these tours effectively replace physical visits and accelerate decision-making.",
                'full_description_ar': "تتيح جولاتنا الافتراضية التفاعلية لعملائك المحتملين استكشاف كل ركن من مساحاتك من شاشتهم — سطح المكتب أو الجهاز اللوحي أو الهاتف الذكي. مع التنقل السلس والبديهي، يتحرك المستخدمون بحرية ويكبرون التفاصيل ويكتشفون الأجواء الحقيقية للمكان.",
                'order': 2,
            },
            {
                'title_fr': 'Captures 360° réelles',
                'title_en': '360° Real Captures',
                'title_ar': 'التقاط 360 درجة حقيقي',
                'slug': 'captures-360',
                'icon': '📸',
                'short_description_fr': "Capturez la réalité de vos espaces existants avec notre technologie 360° haute résolution pour showrooms, commerces et événements.",
                'short_description_en': 'Capture the reality of your existing spaces with our high-resolution 360° technology for showrooms, stores and events.',
                'short_description_ar': 'التقط واقع مساحاتك الحالية بتقنيتنا عالية الدقة 360 درجة لصالات العرض والمتاجر والفعاليات.',
                'full_description_fr': "Nos captures 360° haute résolution immortalisent vos espaces tels qu'ils sont, dans toute leur authenticité. Nous intervenons sur site avec un équipement professionnel pour produire des panoramiques immersifs qui transportent virtuellement le visiteur au cœur de votre lieu.\n\nParfaites pour les showrooms, les hôtels, les restaurants, les sites touristiques ou les espaces événementiels, ces captures constituent un outil de communication puissant et différenciant.",
                'full_description_en': "Our high-resolution 360° captures immortalize your spaces as they are, in all their authenticity. We work on-site with professional equipment to produce immersive panoramas that virtually transport visitors to the heart of your space.\n\nPerfect for showrooms, hotels, restaurants, tourist sites or event spaces, these captures are a powerful and differentiating communication tool.",
                'full_description_ar': "تخلد عمليات التقاط 360 درجة عالية الدقة لدينا مساحاتك كما هي، بكل أصالتها. نعمل في الموقع بمعدات احترافية لإنتاج بانوراما غامرة تنقل الزوار فعليًا إلى قلب مساحتك.",
                'order': 3,
            },
            {
                'title_fr': 'Branding & communication visuelle',
                'title_en': 'Branding & Visual Communication',
                'title_ar': 'العلامة التجارية والتواصل البصري',
                'slug': 'branding-visuel',
                'icon': '🎨',
                'short_description_fr': "Construisez une identité visuelle mémorable avec nos créations graphiques premium : logos, chartes, supports publicitaires.",
                'short_description_en': 'Build a memorable visual identity with our premium graphic creations: logos, brand guidelines, advertising materials.',
                'short_description_ar': 'ابنِ هوية بصرية لا تُنسى مع إبداعاتنا الجرافيكية المميزة: الشعارات، إرشادات العلامة التجارية، المواد الإعلانية.',
                'full_description_fr': "Votre image de marque est votre premier ambassadeur. Notre équipe de designers conçoit des identités visuelles complètes qui reflètent l'ADN de votre entreprise et captivent votre audience cible.\n\nDu logo à la charte graphique, des supports print aux déclinaisons digitales, nous créons un univers visuel cohérent et impactant qui renforce votre crédibilité et vous différencie sur votre marché.",
                'full_description_en': "Your brand image is your first ambassador. Our team of designers creates complete visual identities that reflect your company's DNA and captivate your target audience.\n\nFrom logo to brand guidelines, from print materials to digital adaptations, we create a coherent and impactful visual universe that strengthens your credibility and differentiates you in your market.",
                'full_description_ar': "صورة علامتك التجارية هي سفيرك الأول. يقوم فريق المصممين لدينا بإنشاء هويات بصرية كاملة تعكس الحمض النووي لشركتك وتأسر جمهورك المستهدف.",
                'order': 4,
            },
            {
                'title_fr': 'Photographie professionnelle',
                'title_en': 'Professional Photography',
                'title_ar': 'التصوير الفوتوغرافي الاحترافي',
                'slug': 'photographie',
                'icon': '📷',
                'short_description_fr': "Des clichés d'exception qui subliment vos espaces, produits et événements avec un œil expert et un équipement de pointe.",
                'short_description_en': "Exceptional shots that enhance your spaces, products and events with expert eye and cutting-edge equipment.",
                'short_description_ar': 'لقطات استثنائية تعزز مساحاتك ومنتجاتك وفعالياتك بعين خبيرة ومعدات متطورة.',
                'full_description_fr': "Notre service de photographie professionnelle couvre l'ensemble de vos besoins visuels : architecture, intérieurs, produits, corporate, événementiel. Nos photographes maîtrisent l'art de la lumière et de la composition pour livrer des images qui valorisent chaque sujet.\n\nPost-production soignée, formats optimisés pour le web et l'impression, livraison rapide — nous assurons un rendu premium de bout en bout.",
                'full_description_en': "Our professional photography service covers all your visual needs: architecture, interiors, products, corporate, events. Our photographers master the art of light and composition to deliver images that enhance every subject.\n\nCareful post-production, web and print-optimized formats, fast delivery — we ensure premium quality from start to finish.",
                'full_description_ar': "تغطي خدمة التصوير الفوتوغرافي الاحترافي لدينا جميع احتياجاتك البصرية: الهندسة المعمارية، الديكور الداخلي، المنتجات، الشركات، الفعاليات.",
                'order': 5,
            },
            {
                'title_fr': 'Animation & motion design',
                'title_en': 'Animation & Motion Design',
                'title_ar': 'الرسوم المتحركة وتصميم الحركة',
                'slug': 'animation-motion-design',
                'icon': '🎬',
                'short_description_fr': "Donnez du mouvement à vos idées avec nos animations 3D et vidéos motion design qui captivent et convertissent.",
                'short_description_en': 'Give movement to your ideas with our 3D animations and motion design videos that captivate and convert.',
                'short_description_ar': 'أعطِ حركة لأفكارك من خلال الرسوم المتحركة ثلاثية الأبعاد وفيديوهات تصميم الحركة التي تأسر وتحول.',
                'full_description_fr': "L'animation ajoute une dimension émotionnelle unique à votre communication. Nos motion designers créent des vidéos percutantes qui racontent votre histoire, présentent vos projets en mouvement et renforcent l'engagement de votre audience.\n\nSurvols architecturaux, animations produit, vidéos explicatives, teasers immobiliers — chaque format est conçu pour maximiser l'impact sur vos canaux de diffusion.",
                'full_description_en': "Animation adds a unique emotional dimension to your communication. Our motion designers create impactful videos that tell your story, present your projects in motion and boost audience engagement.\n\nArchitectural flythroughs, product animations, explainer videos, real estate teasers — each format designed to maximize impact across your distribution channels.",
                'full_description_ar': "تضيف الرسوم المتحركة بعدًا عاطفيًا فريدًا لتواصلك. يقوم مصممو الحركة لدينا بإنشاء فيديوهات مؤثرة تروي قصتك وتعرض مشاريعك بالحركة وتعزز تفاعل الجمهور.",
                'order': 6,
            },
        ]
        for d in data:
            slug = d.pop('slug')
            Service.objects.get_or_create(slug=slug, defaults={**d, 'slug': slug, 'is_active': True})
        self.stdout.write('  [+] Services')

    def _create_projects(self):
        immo = Sector.objects.filter(slug='immobilier').first()
        retail = Sector.objects.filter(slug='retail').first()
        archi = Sector.objects.filter(slug='architecture').first()

        data = [
            {
                'title_fr': 'Résidence Azure — Programme immobilier de prestige',
                'title_en': 'Azure Residence — Prestigious Real Estate Program',
                'title_ar': 'إقامة أزور — برنامج عقاري فاخر',
                'slug': 'residence-azure',
                'sector': immo,
                'client_fr': 'Groupe Immobilier Azur',
                'client_en': 'Azur Real Estate Group',
                'client_ar': 'مجموعة أزور العقارية',
                'description_fr': "Modélisation 3D complète d'un programme immobilier de 45 appartements haut de gamme en bord de mer. Visuels photoréalistes des intérieurs, espaces communs et façades pour la commercialisation sur plan.",
                'description_en': "Complete 3D modeling of a 45-unit luxury seaside apartment program. Photorealistic visuals of interiors, common areas and facades for off-plan sales.",
                'description_ar': "نمذجة ثلاثية الأبعاد كاملة لبرنامج سكني فاخر مكون من 45 شقة على شاطئ البحر.",
                'challenge_fr': 'Commercialiser un programme immobilier dont la construction n\'avait pas encore débuté, sans aucun visuel concret à présenter aux acheteurs potentiels.',
                'challenge_en': 'Marketing a real estate program whose construction had not yet begun, with no concrete visuals to present to potential buyers.',
                'challenge_ar': 'تسويق برنامج عقاري لم يبدأ بناؤه بعد، بدون أي مرئيات ملموسة لتقديمها للمشترين المحتملين.',
                'solution_fr': 'Création de 12 rendus 3D photoréalistes, 3 vidéos de survol et une visite virtuelle complète de l\'appartement témoin.',
                'solution_en': 'Creation of 12 photorealistic 3D renders, 3 flyover videos and a complete virtual tour of the show apartment.',
                'solution_ar': 'إنشاء 12 عرضًا ثلاثي الأبعاد واقعيًا و3 فيديوهات تحليق وجولة افتراضية كاملة للشقة النموذجية.',
                'result_fr': '85% des lots vendus avant le début des travaux, soit 6 mois d\'avance sur le plan de commercialisation initial.',
                'result_en': '85% of units sold before construction began, 6 months ahead of the initial sales plan.',
                'result_ar': 'بيع 85% من الوحدات قبل بدء البناء، أي قبل 6 أشهر من خطة المبيعات الأولية.',
                'is_featured': True,
                'has_virtual_tour': True,
                'virtual_tour_url': 'https://pannellum.org/images/cerro-toco-702702.jpg',
                'date': date(2025, 6, 15),
            },
            {
                'title_fr': 'Concept Store Lumière — Retail nouvelle génération',
                'title_en': 'Lumière Concept Store — Next-Gen Retail',
                'title_ar': 'متجر لوميير المفاهيمي — تجزئة الجيل القادم',
                'slug': 'concept-store-lumiere',
                'sector': retail,
                'client_fr': 'Maison Lumière',
                'client_en': 'Maison Lumière',
                'client_ar': 'ميزون لوميير',
                'description_fr': "Capture 360° complète d'un concept store de 300m² et création d'une visite virtuelle interactive permettant aux clients de découvrir l'espace depuis chez eux et de visualiser les produits en contexte.",
                'description_en': "Complete 360° capture of a 300sqm concept store and creation of an interactive virtual tour allowing customers to discover the space from home and visualize products in context.",
                'description_ar': "التقاط 360 درجة كامل لمتجر مفاهيمي بمساحة 300 متر مربع وإنشاء جولة افتراضية تفاعلية.",
                'challenge_fr': 'Augmenter le trafic en ligne et convertir les visiteurs digitaux en clients physiques pour un magasin récemment rénové.',
                'challenge_en': 'Increase online traffic and convert digital visitors to physical customers for a recently renovated store.',
                'challenge_ar': 'زيادة حركة المرور عبر الإنترنت وتحويل الزوار الرقميين إلى عملاء فعليين لمتجر تم تجديده مؤخرًا.',
                'solution_fr': 'Visite virtuelle 360° avec points d\'intérêt cliquables, intégrée au site e-commerce du client.',
                'solution_en': '360° virtual tour with clickable hotspots, integrated into the client\'s e-commerce site.',
                'solution_ar': 'جولة افتراضية 360 درجة مع نقاط اهتمام قابلة للنقر، مدمجة في موقع التجارة الإلكترونية للعميل.',
                'result_fr': '+120% de trafic web, +35% de visites en magasin dans les 3 premiers mois suivant le lancement.',
                'result_en': '+120% web traffic, +35% in-store visits in the first 3 months after launch.',
                'result_ar': '+120% حركة مرور الويب، +35% زيارات في المتجر في الأشهر الثلاثة الأولى بعد الإطلاق.',
                'is_featured': True,
                'has_virtual_tour': False,
                'date': date(2025, 3, 20),
            },
            {
                'title_fr': 'Villa Méditerranée — Résidence privée de luxe',
                'title_en': 'Mediterranean Villa — Luxury Private Residence',
                'title_ar': 'فيلا البحر الأبيض المتوسط — إقامة خاصة فاخرة',
                'slug': 'villa-mediterranee',
                'sector': archi,
                'client_fr': 'Client privé',
                'client_en': 'Private client',
                'client_ar': 'عميل خاص',
                'description_fr': "Modélisation 3D intégrale d'une villa contemporaine de 500m² en phase de conception. Rendus extérieurs et intérieurs avec intégration paysagère, suivi des modifications architecturales en temps réel.",
                'description_en': "Complete 3D modeling of a 500sqm contemporary villa in design phase. Exterior and interior renders with landscape integration, real-time architectural modification tracking.",
                'description_ar': "نمذجة ثلاثية الأبعاد كاملة لفيلا معاصرة بمساحة 500 متر مربع في مرحلة التصميم.",
                'challenge_fr': 'Permettre au client de valider chaque choix architectural et décoratif avant le début de la construction.',
                'challenge_en': 'Allow the client to validate every architectural and decorative choice before construction begins.',
                'challenge_ar': 'السماح للعميل بالتحقق من كل خيار معماري وزخرفي قبل بدء البناء.',
                'solution_fr': 'Modélisation 3D évolutive avec 8 itérations, visite virtuelle interactive du projet final.',
                'solution_en': 'Iterative 3D modeling with 8 iterations, interactive virtual tour of the final design.',
                'solution_ar': 'نمذجة ثلاثية الأبعاد تطورية مع 8 تكرارات، جولة افتراضية تفاعلية للتصميم النهائي.',
                'result_fr': 'Zéro modification post-construction, économie estimée à 45 000€ sur le budget travaux.',
                'result_en': 'Zero post-construction modifications, estimated savings of €45,000 on construction budget.',
                'result_ar': 'صفر تعديلات بعد البناء، توفير مقدر بـ 45,000 يورو في ميزانية البناء.',
                'is_featured': True,
                'has_virtual_tour': True,
                'virtual_tour_url': 'https://pannellum.org/images/jfk-702702.jpg',
                'date': date(2025, 9, 1),
            },
        ]
        for d in data:
            slug = d.pop('slug')
            Project.objects.get_or_create(slug=slug, defaults={**d, 'slug': slug})
        self.stdout.write('  [+] Projets portfolio')

    def _create_case_studies(self):
        immo = Sector.objects.filter(slug='immobilier').first()
        retail = Sector.objects.filter(slug='retail').first()
        evt = Sector.objects.filter(slug='evenementiel').first()

        data = [
            {
                'title_fr': 'Accélération des ventes d\'un programme neuf',
                'title_en': 'Accelerating Sales for a New Development',
                'title_ar': 'تسريع مبيعات برنامج جديد',
                'slug': 'acceleration-ventes-programme-neuf',
                'sector': immo,
                'problem_fr': "Un promoteur immobilier lançait un programme de 60 logements mais peinait à convaincre les acheteurs sans espace témoin physique, les délais de construction ne permettant pas de proposer des visites sur site.",
                'problem_en': "A real estate developer was launching a 60-unit program but struggled to convince buyers without a physical showroom, as construction timelines didn't allow on-site visits.",
                'problem_ar': "كان مطور عقاري يطلق برنامجًا مكونًا من 60 وحدة سكنية لكنه واجه صعوبة في إقناع المشترين بدون صالة عرض فعلية.",
                'service_importance_fr': "La visualisation 3D et les visites virtuelles ont permis de créer un argumentaire de vente visuel puissant : les prospects pouvaient explorer chaque type d'appartement, personnaliser les finitions et se projeter dans leur futur logement.",
                'service_importance_en': "3D visualization and virtual tours created a powerful visual sales pitch: prospects could explore each apartment type, customize finishes and envision their future home.",
                'service_importance_ar': "أتاح التصور ثلاثي الأبعاد والجولات الافتراضية إنشاء عرض مبيعات بصري قوي.",
                'result_fr': "70% des lots réservés en 4 mois, contre un objectif initial de 12 mois. Le taux de transformation des visites virtuelles vers les rendez-vous commerciaux a atteint 45%.",
                'result_en': "70% of units reserved in 4 months, vs. an initial 12-month target. Virtual tour-to-sales appointment conversion rate reached 45%.",
                'result_ar': "حجز 70% من الوحدات في 4 أشهر، مقابل هدف أولي مدته 12 شهرًا.",
                'efficiency_fr': "Retour sur investissement de 800% : le coût de production des visuels 3D a été amorti dès le premier mois de commercialisation grâce à l'accélération significative des ventes.",
                'efficiency_en': "800% return on investment: 3D visual production costs were recouped in the first month of sales thanks to significant sales acceleration.",
                'efficiency_ar': "عائد استثمار بنسبة 800%: تم استرداد تكاليف إنتاج المرئيات ثلاثية الأبعاد في الشهر الأول من المبيعات.",
                'date': date(2025, 5, 10),
            },
            {
                'title_fr': 'Transformation digitale d\'un concept-store',
                'title_en': 'Digital Transformation of a Concept Store',
                'title_ar': 'التحول الرقمي لمتجر مفاهيمي',
                'slug': 'transformation-digitale-concept-store',
                'sector': retail,
                'problem_fr': "Une enseigne de décoration haut de gamme souhaitait étendre son rayonnement au-delà de sa zone de chalandise physique, sans ouvrir de nouveaux points de vente coûteux.",
                'problem_en': "A high-end home décor brand wanted to extend its reach beyond its physical catchment area without opening costly new stores.",
                'problem_ar': "أرادت علامة تجارية راقية للديكور المنزلي توسيع نطاق وصولها خارج منطقة تغطيتها الفعلية.",
                'service_importance_fr': "La visite virtuelle 360° du showroom, couplée à une navigation enrichie avec fiches produits et liens d'achat, a créé une expérience d'achat hybride unique, à mi-chemin entre le e-commerce et la visite en magasin.",
                'service_importance_en': "The 360° virtual tour of the showroom, coupled with enriched navigation featuring product cards and purchase links, created a unique hybrid shopping experience.",
                'service_importance_ar': "أنشأت الجولة الافتراضية 360 درجة لصالة العرض تجربة تسوق هجينة فريدة.",
                'result_fr': "+200% de commandes en ligne dans les 6 mois. Le panier moyen des clients ayant utilisé la visite virtuelle était 40% supérieur à celui des acheteurs classiques.",
                'result_en': "+200% online orders in 6 months. Average basket for customers using the virtual tour was 40% higher than traditional buyers.",
                'result_ar': "+200% طلبات عبر الإنترنت في 6 أشهر. كان متوسط سلة العملاء الذين استخدموا الجولة الافتراضية أعلى بنسبة 40%.",
                'efficiency_fr': "L'investissement dans la visite virtuelle a été rentabilisé en 8 semaines. Le showroom virtuel est devenu le premier canal d'acquisition de nouveaux clients hors zone.",
                'efficiency_en': "The virtual tour investment paid for itself in 8 weeks. The virtual showroom became the top acquisition channel for new out-of-area clients.",
                'efficiency_ar': "أثمر الاستثمار في الجولة الافتراضية عن عوائده في 8 أسابيع.",
                'date': date(2025, 8, 15),
            },
            {
                'title_fr': 'Couverture immersive d\'un salon professionnel',
                'title_en': 'Immersive Coverage of a Trade Show',
                'title_ar': 'تغطية غامرة لمعرض تجاري',
                'slug': 'couverture-immersive-salon',
                'sector': evt,
                'problem_fr': "L'organisateur d'un salon professionnel international souhaitait offrir une expérience mémorable aux exposants absents et prolonger la durée de vie de l'événement au-delà des 3 jours physiques.",
                'problem_en': "An international trade show organizer wanted to offer a memorable experience to absent exhibitors and extend the event's lifespan beyond the 3 physical days.",
                'problem_ar': "أراد منظم معرض تجاري دولي تقديم تجربة لا تُنسى للعارضين الغائبين.",
                'service_importance_fr': "La captation 360° de l'intégralité du salon (120 stands) combinée à une plateforme de visite virtuelle interactive a permis de créer un « salon permanent » accessible en ligne toute l'année.",
                'service_importance_en': "The complete 360° capture of the entire show (120 booths) combined with an interactive virtual tour platform created a 'permanent trade show' accessible online year-round.",
                'service_importance_ar': "أدى التقاط 360 درجة الكامل للمعرض بأكمله (120 جناحًا) إلى إنشاء 'معرض دائم' متاح عبر الإنترنت.",
                'result_fr': "15 000 visites virtuelles dans les 2 mois post-événement. 30% des exposants ont renouvelé leur participation l'année suivante grâce à la visibilité prolongée.",
                'result_en': "15,000 virtual visits in the 2 months post-event. 30% of exhibitors renewed their participation the following year thanks to extended visibility.",
                'result_ar': "15,000 زيارة افتراضية في الشهرين التاليين للحدث. جدد 30% من العارضين مشاركتهم في العام التالي.",
                'efficiency_fr': "Le coût par lead généré via la visite virtuelle était 5x inférieur à celui des canaux traditionnels. Le salon virtuel est devenu un produit à part entière, générant des revenus publicitaires additionnels.",
                'efficiency_en': "Cost per lead generated via the virtual tour was 5x lower than traditional channels. The virtual show became a standalone product generating additional advertising revenue.",
                'efficiency_ar': "كانت تكلفة العميل المحتمل عبر الجولة الافتراضية أقل بـ 5 مرات من القنوات التقليدية.",
                'date': date(2025, 11, 5),
            },
        ]
        for d in data:
            slug = d.pop('slug')
            CaseStudy.objects.get_or_create(slug=slug, defaults={**d, 'slug': slug})
        self.stdout.write('  [+] Études de cas')

    def _create_blog(self):
        cat_tech, _ = Category.objects.get_or_create(
            slug='technologie',
            defaults={
                'name_fr': 'Technologie', 'name_en': 'Technology', 'name_ar': 'التكنولوجيا',
                'slug': 'technologie',
            }
        )
        cat_tips, _ = Category.objects.get_or_create(
            slug='conseils',
            defaults={
                'name_fr': 'Conseils', 'name_en': 'Tips', 'name_ar': 'نصائح',
                'slug': 'conseils',
            }
        )
        cat_trends, _ = Category.objects.get_or_create(
            slug='tendances',
            defaults={
                'name_fr': 'Tendances', 'name_en': 'Trends', 'name_ar': 'الاتجاهات',
                'slug': 'tendances',
            }
        )

        articles = [
            {
                'title_fr': "5 raisons d'adopter la visite virtuelle pour votre projet immobilier",
                'title_en': '5 Reasons to Adopt Virtual Tours for Your Real Estate Project',
                'title_ar': '5 أسباب لاعتماد الجولة الافتراضية لمشروعك العقاري',
                'slug': '5-raisons-visite-virtuelle-immobilier',
                'category': cat_tips,
                'author_fr': 'Alexandre Moreau', 'author_en': 'Alexandre Moreau', 'author_ar': 'ألكسندر مورو',
                'excerpt_fr': "La visite virtuelle n'est plus un gadget : c'est un accélérateur de ventes qui transforme radicalement la commercialisation immobilière.",
                'excerpt_en': "Virtual tours are no longer a gimmick: they're a sales accelerator that radically transforms real estate marketing.",
                'excerpt_ar': 'لم تعد الجولات الافتراضية مجرد أداة ترفيهية: إنها مسرّع مبيعات يحول تسويق العقارات جذريًا.',
                'content_fr': "L'industrie immobilière connaît une transformation digitale sans précédent. Au cœur de cette révolution, la visite virtuelle s'impose comme l'outil incontournable pour les promoteurs et agents immobiliers qui souhaitent se démarquer.\n\n1. **Qualification des prospects à distance** : Les acheteurs potentiels peuvent explorer le bien depuis n'importe où, éliminant les visites de curiosité et ne mobilisant les commerciaux que pour les prospects véritablement intéressés.\n\n2. **Disponibilité 24/7** : Contrairement à un espace témoin physique, la visite virtuelle est accessible à toute heure, depuis n'importe quel appareil. Un atout décisif pour les acheteurs internationaux dans des fuseaux horaires différents.\n\n3. **Réduction du cycle de vente** : Nos données montrent que les programmes disposant d'une visite virtuelle réduisent leur cycle de vente de 30 à 50%. Les acheteurs arrivent en rendez-vous avec une connaissance approfondie du bien.\n\n4. **Avantage concurrentiel immédiat** : Dans un marché compétitif, proposer une expérience immersive différencie instantanément votre offre. C'est un signal de modernité et de professionnalisme.\n\n5. **ROI mesurable** : Le coût de production d'une visite virtuelle est infime comparé au budget marketing global d'un programme. Le retour sur investissement se mesure en semaines, pas en mois.",
                'content_en': "The real estate industry is undergoing unprecedented digital transformation. At the heart of this revolution, virtual tours have become the essential tool for developers and agents looking to stand out.\n\n1. **Remote prospect qualification**: Potential buyers can explore properties from anywhere, eliminating curiosity visits and only mobilizing sales teams for genuinely interested prospects.\n\n2. **24/7 availability**: Unlike physical showrooms, virtual tours are accessible at any time, from any device. A decisive advantage for international buyers in different time zones.\n\n3. **Reduced sales cycle**: Our data shows that programs with virtual tours reduce their sales cycle by 30-50%. Buyers arrive at appointments with thorough knowledge of the property.\n\n4. **Immediate competitive advantage**: In a competitive market, offering an immersive experience instantly differentiates your offering. It signals modernity and professionalism.\n\n5. **Measurable ROI**: The cost of producing a virtual tour is minimal compared to a program's overall marketing budget. Return on investment is measured in weeks, not months.",
                'content_ar': "تشهد صناعة العقارات تحولًا رقميًا غير مسبوق. في قلب هذه الثورة، أصبحت الجولات الافتراضية الأداة الأساسية للمطورين والوكلاء الذين يتطلعون إلى التميز.",
                'reading_time': 6,
                'published_date': timezone.now(),
                'is_published': True,
            },
            {
                'title_fr': "Tendances 2026 : l'IA au service de la visualisation architecturale",
                'title_en': '2026 Trends: AI in Architectural Visualization',
                'title_ar': 'اتجاهات 2026: الذكاء الاصطناعي في التصور المعماري',
                'slug': 'tendances-2026-ia-visualisation-architecturale',
                'category': cat_trends,
                'author_fr': 'Sophie Laurent', 'author_en': 'Sophie Laurent', 'author_ar': 'صوفي لوران',
                'excerpt_fr': "L'intelligence artificielle bouleverse les workflows de visualisation 3D. Découvrez les innovations qui redéfinissent notre métier en 2026.",
                'excerpt_en': "Artificial intelligence is disrupting 3D visualization workflows. Discover the innovations redefining our industry in 2026.",
                'excerpt_ar': 'يعطل الذكاء الاصطناعي سير عمل التصور ثلاثي الأبعاد. اكتشف الابتكارات التي تعيد تعريف صناعتنا في 2026.',
                'content_fr': "L'année 2026 marque un tournant majeur dans notre industrie. L'intégration de l'intelligence artificielle dans les pipelines de rendu 3D ouvre des perspectives fascinantes pour les professionnels de la visualisation architecturale.\n\nLes outils de génération assistée permettent désormais de créer des variantes d'aménagement en quelques minutes plutôt qu'en plusieurs heures. L'IA aide à optimiser les placements de lumière, suggère des palettes de matériaux cohérentes et accélère considérablement la phase de post-production.\n\nCependant, l'expertise humaine reste irremplaçable : la sensibilité artistique, la compréhension des enjeux client et la direction créative sont des compétences que l'IA augmente sans pouvoir les remplacer.",
                'content_en': "2026 marks a major turning point in our industry. The integration of artificial intelligence into 3D rendering pipelines opens fascinating perspectives for architectural visualization professionals.\n\nAI-assisted generation tools now create layout variants in minutes rather than hours. AI helps optimize light placement, suggests coherent material palettes and dramatically accelerates the post-production phase.\n\nHowever, human expertise remains irreplaceable: artistic sensitivity, understanding of client challenges and creative direction are skills that AI enhances without being able to replace.",
                'content_ar': "يمثل عام 2026 نقطة تحول رئيسية في صناعتنا. يفتح دمج الذكاء الاصطناعي في خطوط إنتاج العرض ثلاثي الأبعاد آفاقًا رائعة.",
                'reading_time': 8,
                'published_date': timezone.now(),
                'is_published': True,
            },
            {
                'title_fr': 'Comment choisir entre modélisation 3D et capture 360° ?',
                'title_en': 'How to Choose Between 3D Modeling and 360° Capture?',
                'title_ar': 'كيف تختار بين النمذجة ثلاثية الأبعاد والتقاط 360 درجة؟',
                'slug': 'choisir-modelisation-3d-capture-360',
                'category': cat_tech,
                'author_fr': 'Karim Benali', 'author_en': 'Karim Benali', 'author_ar': 'كريم بن علي',
                'excerpt_fr': "Deux approches complémentaires pour deux cas d'usage différents. Guide pratique pour faire le bon choix selon votre projet.",
                'excerpt_en': "Two complementary approaches for two different use cases. A practical guide to making the right choice for your project.",
                'excerpt_ar': 'نهجان متكاملان لحالتي استخدام مختلفتين. دليل عملي لاتخاذ القرار الصحيح لمشروعك.',
                'content_fr': "L'une des questions les plus fréquentes de nos clients : faut-il opter pour la modélisation 3D ou la capture 360° ?\n\n**La modélisation 3D** est idéale lorsque l'espace n'existe pas encore physiquement (projets sur plan, rénovations, prototypes). Elle offre une liberté totale de personnalisation et permet de créer des visuels « parfaits ».\n\n**La capture 360°** convient parfaitement aux espaces existants que l'on souhaite documenter ou promouvoir avec authenticité. Elle est plus rapide à produire et transmet une sensation de réalité brute.\n\nNotre recommandation : combinez les deux pour un impact maximal. La modélisation 3D pour montrer le potentiel, la capture 360° pour prouver la réalité.",
                'content_en': "One of our clients' most frequent questions: should you choose 3D modeling or 360° capture?\n\n**3D Modeling** is ideal when the space doesn't yet physically exist (off-plan projects, renovations, prototypes). It offers total customization freedom and creates 'perfect' visuals.\n\n**360° Capture** is perfect for existing spaces you want to document or promote with authenticity. It's faster to produce and conveys a sense of raw reality.\n\nOur recommendation: combine both for maximum impact.",
                'content_ar': "أحد الأسئلة الأكثر شيوعًا من عملائنا: هل يجب اختيار النمذجة ثلاثية الأبعاد أم التقاط 360 درجة؟",
                'reading_time': 5,
                'published_date': timezone.now(),
                'is_published': True,
            },
        ]
        for d in articles:
            slug = d.pop('slug')
            Article.objects.get_or_create(slug=slug, defaults={**d, 'slug': slug})
        self.stdout.write('  [+] Articles de blog')

    def _create_page_seo(self):
        pages = [
            {'page_identifier': 'home',
             'meta_title_fr': 'VR Creation Company — Modélisation 3D, Visites Virtuelles & Captures 360°',
             'meta_title_en': 'VR Creation Company — 3D Modeling, Virtual Tours & 360° Captures',
             'meta_title_ar': 'في آر كرييشن — النمذجة ثلاثية الأبعاد والجولات الافتراضية والتقاط 360 درجة',
             'meta_description_fr': 'Agence spécialisée en création visuelle 3D, visites virtuelles et captures 360°. Sublimez vos projets immobiliers, retail et architecturaux.',
             'meta_description_en': 'Agency specializing in 3D visual creation, virtual tours and 360° captures. Enhance your real estate, retail and architectural projects.',
             'meta_description_ar': 'وكالة متخصصة في الإبداع البصري ثلاثي الأبعاد والجولات الافتراضية والتقاط 360 درجة.'},
            {'page_identifier': 'about',
             'meta_title_fr': 'À propos — VR Creation Company',
             'meta_title_en': 'About — VR Creation Company',
             'meta_title_ar': 'من نحن — في آر كرييشن',
             'meta_description_fr': 'Découvrez l\'équipe, les valeurs et la méthodologie de VR Creation Company. Une expertise pluridisciplinaire au service de vos projets visuels.',
             'meta_description_en': 'Discover the team, values and methodology of VR Creation Company. Multidisciplinary expertise serving your visual projects.',
             'meta_description_ar': 'اكتشف فريق وقيم ومنهجية في آر كرييشن.'},
            {'page_identifier': 'services',
             'meta_title_fr': 'Nos services — Modélisation 3D, Visites Virtuelles, Branding | VR Creation',
             'meta_title_en': 'Our Services — 3D Modeling, Virtual Tours, Branding | VR Creation',
             'meta_title_ar': 'خدماتنا — النمذجة ثلاثية الأبعاد، الجولات الافتراضية، العلامة التجارية',
             'meta_description_fr': 'Découvrez nos 6 expertises : modélisation 3D, visites virtuelles, captures 360°, branding, photographie et motion design.',
             'meta_description_en': 'Discover our 6 areas of expertise: 3D modeling, virtual tours, 360° captures, branding, photography and motion design.',
             'meta_description_ar': 'اكتشف مجالات خبرتنا الستة.'},
            {'page_identifier': 'portfolio',
             'meta_title_fr': 'Portfolio — Nos réalisations | VR Creation Company',
             'meta_title_en': 'Portfolio — Our Work | VR Creation Company',
             'meta_title_ar': 'معرض الأعمال — إنجازاتنا',
             'meta_description_fr': 'Explorez nos projets les plus emblématiques en immobilier, retail, architecture et événementiel.',
             'meta_description_en': 'Explore our most iconic projects in real estate, retail, architecture and events.',
             'meta_description_ar': 'استكشف مشاريعنا الأكثر شهرة.'},
            {'page_identifier': 'contact',
             'meta_title_fr': 'Contact — Parlons de votre projet | VR Creation Company',
             'meta_title_en': 'Contact — Let\'s Discuss Your Project | VR Creation Company',
             'meta_title_ar': 'اتصل بنا — لنتحدث عن مشروعك',
             'meta_description_fr': 'Contactez VR Creation Company pour discuter de votre projet 3D, visite virtuelle ou capture 360°. Réponse sous 24h.',
             'meta_description_en': 'Contact VR Creation Company to discuss your 3D project, virtual tour or 360° capture. Response within 24h.',
             'meta_description_ar': 'اتصل بنا لمناقشة مشروعك. رد خلال 24 ساعة.'},
            {'page_identifier': 'blog',
             'meta_title_fr': 'Blog — Actualités & Insights | VR Creation Company',
             'meta_title_en': 'Blog — News & Insights | VR Creation Company',
             'meta_title_ar': 'المدونة — أخبار ورؤى',
             'meta_description_fr': 'Tendances du secteur, coulisses de nos projets et conseils d\'experts sur la visualisation 3D et la réalité virtuelle.',
             'meta_description_en': 'Industry trends, behind-the-scenes of our projects and expert advice on 3D visualization and virtual reality.',
             'meta_description_ar': 'اتجاهات الصناعة وكواليس مشاريعنا ونصائح الخبراء.'},
        ]
        for p in pages:
            pid = p.pop('page_identifier')
            PageSEO.objects.get_or_create(page_identifier=pid, defaults={**p, 'page_identifier': pid})
        self.stdout.write('  [+] SEO des pages')
