"""
Seed promotions data with dynamic details, deliverables, comparisons, and steps.
Usage: python manage.py seed_promotions
"""
from django.core.management.base import BaseCommand
from apps.core.models import Promotion, PromotionDeliverable, PromotionComparison, PromotionStep


class Command(BaseCommand):
    help = 'Seeds database with a default Promotion package (Pack Spécial Promoteurs Débutants) and its associated sections.'

    def handle(self, *args, **options):
        self.stdout.write('— Seeding promotions —')

        # Clean existing promotions
        Promotion.objects.all().delete()

        # Create main promotion
        promo = Promotion(
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
            order=1
        )
        promo.save()

        # Create deliverables
        deliverables_data = [
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
                'description_fr': "Une vidéo de survol du projet (extérieur + intérieur), parfaite pour les réseaux sociaux et vos rendez-vous commerciaux. Capte l'attention en 10 secondes.",
                'description_en': "A flyover video of the project (exterior + interior), perfect for social media and your sales meetings. Captures attention in 10 seconds.",
                'description_ar': "فيديو تحليق فوق المشروع (خارجي + داخلي)، ممتاز لمواقع التواصل الاجتماعي واجتماعات المبيعات. يجذب الانتباه في 10 ثوانٍ.",
                'icon': 'fas fa-film'
            },
            {
                'title_fr': "Branding & supports",
                'title_en': "Branding & Marketing Assets",
                'title_ar': "الهوية البصرية والدعائم الإعلانية",
                'description_fr': "Logo du projet, plaquette commerciale, brochure de vente, affiches de chantier. Une identité visuelle crédible, même pour un premier projet.",
                'description_en': "Project logo, sales brochure, site banners. A credible visual identity, even for a first project.",
                'description_ar': "شعار المشروع، الكتيب التجاري، مطوية المبيعات، وملصقات الورشة. هوية بصرية موثوقة، حتى بالنسبة للمشروع الأول.",
                'icon': 'fas fa-palette'
            },
            {
                'title_fr': "Photo & captures 360°",
                'title_en': "Photo & 360° Captures",
                'title_ar': "صور ولقطات 360 درجة",
                'description_fr': "Pour humaniser votre communication et rassurer vos prospects avec du contenu réel, une fois le showroom ou le terrain prêt.",
                'description_en': "To humanize your communication and reassure your prospects with real content, once the showroom or site is ready.",
                'description_ar': "لإضفاء طابع إنساني على تواصلكم وطمأنة عملائكم المحتملين بمحتوى حقيقي، بمجرد جاهزية صالة العرض أو الموقع.",
                'icon': 'fas fa-camera'
            }
        ]
        for idx, item in enumerate(deliverables_data):
            PromotionDeliverable.objects.create(
                promotion=promo,
                title_fr=item['title_fr'],
                title_en=item['title_en'],
                title_ar=item['title_ar'],
                description_fr=item['description_fr'],
                description_en=item['description_en'],
                description_ar=item['description_ar'],
                icon=item['icon'],
                order=idx + 1
            )

        # Create comparisons
        comparisons_data = [
            {
                'feature_fr': "Visualisation",
                'feature_en': "Visualization",
                'feature_ar': "الرؤية البصرية",
                'without_vr_fr': "Plans 2D difficiles à comprendre pour le client",
                'without_vr_en': "Abstract 2D plans hard for client to understand",
                'without_vr_ar': "مخططات ثنائية الأبعاد يصعب على العميل فهمها",
                'with_vr_fr': "Rendus 3D immédiatement parlants",
                'with_vr_en': "Immediately talking 3D renders",
                'with_vr_ar': "رسوم ثلاثية الأبعاد واضحة على الفور",
            },
            {
                'feature_fr': "Projection client",
                'feature_en': "Client projection",
                'feature_ar': "التخيل لدى العميل",
                'without_vr_fr': "Prospects qui hésitent faute de projection",
                'without_vr_en': "Prospects hesitating due to lack of projection",
                'without_vr_ar': "عملاء محتملون يترددون لعدم قدرتهم على التخيل",
                'with_vr_fr': "Clients convaincus dès la première visite",
                'with_vr_en': "Clients convinced from the first visit",
                'with_vr_ar': "عملاء مقتنعون منذ الزيارة الأولى",
            },
            {
                'feature_fr': "Flexibilité",
                'feature_en': "Flexibility",
                'feature_ar': "المرونة",
                'without_vr_fr': "Maquette physique coûteuse et lente à modifier",
                'without_vr_en': "Physical model expensive and slow to modify",
                'without_vr_ar': "مجسم مادي مكلف وبطيء التعديل",
                'with_vr_fr': "Maquette numérique rapide et modifiable",
                'with_vr_en': "Digital model fast and modifiable",
                'with_vr_ar': "مجسم رقمي سريع وقابل للتعدil",
            },
            {
                'feature_fr': "Image de marque",
                'feature_en': "Brand image",
                'feature_ar': "صورة العلامة التجارية",
                'without_vr_fr': "Communication artisanale peu rassurante",
                'without_vr_en': "Basic communication not very reassuring",
                'without_vr_ar': "تواصل بسيط لا يبعث على الكثير من الطمأنينة",
                'with_vr_fr': "Identité visuelle premium digne d'une agence",
                'with_vr_en': "Premium visual identity matching top agencies",
                'with_vr_ar': "هوية بصرية راقية تليق بأكبر الوكالات",
            },
            {
                'feature_fr': "Ventes",
                'feature_en': "Sales speed",
                'feature_ar': "سرعة المبيعات",
                'without_vr_fr': "Ventes sur plan lentes et laborieuses",
                'without_vr_en': "Slow and tedious off-plan sales",
                'without_vr_ar': "مبيعات على المخطط بطيئة ومتعبة",
                'with_vr_fr': "Réservations accélérées, trésorerie sécurisée plus tôt",
                'with_vr_en': "Accelerated reservations, cash secured earlier",
                'with_vr_ar': "حجوزات متسارعة وتأمين السيولة في وقت مبكر",
            }
        ]
        for idx, item in enumerate(comparisons_data):
            PromotionComparison.objects.create(
                promotion=promo,
                feature_fr=item['feature_fr'],
                feature_en=item['feature_en'],
                feature_ar=item['feature_ar'],
                without_vr_fr=item['without_vr_fr'],
                without_vr_en=item['without_vr_en'],
                without_vr_ar=item['without_vr_ar'],
                with_vr_fr=item['with_vr_fr'],
                with_vr_en=item['with_vr_en'],
                with_vr_ar=item['with_vr_ar'],
                order=idx + 1
            )

        # Create steps
        steps_data = [
            {
                'title_fr': "Envoyez-nous votre plan",
                'title_en': "Send us your plan",
                'title_ar': "أرسل لنا مخططك",
                'description_fr': "Plan architectural, esquisse ou permis de construire — peu importe le stade d'avancement.",
                'description_en': "Architectural plan, sketch or building permit — no matter the stage of advancement.",
                'description_ar': "مخطط معماري، مسودة أو رخصة بناء — مهما كانت مرحلة تقدم المشروع."
            },
            {
                'title_fr': "Nous créons vos visuels",
                'title_en': "We build your visuals",
                'title_ar': "نصمم لك مرئياتك",
                'description_fr': "Rendus 3D, visite virtuelle et supports commerciaux réalisés sur mesure sous quelques jours.",
                'description_en': "3D renders, virtual tour and marketing materials custom made in a few days.",
                'description_ar': "عروض ثلاثية الأبعاد، جولة افتراضية ودعائم تسويقية مصممة خصيصاً في بضعة أيام."
            },
            {
                'title_fr': "Vous vendez",
                'title_en': "You start selling",
                'title_ar': "تبدأ في البيع",
                'description_fr': "Utilisez ces outils en rendez-vous client, sur les réseaux sociaux ou sur vos brochures pour réserver vos lots.",
                'description_en': "Use these tools in client meetings, on social media or in your brochures to book your units.",
                'description_ar': "استخدم هذه الأدوات في لقاءات عملائك، على شبكات التواصل الاجتماعي أو على مطوياتك لحجز وحداتك."
            }
        ]
        for idx, item in enumerate(steps_data):
            PromotionStep.objects.create(
                promotion=promo,
                title_fr=item['title_fr'],
                title_en=item['title_en'],
                title_ar=item['title_ar'],
                description_fr=item['description_fr'],
                description_en=item['description_en'],
                description_ar=item['description_ar'],
                order=idx + 1
            )

        self.stdout.write(self.style.SUCCESS('  [OK] Promotion "pack-promoteurs-debutants" and details seeded successfully'))
