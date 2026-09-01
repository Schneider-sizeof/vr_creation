"""
Seed promotions data with dynamic details, deliverables, comparisons, and steps.
Usage: python manage.py seed_promotions
"""
from django.core.management.base import BaseCommand
from apps.core.models import Promotion, PromotionDeliverable, PromotionComparison, PromotionStep
from apps.services.models import Service


class Command(BaseCommand):
    help = 'Seeds database with Promotion packages and their associated sections.'

    def handle(self, *args, **options):
        self.stdout.write('— Seeding promotions —')

        # Clean existing promotions
        Promotion.objects.all().delete()

        # ═══════════════════════════════════════════
        # PACK 1 — Pack Spécial Promoteurs Débutants
        # ═══════════════════════════════════════════
        promo1 = Promotion(
            title_fr="Pack Spécial Promoteurs Débutants",
            title_en="Special Pack for Beginner Developers",
            title_ar="باقة خاصة بالمطورين العقاريين المبتدئين",
            
            slug="pack-promoteurs-debutants",
            badge_text_fr="Offre de Lancement",
            badge_text_en="Launch Offer",
            badge_text_ar="عرض الإطلاق",
            
            headline_fr="VENDEZ VOTRE PROJET IMMOBILIER AVANT MÊME DE POSER LA PREMIÈRE PIERRE",
            headline_en="SELL YOUR REAL ESTATE PROJECT BEFORE EVEN LAYING THE FIRST STONE",
            headline_ar="بع مشروعك العقاري حتى قبل وضع حجر الأساس",
            
            sub_headline_fr="La solution 3D pensée pour les promoteurs débutants qui veulent commercialiser sur plan, sans budget d'agence.",
            sub_headline_en="The 3D solution designed for beginner developers who want to sell off-plan, without an agency budget.",
            sub_headline_ar="حل ثلاثي الأبعاد مصمم للمطورين المبتدئين الذين يرغبون في التسويق على المخطط، دون ميزانية وكالة.",
            
            short_description_fr="Le pack de commercialisation 3D tout-en-un conçu pour rassurer vos banques, séduire vos acheteurs et lancer vos ventes sur plan en un temps record.",
            short_description_en="The all-in-one 3D marketing pack designed to reassure your banks, attract your buyers and launch your off-plan sales in record time.",
            short_description_ar="باقة التسويق ثلاثية الأبعاد الكل في واحد والمصممة لطمأنة بنوككم، وجذب المشترين وإطلاق المبيعات على المخطط في وقت قياسي.",
            
            problem_title_fr="🏗️ LE PROBLÈME QUE VOUS CONNAISSEZ DÉJÀ",
            problem_title_en="🏗️ THE PROBLEM YOU ALREADY KNOW",
            problem_title_ar="🏗️ المشكلة التي تعرفها بالفعل",
            
            problem_text_fr="Vous avez un terrain. Vous avez un plan. Vous avez un permis en cours. Mais comment convaincre un client d'investir dans un appartement... qui n'existe pas encore ?",
            problem_text_en="You have a plot. You have a plan. You have a permit in progress. But how do you convince a client to invest in an apartment... that doesn't exist yet?",
            problem_text_ar="لديك أرض. لديك مخطط. لديك رخصة قيد الدراسة. ولكن كيف تقنع العميل بالاستثمار في شقة... لم توجد بعد؟",
            
            solution_title_fr="💡 LA SOLUTION : VENDRE SUR PLAN AVEC UN IMPACT VISUEL PROFESSIONNEL",
            solution_title_en="💡 THE SOLUTION: SELL OFF-PLAN WITH A PROFESSIONAL VISUAL IMPACT",
            solution_title_ar="💡 الحل: البيع على المخطط بتأثير بصري احترافي",
            
            solution_text_fr="Avec VR Creation, transformez votre simple plan architectural en un outil de vente puissant, dès les premières semaines de votre projet — sans attendre la construction.",
            solution_text_en="With VR Creation, transform your simple architectural plan into a powerful sales tool, from the first weeks of your project — without waiting for construction.",
            solution_text_ar="مع VR Creation، حول مخططك المعماري البسيط إلى أداة مبيعات قوية، منذ الأسابيع الأولى لمشروعك — دون انتظار البناء.",
            
            solution_quote_fr="Donnez à vos clients la possibilité de se projeter, littéralement, dans leur futur bien.",
            solution_quote_en="Give your clients the opportunity to literally project themselves into their future property.",
            solution_quote_ar="امنح عملائك فرصة تخيل أنفسهم، حرفياً، في عقارهم المستقبلي.",
            
            cta_title_fr="🎁 OFFRE DE LANCEMENT — SPÉCIAL PREMIERS PROJETS",
            cta_title_en="🎁 LAUNCH OFFER — SPECIAL FIRST PROJECTS",
            cta_title_ar="🎁 عرض الإطلاق — خاص بالمشاريع الأولى",
            
            cta_text_fr="Pour les promoteurs qui commercialisent leur premier ou deuxième projet immobilier, VR Creation propose un accompagnement dédié avec des tarifs optimisés.",
            cta_text_en="For developers marketing their first or second real estate project, VR Creation offers dedicated support with optimized rates.",
            cta_text_ar="للمطورين الذين يسوقون لمشروعهم العقاري الأول أو الثاني، تقدم VR Creation مواكبة مخصصة بأسعار محسنة.",
            
            offer_price_fr="Sur devis / Offre Spéciale",
            offer_price_en="On request / Special Offer",
            offer_price_ar="عند الطلب / عرض خاص",
            
            is_active=True,
            is_featured=False,
            is_customizable=True,
            order=2
        )
        promo1.save()

        # Link services to Pack 1
        service_slugs_pack1 = ['modelisation-3d', 'visites-virtuelles', 'captures-360', 'branding-visuel', 'photographie']
        for slug in service_slugs_pack1:
            try:
                svc = Service.objects.get(slug=slug)
                promo1.included_services.add(svc)
            except Service.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'  Service "{slug}" not found, skipping'))

        # Deliverables for Pack 1
        deliverables_data_1 = [
            {
                'title_fr': "Modélisation 3D photoréaliste",
                'title_en': "Photorealistic 3D Modeling",
                'title_ar': "نمذجة ثلاثية الأبعاد واقعية",
                'description_fr': "Votre plan devient un rendu 3D ultra-réaliste : façades, intérieurs, matériaux, lumières. Vos prospects visualisent le bien fini, pas des lignes techniques.",
                'description_en': "Your plan becomes an ultra-realistic 3D render: facades, interiors, materials, lighting. Your prospects visualize the finished property, not technical lines.",
                'description_ar': "يصبح مخططك رسماً ثلاثي الأبعاد فائق الواقعية: واجهات، تصميمات داخلية، مواد، وإضاءة. يتخيل عملائك المحتملون العقار مكتملاً، وليس خطوطاً تقنية.",
                'icon': 'fas fa-drafting-compass'
            },
            {
                'title_fr': "Visite virtuelle interactive",
                'title_en': "Interactive Virtual Tour",
                'title_ar': "جولة افتراضية تفاعلية",
                'description_fr': "Une visite 100% navigable, accessible sur mobile, tablette ou ordinateur. Vos clients visitent l'appartement avant le premier coup de pelle.",
                'description_en': "A 100% navigable tour, accessible on mobile, tablet or computer. Your clients visit the apartment before the first shovel stroke.",
                'description_ar': "جولة تفاعلية بالكامل، يمكن الوصول إليها على الهاتف المحمول أو التابلت أو الكمبيوتر. يزور عملائك الشقة قبل بدء الأشغال الأولى.",
                'icon': 'fas fa-vr-cardboard'
            },
            {
                'title_fr': "Vidéo 3D immersive",
                'title_en': "Immersive 3D Video",
                'title_ar': "فيديو ثلاثي الأبعاد غامر",
                'description_fr': "Une vidéo de survol du projet (extérieur + intérieur), parfaite pour les réseaux sociaux et vos rendez-vous commerciaux.",
                'description_en': "A flyover video of the project (exterior + interior), perfect for social media and your sales meetings.",
                'description_ar': "فيديو تحليق فوق المشروع (خارجي + داخلي)، ممتاز لمواقع التواصل الاجتماعي واجتماعات المبيعات.",
                'icon': 'fas fa-film'
            },
            {
                'title_fr': "Branding & supports",
                'title_en': "Branding & Marketing Assets",
                'title_ar': "الهوية البصرية والدعائم الإعلانية",
                'description_fr': "Logo du projet, plaquette commerciale, brochure de vente, affiches de chantier. Une identité visuelle crédible.",
                'description_en': "Project logo, sales brochure, site banners. A credible visual identity, even for a first project.",
                'description_ar': "شعار المشروع، الكتيب التجاري، مطوية المبيعات، وملصقات الورشة. هوية بصرية موثوقة.",
                'icon': 'fas fa-palette'
            },
            {
                'title_fr': "Photo & captures 360°",
                'title_en': "Photo & 360° Captures",
                'title_ar': "صور ولقطات 360 درجة",
                'description_fr': "Pour humaniser votre communication et rassurer vos prospects avec du contenu réel.",
                'description_en': "To humanize your communication and reassure your prospects with real content.",
                'description_ar': "لإضفاء طابع إنساني على تواصلكم وطمأنة عملائكم المحتملين بمحتوى حقيقي.",
                'icon': 'fas fa-camera'
            }
        ]
        for idx, item in enumerate(deliverables_data_1):
            PromotionDeliverable.objects.create(
                promotion=promo1, order=idx + 1, icon=item['icon'],
                title_fr=item['title_fr'], title_en=item['title_en'], title_ar=item['title_ar'],
                description_fr=item['description_fr'], description_en=item['description_en'], description_ar=item['description_ar'],
            )

        # Comparisons for Pack 1
        comparisons_data_1 = [
            ('Visualisation', 'Visualization', 'الرؤية البصرية',
             'Plans 2D difficiles à comprendre', 'Abstract 2D plans', 'مخططات ثنائية الأبعاد يصعب فهمها',
             'Rendus 3D immédiatement parlants', 'Immediately clear 3D renders', 'رسوم ثلاثية الأبعاد واضحة على الفور'),
            ('Projection client', 'Client projection', 'التخيل لدى العميل',
             'Prospects qui hésitent', 'Prospects hesitating', 'عملاء محتملون يترددون',
             'Clients convaincus dès la 1re visite', 'Clients convinced from first visit', 'عملاء مقتنعون منذ الزيارة الأولى'),
            ('Image de marque', 'Brand image', 'صورة العلامة التجارية',
             'Communication artisanale peu rassurante', 'Basic communication', 'تواصل بسيط لا يبعث على الطمأنينة',
             'Identité visuelle premium', 'Premium visual identity', 'هوية بصرية راقية'),
            ('Ventes', 'Sales speed', 'سرعة المبيعات',
             'Ventes sur plan lentes', 'Slow off-plan sales', 'مبيعات على المخطط بطيئة',
             'Réservations accélérées', 'Accelerated reservations', 'حجوزات متسارعة'),
        ]
        for idx, c in enumerate(comparisons_data_1):
            PromotionComparison.objects.create(
                promotion=promo1, order=idx + 1,
                feature_fr=c[0], feature_en=c[1], feature_ar=c[2],
                without_vr_fr=c[3], without_vr_en=c[4], without_vr_ar=c[5],
                with_vr_fr=c[6], with_vr_en=c[7], with_vr_ar=c[8],
            )

        # Steps for Pack 1
        steps_data_1 = [
            ('Envoyez-nous votre plan', 'Send us your plan', 'أرسل لنا مخططك',
             'Plan architectural, esquisse ou permis — peu importe le stade.', 'Architectural plan, sketch or permit.', 'مخطط معماري، مسودة أو رخصة بناء.'),
            ('Nous créons vos visuels', 'We build your visuals', 'نصمم لك مرئياتك',
             'Rendus 3D, visite virtuelle et supports commerciaux sur mesure.', '3D renders, virtual tour and marketing materials.', 'عروض ثلاثية الأبعاد، جولة افتراضية ودعائم تسويقية.'),
            ('Vous vendez', 'You start selling', 'تبدأ في البيع',
             'Utilisez ces outils pour réserver vos lots.', 'Use these tools to book your units.', 'استخدم هذه الأدوات لحجز وحداتك.'),
        ]
        for idx, s in enumerate(steps_data_1):
            PromotionStep.objects.create(
                promotion=promo1, order=idx + 1,
                title_fr=s[0], title_en=s[1], title_ar=s[2],
                description_fr=s[3], description_en=s[4], description_ar=s[5],
            )

        self.stdout.write(self.style.SUCCESS('  [OK] Pack 1 "Pack Promoteurs Débutants" seeded'))

        # ═══════════════════════════════════════════════════
        # PACK 2 — Offre Performance (Commission-Based)
        # ═══════════════════════════════════════════════════
        promo2 = Promotion(
            title_fr="Offre Performance — Zéro Risque, 100% Résultat",
            title_en="Performance Offer — Zero Risk, 100% Results",
            title_ar="عرض الأداء — صفر مخاطرة، نتائج 100%",
            
            slug="offre-performance-commission",
            badge_text_fr="Exclusif",
            badge_text_en="Exclusive",
            badge_text_ar="حصري",
            
            headline_fr="VOUS NE PAYEZ RIEN. NOUS PRENONS TOUT EN CHARGE. VOUS NE PAYEZ QUE SI VOUS VENDEZ.",
            headline_en="YOU PAY NOTHING. WE HANDLE EVERYTHING. YOU ONLY PAY WHEN YOU SELL.",
            headline_ar="لا تدفع شيئاً. نتكفل بكل شيء. تدفع فقط عندما تبيع.",
            
            sub_headline_fr="VR Creation conçoit la meilleure stratégie marketing pour votre projet, déploie tous les outils nécessaires et gère même la relation avec vos acheteurs. Votre seul investissement : une commission sur chaque vente réussie.",
            sub_headline_en="VR Creation designs the best marketing strategy for your project, deploys all necessary tools, and even manages buyer relationships. Your only investment: a commission on each successful sale.",
            sub_headline_ar="VR Creation تصمم أفضل استراتيجية تسويق لمشروعك، تنشر جميع الأدوات اللازمة وتدير حتى العلاقة مع المشترين. استثمارك الوحيد: عمولة على كل عملية بيع ناجحة.",
            
            short_description_fr="Zéro investissement initial. Nous créons la stratégie, les visuels, le site, la gestion commerciale — et vous ne payez qu'une commission par vente réussie.",
            short_description_en="Zero upfront investment. We create the strategy, visuals, website, sales management — and you only pay a commission per successful sale.",
            short_description_ar="صفر استثمار مبدئي. نصمم الاستراتيجية، المرئيات، الموقع، إدارة المبيعات — ولا تدفع إلا عمولة عن كل بيع ناجح.",
            
            problem_title_fr="💰 LE DILEMME DU PROMOTEUR",
            problem_title_en="💰 THE DEVELOPER'S DILEMMA",
            problem_title_ar="💰 معضلة المطور العقاري",
            
            problem_text_fr="Investir dans le marketing avant même d'avoir vendu un seul lot ? C'est le risque qui freine la plupart des promoteurs. Budget limité, incertitude du marché, peur de l'échec commercial — autant de raisons de ne pas franchir le pas.",
            problem_text_en="Investing in marketing before selling a single unit? That's the risk holding back most developers. Limited budget, market uncertainty, fear of commercial failure — all reasons not to take the leap.",
            problem_text_ar="الاستثمار في التسويق قبل بيع وحدة واحدة؟ هذا هو الخطر الذي يعيق معظم المطورين. ميزانية محدودة، عدم يقين السوق، الخوف من الفشل التجاري — كلها أسباب للتردد.",
            
            solution_title_fr="🚀 NOTRE MODÈLE : ZÉRO RISQUE, RÉSULTAT GARANTI",
            solution_title_en="🚀 OUR MODEL: ZERO RISK, GUARANTEED RESULTS",
            solution_title_ar="🚀 نموذجنا: صفر مخاطرة، نتائج مضمونة",
            
            solution_text_fr="Nous ne vous vendons pas un pack de services. Nous investissons dans votre succès. Notre équipe analyse votre projet, conçoit la stratégie la plus efficace et déploie uniquement les outils qui feront la différence — site web, visites 3D, branding, réseaux sociaux, gestion des prospects et même la réponse aux acheteurs. Tout est piloté depuis notre dashboard en temps réel.",
            solution_text_en="We don't sell you a services package. We invest in your success. Our team analyzes your project, designs the most effective strategy and deploys only the tools that will make a difference — website, 3D tours, branding, social media, lead management and even responding to buyers. Everything is tracked via our real-time dashboard.",
            solution_text_ar="لا نبيعك حزمة خدمات. نستثمر في نجاحك. فريقنا يحلل مشروعك، يصمم أفضل استراتيجية وينشر فقط الأدوات التي ستحدث الفرق — موقع إلكتروني، جولات ثلاثية الأبعاد، هوية بصرية، وسائل التواصل الاجتماعي، إدارة العملاء المحتملين وحتى الرد على المشترين.",
            
            solution_quote_fr="Vous ne prenez aucun risque. Si vous ne vendez pas, vous ne payez pas. C'est aussi simple que ça.",
            solution_quote_en="You take zero risk. If you don't sell, you don't pay. It's that simple.",
            solution_quote_ar="لا تتحمل أي مخاطرة. إذا لم تبع، لا تدفع. الأمر بهذه البساطة.",
            
            cta_title_fr="🤝 PRÊT À VENDRE SANS RISQUE ?",
            cta_title_en="🤝 READY TO SELL WITHOUT RISK?",
            cta_title_ar="🤝 مستعد للبيع بدون مخاطرة؟",
            
            cta_text_fr="Contactez-nous pour une étude gratuite de votre projet. Nous évaluerons ensemble le potentiel commercial et vous proposerons une stratégie sur mesure — sans aucun engagement financier de votre part.",
            cta_text_en="Contact us for a free project assessment. We'll evaluate the commercial potential together and propose a tailored strategy — with no financial commitment on your part.",
            cta_text_ar="اتصل بنا لدراسة مجانية لمشروعك. سنقيم معاً الإمكانات التجارية ونقترح استراتيجية مصممة خصيصاً — بدون أي التزام مالي من جانبك.",
            
            offer_price_fr="0 DH — Commission sur vente uniquement",
            offer_price_en="$0 — Commission on sale only",
            offer_price_ar="0 درهم — عمولة على البيع فقط",
            
            commission_rate_fr="Sur négociation",
            commission_rate_en="Negotiable",
            commission_rate_ar="قابلة للتفاوض",
            
            is_active=True,
            is_featured=True,
            is_customizable=False,
            order=1
        )
        promo2.save()

        # Deliverables for Pack 2
        deliverables_data_2 = [
            {
                'title_fr': "Stratégie marketing sur mesure",
                'title_en': "Custom Marketing Strategy",
                'title_ar': "استراتيجية تسويق مصممة خصيصاً",
                'description_fr': "Analyse approfondie de votre projet, de votre marché cible et de la concurrence. Nous concevons un plan d'action précis pour maximiser vos ventes.",
                'description_en': "In-depth analysis of your project, target market and competition. We design a precise action plan to maximize your sales.",
                'description_ar': "تحليل معمق لمشروعك، والسوق المستهدف والمنافسة. نصمم خطة عمل دقيقة لتعظيم مبيعاتك.",
                'icon': 'fas fa-chess-queen'
            },
            {
                'title_fr': "Création de tous les supports visuels",
                'title_en': "Full Visual Asset Creation",
                'title_ar': "إنشاء جميع الدعائم البصرية",
                'description_fr': "Site web, rendus 3D, visites virtuelles, vidéos, branding — nous déployons uniquement ce qui est nécessaire pour votre projet.",
                'description_en': "Website, 3D renders, virtual tours, videos, branding — we deploy only what's necessary for your project.",
                'description_ar': "موقع إلكتروني، عروض ثلاثية الأبعاد، جولات افتراضية، فيديوهات، هوية بصرية — ننشر فقط ما هو ضروري لمشروعك.",
                'icon': 'fas fa-layer-group'
            },
            {
                'title_fr': "Gestion des réseaux sociaux",
                'title_en': "Social Media Management",
                'title_ar': "إدارة وسائل التواصل الاجتماعي",
                'description_fr': "Publication régulière, publicités ciblées, community management — nous gérons votre présence en ligne de A à Z.",
                'description_en': "Regular posting, targeted ads, community management — we handle your online presence from A to Z.",
                'description_ar': "نشر منتظم، إعلانات مستهدفة، إدارة المجتمع — ندير تواجدك الرقمي من الألف إلى الياء.",
                'icon': 'fas fa-share-alt'
            },
            {
                'title_fr': "Gestion commerciale & réponse aux acheteurs",
                'title_en': "Sales Management & Buyer Response",
                'title_ar': "إدارة المبيعات والرد على المشترين",
                'description_fr': "Nous répondons à vos prospects, qualifions les leads et organisons les rendez-vous. Vous vous concentrez sur votre chantier.",
                'description_en': "We respond to your prospects, qualify leads and arrange appointments. You focus on your construction.",
                'description_ar': "نرد على عملائكم المحتملين، نقيّم العملاء المحتملين وننظم المواعيد. أنتم تركزون على البناء.",
                'icon': 'fas fa-headset'
            },
            {
                'title_fr': "Dashboard de suivi en temps réel",
                'title_en': "Real-Time Tracking Dashboard",
                'title_ar': "لوحة تحكم للمتابعة في الوقت الحقيقي",
                'description_fr': "Visualisez vos leads, vos ventes, vos performances marketing et votre ROI depuis une interface simple et intuitive.",
                'description_en': "View your leads, sales, marketing performance and ROI from a simple, intuitive interface.",
                'description_ar': "تابع عملاءك المحتملين، مبيعاتك، أداء التسويق والعائد على الاستثمار من واجهة بسيطة وبديهية.",
                'icon': 'fas fa-chart-line'
            },
        ]
        for idx, item in enumerate(deliverables_data_2):
            PromotionDeliverable.objects.create(
                promotion=promo2, order=idx + 1, icon=item['icon'],
                title_fr=item['title_fr'], title_en=item['title_en'], title_ar=item['title_ar'],
                description_fr=item['description_fr'], description_en=item['description_en'], description_ar=item['description_ar'],
            )

        # Comparisons for Pack 2
        comparisons_data_2 = [
            ('Investissement initial', 'Initial investment', 'الاستثمار المبدئي',
             'Budget marketing à avancer sans garantie', 'Marketing budget upfront with no guarantee', 'ميزانية تسويق مسبقة بدون ضمان',
             'Zéro investissement — on avance pour vous', 'Zero investment — we invest for you', 'صفر استثمار — نستثمر من أجلك'),
            ('Risque financier', 'Financial risk', 'المخاطرة المالية',
             'Perte si le marketing ne fonctionne pas', 'Loss if marketing doesn\'t work', 'خسارة إذا لم ينجح التسويق',
             'Zéro risque — paiement uniquement sur vente', 'Zero risk — pay only on sale', 'صفر مخاطرة — الدفع فقط عند البيع'),
            ('Gestion commerciale', 'Sales management', 'الإدارة التجارية',
             'Vous devez tout gérer vous-même', 'You must manage everything yourself', 'يجب عليك إدارة كل شيء بنفسك',
             'Nous gérons leads, prospects et rendez-vous', 'We handle leads, prospects and appointments', 'ندير العملاء المحتملين والمواعيد'),
            ('Stratégie', 'Strategy', 'الاستراتيجية',
             'Approche au hasard, sans plan clair', 'Random approach without clear plan', 'نهج عشوائي بدون خطة واضحة',
             'Stratégie sur mesure par nos experts', 'Custom strategy by our experts', 'استراتيجية مصممة من خبرائنا'),
            ('Suivi', 'Tracking', 'المتابعة',
             'Pas de visibilité sur les résultats', 'No visibility on results', 'عدم وضوح النتائج',
             'Dashboard temps réel avec KPIs clairs', 'Real-time dashboard with clear KPIs', 'لوحة تحكم بمؤشرات أداء واضحة'),
        ]
        for idx, c in enumerate(comparisons_data_2):
            PromotionComparison.objects.create(
                promotion=promo2, order=idx + 1,
                feature_fr=c[0], feature_en=c[1], feature_ar=c[2],
                without_vr_fr=c[3], without_vr_en=c[4], without_vr_ar=c[5],
                with_vr_fr=c[6], with_vr_en=c[7], with_vr_ar=c[8],
            )

        # Steps for Pack 2
        steps_data_2 = [
            ('Étude gratuite de votre projet', 'Free project assessment', 'دراسة مجانية لمشروعك',
             'Nous analysons votre projet, votre marché et évaluons le potentiel commercial.', 'We analyze your project, market and evaluate commercial potential.', 'نحلل مشروعك، سوقك ونقيم الإمكانات التجارية.'),
            ('Nous déployons la stratégie', 'We deploy the strategy', 'ننشر الاستراتيجية',
             'Création des visuels, mise en ligne, lancement des campagnes marketing — sans que vous ne dépensiez un centime.', 'Visual creation, launch, marketing campaigns — without you spending a cent.', 'إنشاء المرئيات، الإطلاق، حملات التسويق — بدون أن تنفق سنتيماً واحداً.'),
            ('Vous vendez, vous nous payez', 'You sell, you pay us', 'تبيع، تدفع لنا',
             'Commission uniquement sur les ventes réussies. Si vous ne vendez pas, vous ne payez rien.', 'Commission only on successful sales. If you don\'t sell, you pay nothing.', 'عمولة فقط على المبيعات الناجحة. إذا لم تبع، لا تدفع شيئاً.'),
        ]
        for idx, s in enumerate(steps_data_2):
            PromotionStep.objects.create(
                promotion=promo2, order=idx + 1,
                title_fr=s[0], title_en=s[1], title_ar=s[2],
                description_fr=s[3], description_en=s[4], description_ar=s[5],
            )

        self.stdout.write(self.style.SUCCESS('  [OK] Pack 2 "Offre Performance — Commission" seeded (FEATURED)'))
        self.stdout.write(self.style.SUCCESS('  [OK] All promotions seeded successfully'))
