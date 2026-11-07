import os
import shutil
from django.conf import settings
from django.db import migrations


def seed_promotions_and_fix_photos(apps, schema_editor):
    StrategicSuccess = apps.get_model('core', 'StrategicSuccess')
    Promotion = apps.get_model('core', 'Promotion')
    PromotionDeliverable = apps.get_model('core', 'PromotionDeliverable')
    PromotionComparison = apps.get_model('core', 'PromotionComparison')
    PromotionStep = apps.get_model('core', 'PromotionStep')
    Service = apps.get_model('services', 'Service')

    # 1. Fix StrategicSuccess images: clear dummy media path and ensure static fallback
    for item in StrategicSuccess.objects.all():
        item.image = ""
        item.save()

    # Also try to copy static strategic images to media/services if media dir exists
    try:
        media_services = os.path.join(settings.MEDIA_ROOT, 'services')
        os.makedirs(media_services, exist_ok=True)
        static_strategic = os.path.join(settings.BASE_DIR, 'static', 'img', 'strategic')
        if os.path.exists(static_strategic):
            for fname in os.listdir(static_strategic):
                if fname.endswith(('.jpg', '.png')):
                    shutil.copy(os.path.join(static_strategic, fname), os.path.join(media_services, fname))
    except Exception:
        pass

    # 2. Seed / Ensure Pack 1: Pack Spécial Promoteurs Débutants
    promo1, _ = Promotion.objects.get_or_create(slug="pack-promoteurs-debutants")
    promo1.title_fr = "Pack Spécial Promoteurs Débutants"
    promo1.title_en = "Special Pack for Beginner Developers"
    promo1.title_ar = "باقة خاصة بالمطورين العقاريين المبتدئين"
    promo1.badge_text_fr = "Offre de Lancement"
    promo1.badge_text_en = "Launch Offer"
    promo1.badge_text_ar = "عرض الإطلاق"
    promo1.headline_fr = "VENDEZ VOTRE PROJET IMMOBILIER AVANT MÊME DE POSER LA PREMIÈRE PIERRE"
    promo1.headline_en = "SELL YOUR REAL ESTATE PROJECT BEFORE EVEN LAYING THE FIRST STONE"
    promo1.headline_ar = "بع مشروعك العقاري حتى قبل وضع حجر الأساس"
    promo1.sub_headline_fr = "La solution 3D pensée pour les promoteurs débutants qui veulent commercialiser sur plan, sans budget d'agence."
    promo1.sub_headline_en = "The 3D solution designed for beginner developers who want to sell off-plan, without an agency budget."
    promo1.sub_headline_ar = "حل ثلاثي الأبعاد مصمم للمطورين المبتدئين الذين يرغبون في التسويق على المخطط، دون ميزانية وكالة."
    promo1.short_description_fr = "Le pack de commercialisation 3D tout-en-un conçu pour rassurer vos banques, séduire vos acheteurs et lancer vos ventes sur plan en un temps record."
    promo1.short_description_en = "The all-in-one 3D marketing pack designed to reassure your banks, attract your buyers and launch your off-plan sales in record time."
    promo1.short_description_ar = "باقة التسويق ثلاثية الأبعاد الكل في واحد والمصممة لطمأنة بنوككم، وجذب المشترين وإطلاق المبيعات على المخطط في وقت قياسي."
    promo1.problem_title_fr = "🏗️ LE PROBLÈME QUE VOUS CONNAISSEZ DÉJÀ"
    promo1.problem_title_en = "🏗️ THE PROBLEM YOU ALREADY KNOW"
    promo1.problem_title_ar = "🏗️ المشكلة التي تعرفها بالفعل"
    promo1.problem_text_fr = "Vous avez un terrain. Vous avez un plan. Vous avez un permis en cours. Mais comment convaincre un client d'investir dans un appartement... qui n'existe pas encore ?"
    promo1.problem_text_en = "You have a plot. You have a plan. You have a permit in progress. But how do you convince a client to invest in an apartment... that doesn't exist yet?"
    promo1.problem_text_ar = "لديك أرض. لديك مخطط. لديك رخصة قيد الدراسة. ولكن كيف تقنع العميل بالاستثمار في شقة... لم توجد بعد؟"
    promo1.solution_title_fr = "💡 LA SOLUTION : VENDRE SUR PLAN AVEC UN IMPACT VISUEL PROFESSIONNEL"
    promo1.solution_title_en = "💡 THE SOLUTION: SELL OFF-PLAN WITH A PROFESSIONAL VISUAL IMPACT"
    promo1.solution_title_ar = "💡 الحل: البيع على المخطط بتأثير بصري احترافي"
    promo1.solution_text_fr = "Avec VR Creation, transformez votre simple plan architectural en un outil de vente puissant, dès les premières semaines de votre projet — sans attendre la construction."
    promo1.solution_text_en = "With VR Creation, transform your simple architectural plan into a powerful sales tool, from the first weeks of your project — without waiting for construction."
    promo1.solution_text_ar = "مع VR Creation، حول مخططك المعماري البسيط إلى أداة مبيعات قوية، منذ الأسابيع الأولى لمشروعك — دون انتظار البناء."
    promo1.solution_quote_fr = "Donnez à vos clients la possibilité de se projeter, littéralement, dans leur futur bien."
    promo1.solution_quote_en = "Give your clients the opportunity to literally project themselves into their future property."
    promo1.solution_quote_ar = "امنح عملائك فرصة تخيل أنفسهم، حرفياً، في عقارهم المستقبلي."
    promo1.cta_title_fr = "🎁 OFFRE DE LANCEMENT — SPÉCIAL PREMIERS PROJETS"
    promo1.cta_title_en = "🎁 LAUNCH OFFER — SPECIAL FIRST PROJECTS"
    promo1.cta_title_ar = "🎁 عرض الإطلاق — خاص بالمشاريع الأولى"
    promo1.cta_text_fr = "Pour les promoteurs qui commercialisent leur premier ou deuxième projet immobilier, VR Creation propose un accompagnement dédié avec des tarifs optimisés."
    promo1.cta_text_en = "For developers marketing their first or second real estate project, VR Creation offers dedicated support with optimized rates."
    promo1.cta_text_ar = "للمطورين الذين يسوقون لمشروعهم العقاري الأول أو الثاني، تقدم VR Creation مواكبة مخصصة بأسعار محسنة."
    promo1.offer_price_fr = "Sur devis / Offre Spéciale"
    promo1.offer_price_en = "On request / Special Offer"
    promo1.offer_price_ar = "عند الطلب / عرض خاص"
    promo1.is_active = True
    promo1.is_featured = False
    promo1.is_customizable = True
    promo1.order = 2
    promo1.save()

    # Link services to Pack 1
    for slug in ['modelisation-3d', 'visites-virtuelles', 'captures-360', 'branding-visuel', 'photographie']:
        svc = Service.objects.filter(slug=slug).first()
        if svc:
            promo1.included_services.add(svc)

    if not promo1.deliverables.exists():
        deliv1 = [
            ("Modélisation 3D photoréaliste", "Photorealistic 3D Modeling", "نمذجة ثلاثية الأبعاد واقعية",
             "Votre plan devient un rendu 3D ultra-réaliste : façades, intérieurs, matériaux, lumières. Vos prospects visualisent le bien fini, pas des lignes techniques.",
             "Your plan becomes an ultra-realistic 3D render: facades, interiors, materials, lighting.",
             "يصبح مخططك رسماً ثلاثي الأبعاد فائق الواقعية: واجهات، تصميمات داخلية، مواد، وإضاءة.",
             'fas fa-drafting-compass'),
            ("Visite virtuelle interactive", "Interactive Virtual Tour", "جولة افتراضية تفاعلية",
             "Une visite 100% navigable, accessible sur mobile, tablette ou ordinateur. Vos clients visitent l'appartement avant le premier coup de pelle.",
             "A 100% navigable tour, accessible on mobile, tablet or computer.",
             "جولة تفاعلية بالكامل، يمكن الوصول إليها على الهاتف المحمول أو التابلت أو الكمبيوتر.",
             'fas fa-vr-cardboard'),
            ("Vidéo 3D immersive", "Immersive 3D Video", "فيديو ثلاثي الأبعاد غامر",
             "Une vidéo de survol du projet (extérieur + intérieur), parfaite pour les réseaux sociaux et vos rendez-vous commerciaux.",
             "A flyover video of the project (exterior + interior), perfect for social media.",
             "فيديو تحليق فوق المشروع (خارجي + داخلي)، ممتاز لمواقع التواصل الاجتماعي واجتماعات المبيعات.",
             'fas fa-film'),
            ("Branding & supports", "Branding & Marketing Assets", "الهوية البصرية والدعائم الإعلانية",
             "Logo du projet, plaquette commerciale, brochure de vente, affiches de chantier. Une identité visuelle crédible.",
             "Project logo, sales brochure, site banners. A credible visual identity.",
             "شعار المشروع، الكتيب التجاري، مطوية المبيعات، وملصقات الورشة.",
             'fas fa-palette'),
            ("Photo & captures 360°", "Photo & 360° Captures", "صور ولقطات 360 درجة",
             "Pour humaniser votre communication et rassurer vos prospects avec du contenu réel.",
             "To humanize your communication and reassure your prospects with real content.",
             "لإضفاء طابع إنساني على تواصلكم وطمأنة عملائكم المحتملين بمحتوى حقيقي.",
             'fas fa-camera')
        ]
        for idx, (t_fr, t_en, t_ar, d_fr, d_en, d_ar, icon) in enumerate(deliv1):
            PromotionDeliverable.objects.create(
                promotion=promo1, order=idx+1, icon=icon,
                title_fr=t_fr, title_en=t_en, title_ar=t_ar,
                description_fr=d_fr, description_en=d_en, description_ar=d_ar
            )

    # 3. Seed / Ensure Pack 2: Offre Performance
    promo2, _ = Promotion.objects.get_or_create(slug="offre-performance-commission")
    promo2.title_fr = "Offre Performance — Zéro Risque, 100% Résultat"
    promo2.title_en = "Performance Offer — Zero Risk, 100% Results"
    promo2.title_ar = "عرض الأداء — صفر مخاطرة، نتائج 100%"
    promo2.badge_text_fr = "Exclusif"
    promo2.badge_text_en = "Exclusive"
    promo2.badge_text_ar = "حصري"
    promo2.headline_fr = "VOUS NE PAYEZ RIEN. NOUS PRENONS TOUT EN CHARGE. VOUS NE PAYEZ QUE SI VOUS VENDEZ."
    promo2.headline_en = "YOU PAY NOTHING. WE HANDLE EVERYTHING. YOU ONLY PAY WHEN YOU SELL."
    promo2.headline_ar = "لا تدفع شيئاً. نتكفل بكل شيء. تدفع فقط عندما تبيع."
    promo2.sub_headline_fr = "VR Creation conçoit la meilleure stratégie marketing pour votre projet, déploie tous les outils nécessaires et gère même la relation avec vos acheteurs. Votre seul investissement : une commission sur chaque vente réussie."
    promo2.sub_headline_en = "VR Creation designs the best marketing strategy for your project, deploys all necessary tools, and even manages buyer relationships. Your only investment: a commission on each successful sale."
    promo2.sub_headline_ar = "VR Creation تصمم أفضل استراتيجية تسويق لمشروعك، تنشر جميع الأدوات اللازمة وتدير حتى العلاقة مع المشترين. استثمارك الوحيد: عمولة على كل عملية بيع ناجحة."
    promo2.short_description_fr = "Zéro investissement initial. Nous créons la stratégie, les visuels, le site, la gestion commerciale — et vous ne payez qu'une commission par vente réussie."
    promo2.short_description_en = "Zero upfront investment. We create the strategy, visuals, website, sales management — and you only pay a commission per successful sale."
    promo2.short_description_ar = "صفر استثمار مبدئي. نصمم الاستراتيجية، المرئيات، الموقع، إدارة المبيعات — ولا تدفع إلا عمولة عن كل بيع ناجح."
    promo2.problem_title_fr = "💰 LE DILEMME DU PROMOTEUR"
    promo2.problem_title_en = "💰 THE DEVELOPER'S DILEMMA"
    promo2.problem_title_ar = "💰 معضلة المطور العقاري"
    promo2.problem_text_fr = "Investir dans le marketing avant même d'avoir vendu un seul lot ? C'est le risque qui freine la plupart des promoteurs. Budget limité, incertitude du marché, peur de l'échec commercial — autant de raisons de ne pas franchir le pas."
    promo2.problem_text_en = "Investing in marketing before selling a single unit? That's the risk holding back most developers. Limited budget, market uncertainty, fear of commercial failure — all reasons not to take the leap."
    promo2.problem_text_ar = "الاستثمار في التسويق قبل بيع وحدة واحدة؟ هذا هو الخطر الذي يعيق معظم المطورين. ميزانية محدودة، عدم يقين السوق، الخوف من الفشل التجاري — كلها أسباب للتردد."
    promo2.solution_title_fr = "🚀 NOTRE MODÈLE : ZÉRO RISQUE, RÉSULTAT GARANTI"
    promo2.solution_title_en = "🚀 OUR MODEL: ZERO RISK, GUARANTEED RESULTS"
    promo2.solution_title_ar = "🚀 نموذجنا: صفر مخاطرة، نتائج مضمونة"
    promo2.solution_text_fr = "Nous ne vous vendons pas un pack de services. Nous investissons dans votre succès. Notre équipe analyse votre projet, conçoit la stratégie la plus efficace et déploie uniquement les outils qui feront la différence — site web, visites 3D, branding, réseaux sociaux, gestion des prospects et même la réponse aux acheteurs."
    promo2.solution_text_en = "We don't sell you a services package. We invest in your success. Our team analyzes your project, designs the most effective strategy and deploys only the tools that will make a difference."
    promo2.solution_text_ar = "لا نبيعك حزمة خدمات. نستثمر في نجاحك. فريقنا يحلل مشروعك، يصمم أفضل استراتيجية وينشر فقط الأدوات التي ستحدث الفرق."
    promo2.solution_quote_fr = "Vous ne prenez aucun risque. Si vous ne vendez pas, vous ne payez pas. C'est aussi simple que ça."
    promo2.solution_quote_en = "You take zero risk. If you don't sell, you don't pay. It's that simple."
    promo2.solution_quote_ar = "لا تتحمل أي مخاطرة. إذا لم تبع، لا تدفع. الأمر بهذه البساطة."
    promo2.cta_title_fr = "🤝 PRÊT À VENDRE SANS RISQUE ?"
    promo2.cta_title_en = "🤝 READY TO SELL WITHOUT RISK?"
    promo2.cta_title_ar = "🤝 مستعد للبيع بدون مخاطرة؟"
    promo2.cta_text_fr = "Contactez-nous pour une étude gratuite de votre projet. Nous évaluerons ensemble le potentiel commercial et vous proposerons une stratégie sur mesure — sans aucun engagement financier de votre part."
    promo2.cta_text_en = "Contact us for a free project assessment. We'll evaluate the commercial potential together and propose a tailored strategy — with no financial commitment on your part."
    promo2.cta_text_ar = "اتصل بنا لدراسة مجانية لمشروعك. سنقيم معاً الإمكانات التجارية ونقترح استراتيجية مصممة خصيصاً — بدون أي التزام مالي من جانبك."
    promo2.offer_price_fr = "0 DH — Commission sur vente uniquement"
    promo2.offer_price_en = "$0 — Commission on sale only"
    promo2.offer_price_ar = "0 درهم — عمولة على البيع فقط"
    promo2.commission_rate_fr = "Sur négociation"
    promo2.commission_rate_en = "Negotiable"
    promo2.commission_rate_ar = "قابلة للتفاوض"
    promo2.is_active = True
    promo2.is_featured = True
    promo2.is_customizable = False
    promo2.order = 1
    promo2.save()

    if not promo2.deliverables.exists():
        deliv2 = [
            ("Stratégie marketing sur mesure", "Custom Marketing Strategy", "استراتيجية تسويق مصممة خصيصاً",
             "Analyse approfondie de votre projet, de votre marché cible et de la concurrence.",
             "In-depth analysis of your project, target market and competition.",
             "تحليل معمق لمشروعك، والسوق المستهدف والمنافسة.",
             'fas fa-chess-queen'),
            ("Création de tous les supports visuels", "Full Visual Asset Creation", "إنشاء جميع الدعائم البصرية",
             "Site web, rendus 3D, visites virtuelles, vidéos, branding — nous déployons uniquement ce qui est nécessaire.",
             "Website, 3D renders, virtual tours, videos, branding.",
             "موقع إلكتروني، عروض ثلاثية الأبعاد، جولات افتراضية، فيديوهات، هوية بصرية.",
             'fas fa-layer-group'),
            ("Gestion des réseaux sociaux", "Social Media Management", "إدارة وسائل التواصل الاجتماعي",
             "Publication régulière, publicités ciblées, community management de A à Z.",
             "Regular posting, targeted ads, community management from A to Z.",
             "نشر منتظم، إعلانات مستهدفة، إدارة المجتمع من الألف إلى الياء.",
             'fas fa-share-alt'),
            ("Gestion commerciale & réponse aux acheteurs", "Sales Management & Buyer Response", "إدارة المبيعات والرد على المشترين",
             "Nous répondons à vos prospects, qualifions les leads et organisons les rendez-vous.",
             "We respond to your prospects, qualify leads and arrange appointments.",
             "نرد على عملائكم المحتملين، نقيّم العملاء المحتملين وننظم المواعيد.",
             'fas fa-headset'),
            ("Dashboard de suivi en temps réel", "Real-Time Tracking Dashboard", "لوحة تحكم للمتابعة في الوقت الحقيقي",
             "Visualisez vos leads, vos ventes, vos performances marketing et votre ROI.",
             "View your leads, sales, marketing performance and ROI.",
             "تابع عملاءك المحتملين، مبيعاتك، أداء التسويق والعائد على الاستثمار.",
             'fas fa-chart-line')
        ]
        for idx, (t_fr, t_en, t_ar, d_fr, d_en, d_ar, icon) in enumerate(deliv2):
            PromotionDeliverable.objects.create(
                promotion=promo2, order=idx+1, icon=icon,
                title_fr=t_fr, title_en=t_en, title_ar=t_ar,
                description_fr=d_fr, description_en=d_en, description_ar=d_ar
            )


def rollback(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_seed_strategic_successes'),
    ]

    operations = [
        migrations.RunPython(seed_promotions_and_fix_photos, rollback),
    ]
