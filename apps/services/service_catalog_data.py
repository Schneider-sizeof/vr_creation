"""
Service enrichment data catalog for VR Creation Company.
Provides detailed deliverables, tailored process workflows, turnaround ranges,
target audiences, and 5-6 comprehensive FAQs per service in FR, EN, and AR.
"""
from django.utils.translation import get_language

SERVICE_ENRICHMENT = {
    'modelisation-3d': {
        'turnaround': {
            'fr': "5 à 10 jours ouvrés selon la complexité volumétrique et le nombre de perspectives (TODO_OWNER: valider les délais moyens selon typologie de projet).",
            'en': "5 to 10 business days depending on volumetric complexity and number of perspectives (TODO_OWNER: validate turnaround times).",
            'ar': "من 5 إلى 10 أيام عمل حسب التعقيد الحجمي وعدد الزوايا البصرية (TODO_OWNER: تأكيد المواعيد حسب طبيعة المشروع).",
        },
        'target_audience': {
            'fr': "Promoteurs immobiliers VEFA, architectes d'intérieur, cabinets d'architecture et bureaux d'études à Tanger et dans le Nord du Maroc.",
            'en': "Off-plan (VEFA) real estate developers, interior designers, architecture firms, and engineering offices in Tanger and Northern Morocco.",
            'ar': "المطورون العقاريون (البيع على الخارطة)، مهندسو الديكور الداخلي، مكاتب الهندسة المعمارية والدراسات بطنجة وشمال المغرب.",
        },
        'deliverables': {
            'fr': [
                {"title": "Rendus Ultra-HD 4K (3840×2160 px)", "desc": "Perspectives intérieures et extérieures en haute résolution prêtes pour affichage écran et plaquettes commerciales."},
                {"title": "Fichiers Haute Définition 300 DPI", "desc": "Fichiers optimisés pour l'impression grand format : panneaux de chantier 4×3m, kakémonos et catalogues imprimés."},
                {"title": "Axonométries & Plans 3D texturés", "desc": "Vues écorchées et plans d'étages 3D détaillés pour permettre aux acquéreurs de saisir l'agencement des pièces."},
                {"title": "Exports multi-formats", "desc": "Livraison en formats JPEG, PNG 24-bit transparent et TIFF haute fidélité pour une intégration fluide sur tous vos supports."}
            ],
            'en': [
                {"title": "Ultra-HD 4K Renders (3840×2160 px)", "desc": "High-resolution interior and exterior perspectives ready for digital display and sales brochures."},
                {"title": "High-Resolution 300 DPI Print Files", "desc": "Files optimized for large-scale printing: 4×3m construction hoardings, roll-ups, and sales catalogs."},
                {"title": "Axonometric & 3D Floor Plans", "desc": "Cutaway views and detailed 3D floor layouts helping buyers instantly grasp spatial arrangements."},
                {"title": "Multi-Format Deliverables", "desc": "Delivered in JPEG, transparent 24-bit PNG, and TIFF formats for seamless integration across all marketing assets."}
            ],
            'ar': [
                {"title": "تصاميم ثلاثية الأبعاد بدقة Ultra-HD 4K (3840×2160 بكسل)", "desc": "مشاهد داخلية وخارجية فائقة الدقة جاهزة للشاشات والكتيبات الترويجية."},
                {"title": "ملفات عالية الدقة 300 DPI للطباعة", "desc": "ملفات مجهزة للطباعة الكبيرة: لوحات ورش البناء 4×3م، اللوحات الإعلانية والكتالوجات."},
                {"title": "مخططات طوابق ثلاثية الأبعاد ومنظور أكسونومتري", "desc": "مخططات مجسمة ومقطوعة تتيح للمشترين استيعاب توزيع الغرف والمساحات بوضوح."},
                {"title": "صيغ تصدير متعددة", "desc": "تسليم بصيغ JPEG و PNG شفاف و TIFF لتكامل سلس مع كافة وسائطكم التسويقية."}
            ]
        },
        'process': {
            'fr': [
                {"step": 1, "title": "Cahier des charges & Plans 2D", "desc": "Réception des fichiers DWG, coupes, façades et planches d'intentions décoratives ou matériaux."},
                {"step": 2, "title": "Modélisation géométrique & Cadrages", "desc": "Construction précise des volumes 3D et sélection concertée des angles de vue stratégiques."},
                {"step": 3, "title": "Texturation PBR & Éclairage réaliste", "desc": "Application des matières réalistes (marbre, bois, zelliges, enduits) et calage de l'ensoleillement méditerranéen."},
                {"step": 4, "title": "Validation intermédiaire basse définition", "desc": "Présentation des rendus d'étape pour ajuster textures, mobilier et aménagement avant le calcul final."},
                {"step": 5, "title": "Calcul final 4K & Post-production", "desc": "Rendu haute définition, colorimétrie soignée, intégration d'arrière-plans réels de Tanger et livraison."}
            ],
            'en': [
                {"step": 1, "title": "Briefing & 2D Architectural Plans", "desc": "Collection of DWG blueprints, elevations, sections, and material/moodboard specifications."},
                {"step": 2, "title": "3D Geometry & Camera Placement", "desc": "Precise volume modeling and strategic selection of optimal viewpoint cameras."},
                {"step": 3, "title": "PBR Texturing & Realistic Lighting", "desc": "Applying physically-based materials (marble, woodwork, zellige) and balanced natural sunlight."},
                {"step": 4, "title": "Draft Review & Client Iteration", "desc": "Presentation of draft renders to fine-tune furnishings, lighting, and materials before final calculation."},
                {"step": 5, "title": "Final 4K Rendering & Post-Production", "desc": "Ultra-HD computation, detailed color correction, insertion of genuine Tanger environments, and handoff."}
            ],
            'ar': [
                {"step": 1, "title": "استلام المخططات المعمارية 2D", "desc": "استلام ملفات DWG والواجهات والقطاعات مع قائمة المواد والتشطيبات المرغوبة."},
                {"step": 2, "title": "البناء المجسم وتحديد زوايا الكاميرا", "desc": "تشييد الكتل المعمارية بدقة متناهية واختيار أفضل زوايا الرؤية الاستراتيجية."},
                {"step": 3, "title": "إكساء المواد والإضاءة الواقعية", "desc": "تطبيق خامات واقعية (رخام، خشب، زليج مغربي) وضبط أشعة الشمس الساحلية الطبيعية."},
                {"step": 4, "title": "مراجعة أولية وتعديلات", "desc": "عرض مسودة التصميم لتعديل الأثاث واللمسات التزيينية قبل معالجة الدقة العالية."},
                {"step": 5, "title": "المعالجة النهائية 4K واللمسات الفنية", "desc": "توليد الصور بدقة فائقة وضبط الألوان ودمج المناظر الحقيقية لطنجة ثم التسليم النهائي."}
            ]
        },
        'faqs': {
            'fr': [
                {"q": "Quels documents sont nécessaires pour démarrer une modélisation 3D ?", "a": "Nous avons besoin des plans architecturaux 2D en format DWG ou PDF vectoriel (plans de masse, distributions, coupes et façades), ainsi que des indications sur les matériaux, teintes et finitions souhaitées."},
                {"q": "Quels sont les délais habituels de livraison des perspectives 3D à Tanger ?", "a": "Pour un pack de 3 à 5 perspectives intérieures ou extérieures, comptez entre 5 et 10 jours ouvrés avec une étape intermédiaire de validation. Les projets d'envergure font l'objet d'un planning jalonné."},
                {"q": "Les rendus 3D sont-ils utilisables pour l'impression grand format de panneaux de chantier ?", "a": "Absolument. Nos rendus sont exportés en Ultra-HD 4K à 300 DPI, garantissant une netteté irréprochable pour les affichages 4×3 mètres, les bâches publicitaires et les catalogues de vente."},
                {"q": "Combien de cycles de modifications sont inclus dans votre prestation ?", "a": "Chaque commande intègre systématiquement deux cycles de retouches pour ajuster les matières, la disposition du mobilier et les éclairages selon vos retours."},
                {"q": "Intégrez-vous l'environnement réel de Tanger autour du bâtiment ?", "a": "Oui, nous pouvons intégrer les véritables vues panoramiques (baie de Tanger, détroit de Gibraltar, forêt de Rmilat) par prise de vue drone ou photographie sur site."},
                {"q": "Fournissez-vous également des plans 3D axonométriques ?", "a": "Oui, nous modélisons des plans de masse 3D et des axonométries écorchées qui facilitent grandement la compréhension des volumes pour les futurs acquéreurs."}
            ],
            'en': [
                {"q": "What blueprints are required to start a 3D modeling project?", "a": "We require 2D CAD drawings (DWG or vector PDF format) including site plans, floor plans, sections, and facades, alongside your desired materials, colors, and interior design guidelines."},
                {"q": "What is the typical delivery timeframe for 3D renderings in Tanger?", "a": "A standard package of 3 to 5 interior or exterior views is typically delivered within 5 to 10 business days, including a midway review checkpoint."},
                {"q": "Are the 3D renders suitable for large construction site hoardings?", "a": "Yes. Our renders are exported in Ultra-HD 4K at 300 DPI, ensuring crisp sharpness on 4×3m billboards, hoardings, and premium sales brochures."},
                {"q": "How many revision rounds are included in the quote?", "a": "Every project includes two structured review cycles to adjust textures, furniture layout, and lighting conditions to your exact requirements."},
                {"q": "Can you incorporate Tanger's real background landscape?", "a": "Yes, we can blend genuine local surroundings—such as Tanger Bay, Gibraltar views, or the Cap Spartel coastline—using on-site photography or licensed drone footage."},
                {"q": "Do you also provide 3D cutaway floor plans?", "a": "Yes, we create textured 3D floor plans and axonometric views that allow prospective buyers to intuitively grasp apartment layout and circulation."}
            ],
            'ar': [
                {"q": "ما هي الوثائق المطلوبة لبدء النمذجة ثلاثية الأبعاد؟", "a": "نحتاج إلى المخططات المعمارية 2D بصيغة DWG أو PDF (مخطط الكتلة، التوزيعات، الواجهات والمقاطع) مع بيان المواد والألوان والتشطيبات المطلوبة."},
                {"q": "ما هي المواعيد المعتادة لتسليم التصاميم ثلاثية الأبعاد في طنجة؟", "a": "تتراوح المدة عادة بين 5 و 10 أيام عمل لحزمة من 3 إلى 5 مناظر داخلية أو خارجية، مع مرحلة مراجعة أولية لضمان الدقة."},
                {"q": "هل تصلح الصور الناتجة للطباعة الإعلانية الكبيرة في ورش البناء؟", "a": "بالتأكيد، تُسلَّم التصاميم بدقة 4K وبمعيار 300 DPI لضمان وضوح فائق على اللوحات الإعلانية الضخمة 4×3م وكتيبات التسويق الفاخرة."},
                {"q": "كم عدد جولات التعديل المشمولة في العرض؟", "a": "يتضمن كل مشروع جولتين من التعديلات لتنقيح الخامات، توزيع الأثاث، ومطابقة زوايا الإضاءة وفق ملاحظاتكم."},
                {"q": "هل يمكن دمج المنظر الحقيقي لمدينة طنجة في الخلفية؟", "a": "نعم، نلتقط صوراً حقيقية لخليج طنجة، مضيق جبل طارق، أو غابة الرميلات بواسطة الدرون لدمجها بدقة تامة خلف النوافذ والتراسات."},
                {"q": "هل تقدمون مخططات 3D مجسمة للشقق (Axonometry)؟", "a": "نعم، نصمم مخططات ثلاثية الأبعاد مقطوعة توضح توزيع الغرف بدقة وتساعد الزبناء على تخيل استغلال المساحة."}
            ]
        },
        'related_services': ['visites-virtuelles', 'animation-motion-design', 'captures-360'],
        'related_projects': ['residence-malabata-tanger', 'villa-californie-tanger']
    },
    'visites-virtuelles': {
        'turnaround': {
            'fr': "7 à 12 jours ouvrés pour une visite virtuelle 3D sur plan complète (TODO_OWNER: ajuster selon nombre de pièces et options interactives).",
            'en': "7 to 12 business days for a complete off-plan 3D virtual tour (TODO_OWNER: adjust based on room count and interactive features).",
            'ar': "من 7 إلى 12 يوم عمل للجولة الافتراضية ثلاثية الأبعاد على الخارطة (TODO_OWNER: تأكيد المدة حسب عدد الغرف والخصائص التفاعلية).",
        },
        'target_audience': {
            'fr': "Promoteurs immobiliers commercialisant en VEFA, résidences hôtelières, agences immobilières de prestige et architectes dans le Nord du Maroc.",
            'en': "Off-plan real estate developers, hotel residences, premium property brokers, and architects across Northern Morocco.",
            'ar': "شركات التطوير العقاري للمشاريع قيد الإنجاز (VEFA)، المنتجعات الفندقية، والوكالات العقارية الراقية بشمال المغرب.",
        },
        'deliverables': {
            'fr': [
                {"title": "Application Web interactive autonome", "desc": "Visite accessible sans installation, compatible tous navigateurs (Chrome, Safari, Firefox, Edge) et casques VR."},
                {"title": "Lecteur responsive mobile & tablette", "desc": "Navigation tactile ultra-fluide avec gyroscope et rotation 360° pour les acheteurs sur smartphone."},
                {"title": "Points d'information interactifs (Hotspots)", "desc": "Fiches techniques intégrées : dimensions, matériaux, options de personnalisation et formulaires de contact."},
                {"title": "Code d'intégration Iframe & Liens partageables", "desc": "Code prêt à insérer sur votre site internet et liens courts dédiés pour vos campagnes WhatsApp et réseaux sociaux."}
            ],
            'en': [
                {"title": "Standalone Interactive Web App", "desc": "Seamless browser-based tour requiring zero downloads, compatible with desktop, mobile, and VR headsets."},
                {"title": "Mobile & Tablet Responsive Player", "desc": "Ultra-smooth touch navigation featuring gyroscope steering and 360° orbital panoramas."},
                {"title": "Interactive Hotspots & Info Tags", "desc": "Embedded technical cards: room dimensions, finish options, brochure downloads, and direct inquiry forms."},
                {"title": "Embeddable Iframe Code & Share Links", "desc": "Plug-and-play iframe snippet for your website plus direct short links for WhatsApp and social campaigns."}
            ],
            'ar': [
                {"title": "تطبيق ويب تفاعلي مباشر", "desc": "جولة افتراضية تعمل مباشرة عبر المتصفح دون تحميل أي برنامج، متوافقة مع نظارات الواقع الافتراضي VR."},
                {"title": "مشغل متجاوب للهواتف والأجهزة اللوحية", "desc": "تجربة لمسية فائقة السلاسة تدعم مستشعر الحركة (Gyroscope) بزاوية 360 درجة."},
                {"title": "نقاط تفاعلية ذكية (Hotspots)", "desc": "نوافذ معلوماتية داخل الجولة: قياسات المساحات، أنواع التشطيبات، وروابط حجز المواعيد."},
                {"title": "كود تضمين Iframe وروابط مباشرة", "desc": "كود جاهز للتثبيت على موقعكم الإلكتروني وروابط قصيرة مخصصة للمشاركة عبر واتساب والإعلانات."}
            ]
        },
        'process': {
            'fr': [
                {"step": 1, "title": "Scénarisation du parcours visiteur", "desc": "Définition des points de vue clés (entrée, salon, suite parentale, terrasse) et de l'arborescence de visite."},
                {"step": 2, "title": "Modélisation 3D & Panoramas 360°", "desc": "Génération des panoramas équirectangulaires 8K photoréalistes pour chaque station de visite."},
                {"step": 3, "title": "Programmation de l'interface & Hotspots", "desc": "Intégration de la charte graphique du promoteur, du plan de masse interactif et des fiches descriptives."},
                {"step": 4, "title": "Optimisation multi-écrans & Temps de chargement", "desc": "Compression intelligente pour garantir un affichage instantané même en connexion 4G mobile au Maroc."},
                {"step": 5, "title": "Mise en ligne & Accompagnement technique", "desc": "Hébergement sur CDN haute performance, fourniture des codes d'intégration et QR codes pour vos brochures."}
            ],
            'en': [
                {"step": 1, "title": "Visitor Journey Mapping", "desc": "Selecting key vantage points (lobby, living room, master suite, terrace) and navigation flow."},
                {"step": 2, "title": "3D Modeling & 8K Equirectangular Panoramas", "desc": "Computing photorealistic 8K spherical panoramas for each designated viewpoint."},
                {"step": 3, "title": "Interface Branding & Hotspot Integration", "desc": "Embedding your corporate identity, interactive mini-map, specifications, and lead generation triggers."},
                {"step": 4, "title": "Cross-Device & Mobile Speed Optimization", "desc": "High-efficiency asset compression ensuring instantaneous loading across mobile 4G/5G networks."},
                {"step": 5, "title": "Hosting, Deployment & Marketing Assets", "desc": "CDN deployment, iframe code handoff, and branded QR codes ready for print collateral."}
            ],
            'ar': [
                {"step": 1, "title": "تخطيط مسار الزائر الافتراضي", "desc": "تحديد محطات الوقوف الرئيسية (المدخل، الصالون، الجناح الرئيسي، التراس) وهندسة التنقل."},
                {"step": 2, "title": "النمذجة وتوليد بانوراما 360° بدقة 8K", "desc": "معالجة مناظر كروية فائقة الواقعية تغطي كامل أرجاء العقار بزاوية 360 درجة."},
                {"step": 3, "title": "برمجة الواجهة التفاعلية والنقاط الإرشادية", "desc": "تضمين هوية المشروع، المخطط المصغر، ونوافذ التفاصيل واستمارات التواصل المباشر."},
                {"step": 4, "title": "التحسين للأجهزة المحمولة وسرعة التصفح", "desc": "ضغط تقني ذكي لضمان فتح الجولة في ثوانٍ معدودة عبر شبكات الهاتف في المغرب."},
                {"step": 5, "title": "النشر والاستضافة والتسليم", "desc": "استضافة سريعة على شبكة CDN وتزويدكم بأكواد التضمين ورموز QR للكتيبات المطبوعة."}
            ]
        },
        'faqs': {
            'fr': [
                {"q": "Quelle est la différence entre une visite 3D sur plan et une capture 360° réelle ?", "a": "La visite 3D sur plan est modélisée numériquement avant la construction pour la vente en VEFA. La capture 360° réelle est réalisée sur place à l'aide de caméras et scanners dans un espace déjà bâti ou aménagé."},
                {"q": "Les visiteurs ont-ils besoin d'installer une application pour explorer la visite ?", "a": "Non. La visite s'ouvre instantanément dans n'importe quel navigateur web sur smartphone, tablette ou ordinateur grâce aux technologies HTML5 et WebGL."},
                {"q": "Peut-on intégrer la visite virtuelle directement dans notre site web ?", "a": "Oui, nous vous remettons une ligne de code iframe prête à copier-coller sur votre site, compatible avec tous les CMS (WordPress, Django, Webflow, etc.)."},
                {"q": "La visite est-elle compatible avec les casques de réalité virtuelle ?", "a": "Oui, nos visites intègrent un mode VR immersif à 1 clic, compatible avec les casques Meta Quest, HTC Vive, Pico ainsi que les masques VR pour smartphone."},
                {"q": "Peut-on ajouter un plan de masse interactif avec radar d'orientation ?", "a": "Tout à fait. Un mini-plan cliquable est incrusté à l'écran, indiquant précisément au visiteur la pièce où il se trouve et la direction de son regard."},
                {"q": "Comment les acheteurs basés à l'étranger (MRE) consultent-ils la visite ?", "a": "Vous pouvez leur transmettre un lien direct WhatsApp ou par e-mail. Ils peuvent ainsi explorer le bien comme s'ils étaient sur place à Tanger, ce qui facilite les décisions d'achat à distance."}
            ],
            'en': [
                {"q": "What is the difference between an off-plan 3D tour and a real 360° capture?", "a": "An off-plan 3D virtual tour is built from architectural plans before construction begins, ideal for VEFA pre-sales. Real 360° capture is filmed on location in already built physical spaces."},
                {"q": "Do visitors need to download an app or software?", "a": "No downloads are required. The tour launches instantly within any modern browser on phones, tablets, or laptops using HTML5 and WebGL."},
                {"q": "Can we embed the virtual tour directly onto our corporate website?", "a": "Yes, we provide a clean, responsive iframe snippet that works seamlessly across all CMS platforms (WordPress, Django, Webflow, custom)."},
                {"q": "Is the experience compatible with VR headsets?", "a": "Yes, our player features a native one-click WebXR mode compatible with Meta Quest, Pico, and mobile VR viewers."},
                {"q": "Can you include an interactive mini-map with orientation radar?", "a": "Yes, a clickable floor layout can be embedded, indicating the user's active location and direction of gaze in real time."},
                {"q": "How does this assist international buyers and the Moroccan diaspora (MRE)?", "a": "You can share a lightweight link via WhatsApp or email, allowing diaspora investors in Europe or North America to inspect every room remotely with total confidence."}
            ],
            'ar': [
                {"q": "ما الفرق بين الجولة ثلاثية الأبعاد على الخارطة والتصوير الواقعي 360°؟", "a": "الجولة 3D على الخارطة تُبنى حاسوبياً قبل انطلاق البناء لخدمة مشاريع البيع قيد الإنجاز (VEFA)، بينما التصوير الواقعي 360° يُلتقط بكاميرات خاصة في عقارات مشيدة ومؤثثة بالفعل."},
                {"q": "هل يحتاج الزبون إلى تحميل أي تطبيق لفتح الجولة؟", "a": "لا، تعمل الجولة مباشرة وبسرعة في متصفحات الهواتف والحواسب دون الحاجة لأي تطبيق إضافي بفضل تقنيات الويب الحديثة."},
                {"q": "هل يمكن دمج الجولة داخل موقعنا الإلكتروني؟", "a": "نعم، نقدم لكم كود تضمين Iframe جاهزاً للنسخ واللصق على موقعكم ليعمل بتوافق تام مع مختلف منصات الويب."},
                {"q": "هل تدعم الجولة نظارات الواقع الافتراضي VR؟", "a": "نعم، تتيح الجولة وضع VR بنقرة واحدة لتجربة انغماس كامل عبر نظارات Meta Quest أو النظارات المخصصة للهواتف."},
                {"q": "هل يتوفر مخطط تفاعلي مصغر يبين موقع الزائر؟", "a": "نعم، ندمج مخططاً تفاعلياً يُظهر الغرفة التي يقف فيها الزائر واتجاه نظره لتسهيل التنقل داخل العقار."},
                {"q": "كيف تفيد الجولة الافتراضية في استقطاب مغاربة العالم والمستثمرين؟", "a": "يمكنكم إرسال الرابط المباشر عبر واتساب لتمكين أفراد الجالية في أوروبا وأمريكا من معاينة تفاصيل العقار بدقة واتخاذ قرار الشراء عن بُعد."}
            ]
        },
        'related_services': ['modelisation-3d', 'captures-360', 'lead-generation'],
        'related_projects': ['residence-malabata-tanger', 'concept-store-tanger']
    },
    'captures-360': {
        'turnaround': {
            'fr': "3 à 5 jours ouvrés après le tournage sur site à Tanger ou dans le Nord (TODO_OWNER: confirmer délais de post-traitement HDR).",
            'en': "3 to 5 business days after on-site capture in Tanger or Northern Morocco (TODO_OWNER: confirm HDR processing turnaround).",
            'ar': "من 3 إلى 5 أيام عمل بعد جلسة التصوير الميداني بطنجة أو الشمال (TODO_OWNER: تأكيد مواعيد المعالجة التقنية).",
        },
        'target_audience': {
            'fr': "Boutiques, showrooms de mobilier, hôtels, restaurants, galeries d'art, cliniques et établissements recevant du public à Tanger, Tétouan et Asilah.",
            'en': "Retail stores, furniture showrooms, boutique hotels, restaurants, art galleries, private clinics, and commercial spaces across Tanger, Tétouan, and Asilah.",
            'ar': "المحلات التجارية، صالات عرض الأثاث، الفنادق، المطاعم، صالات العرض الفنية، والمصحات بطنجة وتطوان وأصيلها.",
        },
        'deliverables': {
            'fr': [
                {"title": "Visite 360° réelle HDR haute résolution", "desc": "Prises de vues panoramiques nettes même en forts contrastes de luminosité."},
                {"title": "Intégration Google Street View & Google Business", "desc": "Publication directe sur votre fiche Google Maps pour booster votre référencement local à Tanger."},
                {"title": "Hotspots multimédias cliquables", "desc": "Incrustation de liens vers votre menu, catalogue produits, vidéo de présentation ou réservation."},
                {"title": "Photos panoramiques 360° pour Facebook & Réseaux", "desc": "Fichiers panoramiques natifs pour publication immersive sur les réseaux sociaux."}
            ],
            'en': [
                {"title": "High-Resolution HDR 360° Tour", "desc": "Crisp panoramic captures optimized for dynamic range across varied interior lighting."},
                {"title": "Google Street View & Maps Publishing", "desc": "Direct integration into your Google Business Profile to elevate local SEO in Tanger."},
                {"title": "Interactive Multimedia Hotspots", "desc": "Embed links to menus, product catalogs, promo videos, or direct reservation engines."},
                {"title": "Social-Ready 360° Panoramas", "desc": "Native spherical photo files ready for interactive publishing on Facebook and social media."}
            ],
            'ar': [
                {"title": "جولة 360° حقيقية بتقنية HDR فائقة الوضوح", "desc": "لقطات بانورامية نقية ومتوازنة الإضاءة في كافة الأركان والزوايا الداخلية."},
                {"title": "الربط مع خرائط جوجل Google Street View", "desc": "نشر الجولة على ملفكم في خرائط جوجل لتعزيز ظهوركم في نتائج البحث المحلي بطنجة."},
                {"title": "نقاط تفاعلية للوسائط المتعددة", "desc": "إضافة روابط لقوائم الطعام، كتالوجات المنتجات، أو أزرار الحجز المباشر داخل الجولة."},
                {"title": "صور بانورامية جاهزة لشبكات التواصل الاجتماعي", "desc": "ملفات 360 درجة متوافقة مع منشورات فيسبوك التفاعلية لزيادة تفاعل المتابعين."}
            ]
        },
        'process': {
            'fr': [
                {"step": 1, "title": "Repérage & Préparation des lieux", "desc": "Conseils d'agencement et choix des créneaux horaires à luminosité optimale pour votre établissement."},
                {"step": 2, "title": "Captation sur site par scanner & caméras HDR", "desc": "Séance de prise de vue 360° méthodique sans interrompre l'activité de vos clients."},
                {"step": 3, "title": "Assemblage des panoramas & Retouche chromatique", "desc": "Stitching de précision, suppression des trépieds et égalisation harmonieuse des lumières."},
                {"step": 4, "title": "Scénarisation & Hotspots interactifs", "desc": "Ajout des points d'intérêt, menus, liens e-commerce et éléments de votre identité visuelle."},
                {"step": 5, "title": "Publication & Intégration Google Street View", "desc": "Mise en ligne, synchronisation Google Maps et fourniture des liens web et iframes."}
            ],
            'en': [
                {"step": 1, "title": "Pre-Shoot Planning & Staging", "desc": "Lighting assessment and space staging recommendations to showcase your premises at their best."},
                {"step": 2, "title": "On-Site HDR 360° Scanning", "desc": "Methodical shoot using professional 360° sensors with zero disruption to your daily operations."},
                {"step": 3, "title": "Stitching & Chromatic Retouching", "desc": "High-precision panorama alignment, tripod nadir removal, and color balancing."},
                {"step": 4, "title": "Hotspots & Interactive Tagging", "desc": "Embedding callouts, product links, menus, and branded interactive overlays."},
                {"step": 5, "title": "Deployment & Google Maps Integration", "desc": "Cloud hosting deployment, Google Street View synchronization, and iframe delivery."}
            ],
            'ar': [
                {"step": 1, "title": "المعاينة وتجهيز المكان", "desc": "تقديم إرشادات لترتيب المساحة واختيار أوقات الإضاءة المثالية للتصوير."},
                {"step": 2, "title": "التصوير الميداني بكاميرات HDR متطورة", "desc": "التقاط المشاهد البانورامية بدقة وسلاسة دون تعطيل نشاطكم التجاري."},
                {"step": 3, "title": "دمج الصور والمعالجة اللونية", "desc": "تركيب الزوايا بدقة متناهية وإزالة الحامل الثلاثي وتوحيد توازن الألوان."},
                {"step": 4, "title": "إضافة النقاط التفاعلية والروابط", "desc": "دمج قوائم الأسعار وروابط الشراء وروابط حجز المواعيد داخل الجولة."},
                {"step": 5, "title": "النشر والربط مع خرائط جوجل", "desc": "تفعيل الجولة على Google Street View وتزويدكم بروابط المشاركة التفاعلية."}
            ]
        },
        'faqs': {
            'fr': [
                {"q": "Combien de temps prend la séance de capture dans mon établissement ?", "a": "Pour une boutique ou un restaurant de 100 à 250 m², le tournage dure généralement entre 1h et 2h30. Nous intervenons en dehors de vos heures de pointe ou avant l'ouverture."},
                {"q": "La visite 360° aide-t-elle le référencement sur Google Maps ?", "a": "Oui, les fiches Google Business équipées d'une visite virtuelle 360° bénéficient d'un engagement utilisateur deux fois supérieur et d'une meilleure visibilité dans les recherches locales à Tanger."},
                {"q": "Pouvez-vous flouter les visages ou plaques d'immatriculation ?", "a": "Absolument. Conformément aux règles de protection des données, nous appliquons un floutage strict sur tous les visages, plaques et données sensibles visibles."},
                {"q": "Peut-on mettre à jour la visite si l'agencement du magasin change ?", "a": "Oui, nous pouvons refaire des captures partielles des zones modifiées sans devoir réenregistrer l'intégralité du parcours."},
                {"q": "Dans quelles villes du Nord vous déplacez-vous ?", "a": "Notre équipe se déplace à Tanger, Tétouan, Asilah, Larache, Chefchaouen, M'diq, Martil, Fnideq et Al Hoceima."},
                {"q": "La visite virtuelle fonctionne-t-elle sur les téléphones mobiles ?", "a": "Parfaitement, elle est 100% responsive et utilise les capteurs gyroscopiques du smartphone pour une navigation naturelle."}
            ],
            'en': [
                {"q": "How long does an on-site shooting session take?", "a": "For a typical venue of 100 to 250 m², the shoot takes between 1 to 2.5 hours. We can schedule early morning or after-hours slots to avoid customer interference."},
                {"q": "Does a 360° tour improve my Google Maps search ranking?", "a": "Yes, Google Business listings with virtual tours generate twice as much customer engagement and demonstrate improved local search prominence in Tanger."},
                {"q": "Can you blur pedestrian faces and vehicle license plates?", "a": "Yes, in strict adherence with privacy standards, we systematically blur all human faces, private documents, and vehicle registration plates."},
                {"q": "Can the tour be updated if we rearrange our store?", "a": "Yes, we can re-shoot specific sections and seamlessly splice updated panoramas into your existing tour."},
                {"q": "Which cities in Northern Morocco do you cover for on-site captures?", "a": "Our production crew covers Tanger, Tétouan, Asilah, Larache, Chefchaouen, M'diq, Martil, Fnideq, and Al Hoceima."},
                {"q": "Does the virtual tour perform well on mobile devices?", "a": "Yes, it is fully responsive and leverages native device gyroscopes for smooth motion-based exploration."}
            ],
            'ar': [
                {"q": "كم تستغرق جلسة التصوير داخل المقر التجاري؟", "a": "تستغرق الجلسة من ساعة إلى ساعتين ونصف لمساحة تتراوح بين 100 و 250 متر مربع، ونحرص على التنسيق قبل ساعات العمل أو في أوقات الهدوء."},
                {"q": "هل تساعد الجولة في تحسين ترتيب النشاط على خرائط جوجل؟", "a": "نعم، تسجل الأنشطة التجارية المزودة بجولات 360 تفاعلاً مضاعفاً وظهوراً أقوى في نتائج البحث المحلية بطنجة والمغرب."},
                {"q": "هل يمكن طمس الوجوه وأرقام لوحات السيارات للحفاظ على الخصوصية؟", "a": "نعم، نلتزم بالمعايير القانونية الصارمة ونقوم بطمس كافة الوجوه والبيانات الشخصية الحساسة."},
                {"q": "هل يمكن تحديث الجولة في حال تغيير ديكور أو أثاث المحل؟", "a": "نعم، يمكننا تصوير الأركان المحدثة ودمجها في الجولة القائمة دون الحاجة لإعادة تصوير المحل كاملاً."},
                {"q": "ما هي المدن التي تغطيها فرقكم الميدانية؟", "a": "نغطي طنجة، تطوان، أصيلة، العرائش، شفشاون، المضيق، مرتيل، الفنيدق، والحسيمة."},
                {"q": "هل تعمل الجولة بسلاسة على الهواتف الذكية؟", "a": "نعم، متوافقة 100% مع الهواتف وتستفيد من حساس الحركة (الجايروسكوب) لتوفير تجربة استكشاف واقعية بمجرد تحريك الهاتف."}
            ]
        },
        'related_services': ['visites-virtuelles', 'photographie', 'lead-generation'],
        'related_projects': ['concept-store-tanger', 'residence-malabata-tanger']
    },
    'photographie': {
        'turnaround': {
            'fr': "3 à 6 jours ouvrés après le shooting (TODO_OWNER: confirmer délais selon nombre de clichés retouchés).",
            'en': "3 to 6 business days after the shoot (TODO_OWNER: confirm retouched photo turnaround).",
            'ar': "من 3 إلى 6 أيام عمل بعد جلسة التصوير (TODO_OWNER: تأكيد مواعيد تسليم الصور المعالجة).",
        },
        'target_audience': {
            'fr': "Architectes, promoteurs immobiliers, hôteliers, propriétaires de villas de luxe et marques à Tanger et dans le Nord.",
            'en': "Architects, property developers, boutique hoteliers, luxury villa owners, and premium brands across Northern Morocco.",
            'ar': "المهندسون المعماريون، المطورون العقاريون، الفنادق، أصحاب الفيلات الفاخرة بطنجة وشمال المغرب.",
        },
        'deliverables': {
            'fr': [
                {"title": "Reportage photo d'architecture & d'intérieur", "desc": "Clichés équilibrés captant la lumière naturelle, les perspectives et les volumes des espaces."},
                {"title": "Prises de vues aériennes par drone", "desc": "Photos et vidéos aériennes mettant en valeur la situation géographique et l'environnement du projet."},
                {"title": "Post-production & Retouche chromatique soignée", "desc": "Correction des perspectives, colorimétrie fine et suppression des éléments parasites."},
                {"title": "Fichiers livrés en double format (Print 300 DPI + Web)", "desc": "Images optimisées pour l'impression haute définition et pour vos réseaux sociaux et site web."}
            ],
            'en': [
                {"title": "Architectural & Interior Photo Coverage", "desc": "Balanced compositions emphasizing natural daylight, geometry, and material craftsmanship."},
                {"title": "Aerial Drone Photography", "desc": "Stunning aerial vistas capturing the geographic location and coastline context of your development."},
                {"title": "Advanced Post-Processing & Retouching", "desc": "Perspective alignment, precise color grading, and unwanted distraction removal."},
                {"title": "Dual-Format Delivery (High-Res 300 DPI + Web)", "desc": "Exported in high-resolution for print publishing alongside compressed web assets for social channels."}
            ],
            'ar': [
                {"title": "تصوير معماري وتصميم داخلي احترافي", "desc": "لقطات متوازنة تبرز جمالية الإضاءة الطبيعية والتناغم الهندسي والمساحات."},
                {"title": "تصوير جوي بواسطة الدرون", "desc": "مشاهد جوية ساحرة تبرز الموقع الجغرافي وقرب المشروع من السواحل والمرافق الحيوية."},
                {"title": "معالجة احترافية وضبط لوني متقن", "desc": "تصحيح زوايا الخطوط المعمارية وتوازن الألوان وإزالة أي عناصر مشتتة."},
                {"title": "تسليم بصيغتين (طباعة عالية الدقة + ويب)", "desc": "ملفات مجهزة للطباعة بجودة 300 DPI وأخرى مضغوطة وسريعة للمواقع والشبكات الاجتماعية."}
            ]
        },
        'process': {
            'fr': [
                {"step": 1, "title": "Briefing artistique & Cadrage des besoins", "desc": "Définition des angles prioritaires, des ambiances souhaitées (jour, coucher de soleil, nuit) et des horaires de lumière."},
                {"step": 2, "title": "Séance de shooting sur site", "desc": "Prises de vues au trépied professionnel, objectifs à décentrement pour respecter la verticalité architecturale."},
                {"step": 3, "title": "Vols de drone & Prises de vue aériennes", "desc": "Captation aérienne sécurisée par télépilote expérimenté pour valoriser l'insertion du bien dans le paysage de Tanger."},
                {"step": 4, "title": "Développement RAW & Retouche fine", "desc": "Harmonisation de l'exposition, correction géométrique des fuyantes et retouche minutieuse des détails."},
                {"step": 5, "title": "Livraison en galerie privée sécurisée", "desc": "Téléchargement immédiat des fichiers haute résolution et des versions allégées pour votre communication."}
            ],
            'en': [
                {"step": 1, "title": "Artistic Briefing & Light Scheduling", "desc": "Determining key compositions, target ambiances (midday, golden hour, twilight), and sun tracking."},
                {"step": 2, "title": "On-Site Architectural Shoot", "desc": "Tripod-mounted capture using tilt-shift lenses to preserve strict vertical architectural lines."},
                {"step": 3, "title": "Drone Flight & Aerial Capture", "desc": "Careful aerial maneuvers highlighting the property's relationship to surrounding Tanger geography."},
                {"step": 4, "title": "RAW Development & Precision Editing", "desc": "HDR exposure blending, perspective correction, and meticulous detail polishing."},
                {"step": 5, "title": "Secure Client Gallery Delivery", "desc": "Instant download of print-ready high-resolution masters alongside web-optimized versions."}
            ],
            'ar': [
                {"step": 1, "title": "التخطيط الفني واختيار مواقيت الإضاءة", "desc": "تحديد الزوايا الأساسية واللحظات الضوئية المفضلة (الصباح، الغروب الذهبي، أو المشاهد الليلية)."},
                {"step": 2, "title": "جلسة التصوير المعماري الميداني", "desc": "استخدام عدسات معمارية مخصصة تحافظ على استقامة الأعمدة والخطوط العمودية."},
                {"step": 3, "title": "التحليق والتصوير الجوي بالدرون", "desc": "تصوير جوي احترافي يبرز تموضع العقار في المشهد الطبيعي الساحلي لطنجة."},
                {"step": 4, "title": "معالجة وتصحيح ملفات RAW", "desc": "معالجة تباين الإضاءة، ضبط درجات الألوان، والتخلص من أي شوائب بصرية."},
                {"step": 5, "title": "التسليم عبر معرض رقمي آمن", "desc": "إمكانية تحميل الصور فوراً بصيغ الطباعة الفاخرة وصيغ الويب السريعة."}
            ]
        },
        'faqs': {
            'fr': [
                {"q": "Disposez-vous des autorisations de vol pour le drone au Maroc ?", "a": "Nos tournages aériens sont encadrés par les protocoles réglementaires applicables au Maroc pour garantir des captations sécurisées et conformes."},
                {"q": "Quelle est la meilleure heure pour photographier une villa ou un hôtel ?", "a": "L'aube et l'heure dorée (fin d'après-midi) offrent une lumière rasante douce qui sublime les façades méditerranéennes, complétée par un shooting crépusculaire pour mettre en valeur les éclairages intérieurs et piscines."},
                {"q": "Fournissez-vous les fichiers RAW non retouchés ?", "a": "Nous livrons des fichiers finaux soigneusement développés et retouchés (TIFF ou JPEG haute définition). Les fichiers bruts RAW ne sont généralement pas diffusés car le développement artistique fait partie intégrante de notre prestation."},
                {"q": "Combien de photos retouchées sont généralement livrées ?", "a": "Selon l'envergure du projet, nous livrons habituellement entre 15 et 30 clichés d'exception sélectionnés et minutieusement retouchés."},
                {"q": "Pouvez-vous réaliser des prises de vue pour le suivi de chantier ?", "a": "Oui, nous proposons des forfaits d'interventions régulières (mensuelles ou bimensuelles) pour documenter l'avancement des chantiers à Tanger et Tétouan."},
                {"q": "Dans quels délais recevons-nous les photos après le shooting ?", "a": "Les photos sélectionnées et retouchées sont livrées sous 3 à 6 jours ouvrés via un espace de téléchargement sécurisé."}
            ],
            'en': [
                {"q": "How do you handle aerial drone flights in Morocco?", "a": "Our drone operations strictly adhere to Moroccan aviation safety procedures, handled by experienced remote pilots to deliver compliant, safe captures."},
                {"q": "What is the best time of day to shoot a luxury villa or resort?", "a": "Golden hour and twilight provide gentle Mediterranean light, while dusk sessions showcase outdoor pools, landscaping, and warm interior lighting."},
                {"q": "Do you deliver unedited RAW image files?", "a": "We deliver finished, retouched master files (high-res JPEG/TIFF). RAW files are excluded as our tailored color grading is essential to our visual signature."},
                {"q": "How many final retouched photos are delivered per assignment?", "a": "Depending on project scope, our packages typically deliver 15 to 30 meticulously graded, high-impact photographs."},
                {"q": "Do you offer construction site monitoring photography?", "a": "Yes, we provide recurring monthly or bi-weekly photo and aerial drone shoots tracking development milestones across Tanger and Tétouan."},
                {"q": "What is the turnaround time to receive retouched photographs?", "a": "The polished final gallery is delivered within 3 to 6 business days through a private high-speed download link."}
            ],
            'ar': [
                {"q": "كيف يتم التعامل مع تصوير الدرون وفق الضوابط في المغرب؟", "a": "نعتمد بروتوكولات احترافية صارمة تضمن السلامة والامتثال للمعايير المعمول بها في المغرب لتنفيذ اللقطات الجوية بأمان."},
                {"q": "ما هو أفضل وقت لتصوير فيلا أو منشأة فندقية؟", "a": "ساعات الصباح الباكر وقبيل الغروب (الساعة الذهبية) تمنح واجهات المباني دفئاً جذاباً، فضلاً عن جلسة الغسق لإبراز إنارة المسابح والحدائق."},
                {"q": "هل تسلمون ملفات RAW الخام؟", "a": "نسلّم صوراً منقحة ومجهزة بأعلى معايير الجودة الفنية (JPEG / TIFF). المعالجة اللونية الاحترافية جزء أساسي من هويتنا الفنية."},
                {"q": "كم عدد الصور المعالجة التي يتضمنها العرض عادة؟", "a": "حسب حجم المشروع، تتراوح الحزمة النموذجية بين 15 و 30 صورة مختارة بعناية ومتقنة المعالجة."},
                {"q": "هل تقدمون خدمة المتابعة المصورة لأوراش البناء؟", "a": "نعم، نقدم عقود متابعة دورية (شهرية أو نصف شهرية) لتوثيق مراحل تقدم أشغال البناء بطنجة وتطوان والمناطق المجاورة."},
                {"q": "ما هي المهلة المستغرقة لتسلم الصور بعد التصوير؟", "a": "تُسلَّم الصور المعالجة خلال 3 إلى 6 أيام عمل عبر رابط تنزيل مباشر وفائق السرعة."}
            ]
        },
        'related_services': ['captures-360', 'modelisation-3d', 'branding-visuel'],
        'related_projects': ['villa-californie-tanger', 'residence-malabata-tanger']
    },
    'animation-motion-design': {
        'turnaround': {
            'fr': "10 à 20 jours ouvrés selon la durée du film et la complexité des scènes 3D (TODO_OWNER: valider les délais moyens de rendu).",
            'en': "10 to 20 business days depending on video duration and 3D complexity (TODO_OWNER: validate average rendering deadlines).",
            'ar': "من 10 إلى 20 يوم عمل حسب مدة الفيديو وتعقيد المشاهد (TODO_OWNER: تأكيد مواعيد إنتاج الرسوم المتحركة).",
        },
        'target_audience': {
            'fr': "Promoteurs immobiliers de grands ensembles, architectes, marques et agences de communication à Tanger et au Maroc.",
            'en': "Large-scale real estate developers, visionary architects, luxury brands, and marketing agencies across Morocco.",
            'ar': "المطورون العقاريون للمشاريع الكبرى، المهندسون المعماريون، والوكالات الإعلانية بطنجة والمغرب.",
        },
        'deliverables': {
            'fr': [
                {"title": "Film 3D cinématographique en 4K Ultra-HD", "desc": "Parcours vidéo immersif avec travellings fluides, animation de végétation et météo dynamique."},
                {"title": "Bande sonore & Sound design professionnel", "desc": "Habillage musical libre de droits, voix-off multilingue (FR/EN/AR) et effets sonores soignés."},
                {"title": "Teasers courts pour réseaux sociaux (Reels / TikTok)", "desc": "Déclinaisons au format vertical 9:16 pour susciter l'engagement sur Instagram et TikTok."},
                {"title": "Animations graphiques (Motion Design)", "desc": "Incrustation de chiffres clés, titrages élégants et plans de situation stylisés."}
            ],
            'en': [
                {"title": "Cinematic 4K Ultra-HD 3D Video Walkthrough", "desc": "Sweeping camera movements, realistic moving vegetation, and dynamic coastal weather atmospherics."},
                {"title": "Professional Sound Design & Multilingual Voiceover", "desc": "Licensed music score, crisp multilingual voiceovers (FR/EN/AR), and tailored sound effects."},
                {"title": "Social Media Teaser Cuts (Reels / TikTok 9:16)", "desc": "Dynamic vertical cutdowns optimized for high retention on Instagram Reels and TikTok."},
                {"title": "Animated Motion Graphics & Data Overlays", "desc": "Elegant on-screen typography, key metric callouts, and animated site location graphics."}
            ],
            'ar': [
                {"title": "فيديو سينمائي ثلاثي الأبعاد بدقة 4K", "desc": "جولة مصورة مذهلة بحركات كاميرا انسيابية وتفاعل واقعي للأشجار والإضاءة الطبيعية."},
                {"title": "هندسة صوتية وتعليق صوتي احترافي", "desc": "موسيقى مرخصة ومؤثرات صوتية محيطية مع تعليق صوتي فصيح ومتقن (عربي/فرنسي/إنجليزي)."},
                {"title": "مقاطع قصيرة لمنصات التواصل (Reels / TikTok)", "desc": "نسخ مصممة بالشكل العمودي 9:16 لجذب اهتمام المتابعين على إنستغرام وتيك توك."},
                {"title": "موشن ديزاين ورسوم بيانية متحركة", "desc": "إبراز بيانات المشروع الأساسية والموقع الاستراتيجي عبر تصاميم نصية ورسومية أنيقة."}
            ]
        },
        'process': {
            'fr': [
                {"step": 1, "title": "Storyboard & Script narratif", "desc": "Scénarisation du film, définition des plans caméras, écriture de la voix-off et du rythme émotionnel."},
                {"step": 2, "title": "Animatique & Cadrages 3D basse résolution", "desc": "Validation des trajectoires de caméra et du timing des séquences avant le calcul de rendu lourd."},
                {"step": 3, "title": "Calcul de rendu 3D sur ferme de serveurs", "desc": "Génération image par image des milliers de frames en 4K avec gestion des reflets et lumières physiques."},
                {"step": 4, "title": "Montage, Motion Design & Étalonnage", "desc": "Assemblage dynamique des plans, incrustation des titrages animés et harmonisation chromatique cinéma."},
                {"step": 5, "title": "Sound design, Mixage voix-off & Livraison", "desc": "Enregistrement de la voix-off professionnelle, mixage audio et exportation dans tous les formats de diffusion."}
            ],
            'en': [
                {"step": 1, "title": "Storyboard & Narrative Scriptwriting", "desc": "Visual script outline, camera trajectory blueprints, voiceover drafting, and emotional pacing."},
                {"step": 2, "title": "Animatic & Low-Res Camera Blocking", "desc": "Previewing camera moves and sequence tempo for client approval prior to intensive rendering."},
                {"step": 3, "title": "High-Performance Cloud Farm Rendering", "desc": "Frame-by-frame 4K generation calculating photorealistic reflections, shadows, and natural daylight."},
                {"step": 4, "title": "Editing, Motion Graphics & Color Grading", "desc": "Pacing cutdown, kinetic typography overlays, and cinema-grade color balance."},
                {"step": 5, "title": "Voiceover Recording & Sound Mastering", "desc": "Professional studio voiceover tracking, audio mixing, and multi-format master export."}
            ],
            'ar': [
                {"step": 1, "title": "كتابة السيناريو ورسم المشاهد (Storyboard)", "desc": "صياغة القصة الإعلانية وتحديد مسار الكاميرا وإعداد نص التعليق الصوتي."},
                {"step": 2, "title": "المعاينة الحركية الأولية (Animatic)", "desc": "مراجعة سرعة حركة الكاميرا واللقطات قبل بدء مرحلة المعالجة المكثفة."},
                {"step": 3, "title": "المعالجة الحسابية عبر مزارع الرندر (Render Farm)", "desc": "توليد آلاف الإطارات بجودة 4K مع محاكاة فيزيائية فائقة الدقة للضوء والظلال."},
                {"step": 4, "title": "المونتاج والموشن ديزاين والتدرج اللوني", "desc": "تركيب المشاهد بإيقاع مشوق مع نصوص متحركة أنيقة وضبط لوني بمستوى السينما."},
                {"step": 5, "title": "تسجيل الصوت والميكساج والتسليم", "desc": "تسجيل التعليق الصوتي بأصوات إذاعية فخمة ومزج المؤثرات الصوتية وتسليم النسخ النهائية."}
            ]
        },
        'faqs': {
            'fr': [
                {"q": "Quelle est la durée recommandée pour une vidéo 3D immobilière ?", "a": "Une durée comprise entre 60 et 90 secondes est idéale pour capter et maintenir l'attention des investisseurs, complétée par des teasers courts de 15 à 30 secondes pour les réseaux sociaux."},
                {"q": "Proposez-vous des voix-off en arabe, français et anglais ?", "a": "Oui, nous collaborons avec des comédiens voix professionnels natifs pour enregistrer vos messages en français, en anglais et en arabe standard ou marocain (darija soignée)."},
                {"q": "Combien de temps faut-il pour concevoir un film d'animation 3D ?", "a": "Comptez généralement entre 2 et 4 semaines selon la complexité des décors, le nombre de pièces à animer et les délais de validation du storyboard."},
                {"q": "Pouvez-vous animer la circulation des personnes ou des véhicules ?", "a": "Oui, nous pouvons intégrer des silhouettes humaines stylisées, des véhicules en mouvement et de la végétation animée par le vent marin pour donner un réalisme saisissant."},
                {"q": "Fournissez-vous des déclinaisons adaptées aux stories et reels Instagram ?", "a": "Oui, nous vous fournissons systématiquement les versions horizontales 16:9 pour écrans et salons, ainsi que des déclinaisons verticales 9:16 pour les réseaux sociaux."},
                {"q": "Peut-on insérer des prises de vues réelles de Tanger dans le film 3D ?", "a": "Tout à fait. Nous combinons fréquemment plans drone réels de la baie de Tanger et séquences 3D dans un montage fluide et percutant."}
            ],
            'en': [
                {"q": "What is the optimal duration for a real estate 3D animation?", "a": "A 60 to 90-second duration is proven to maintain maximum investor focus, complemented by 15-to-30-second teaser cuts for social channels."},
                {"q": "Do you provide voiceovers in Arabic, French, and English?", "a": "Yes, we work with professional voice artists delivering natural performances in French, English, and Modern Standard Arabic or polished Moroccan Darija."},
                {"q": "How long does it take to produce a full 3D architectural animation?", "a": "Production typically spans 2 to 4 weeks, depending on volumetric complexity, scenery detail, and storyboard approval milestones."},
                {"q": "Can you animate pedestrians and moving vehicles?", "a": "Yes, we can incorporate stylized human activity, passing vehicles, and wind-blown Mediterranean flora to enhance lifelike realism."},
                {"q": "Do you provide vertical video formats for Instagram Reels & TikTok?", "a": "Yes, alongside master 16:9 widescreen formats, we craft vertical 9:16 cutdowns specifically optimized for mobile social feeds."},
                {"q": "Can you blend live-action footage of Tanger into the 3D walkthrough?", "a": "Yes, we frequently composite real 4K drone footage of Tanger Bay seamlessly with 3D architectural scenes."}
            ],
            'ar': [
                {"q": "ما هي المدة المثالية لفيديو ترويجي عقاري 3D؟", "a": "تتراوح المدة المثالية بين 60 و 90 ثانية للحفاظ على انتباه المشاهد، مع استخراج مقاطع قصيرة مدتها 15 إلى 30 ثانية للإعلانات."},
                {"q": "هل توفرون تعليقاً صوتياً باللغات العربية والفرنسية والإنجليزية؟", "a": "نعم، نتعامل مع معلقين صوتيين محترفين باللغات الثلاث لتقديم نبرة فخمة تناسب مكانة المشروع."},
                {"q": "كم يستغرق إنتاج فيديو أنيميشن 3D متكامل؟", "a": "يستغرق الإنتاج عموماً ما بين أسبوعين إلى 4 أسابيع تبعاً لمساحة المشروع وعدد المشاهد واعتماد السيناريو."},
                {"q": "هل يمكن إضافة حركة أشخاص وسيارات وأشجار في الفيديو؟", "a": "نعم، ندمج عناصر حركية واقعية كالأشجار التي تتمايل مع نسيم البحر وحركة سيارات انسيابية تضفي حيوية واقعية على المكان."},
                {"q": "هل تسلمون نسخاً مخصصة لإنستغرام ريلز وتيك توك؟", "a": "نعم، نسلمكم النسخة العريضة 16:9 للشاشات الكبيرة إلى جانب نسخ طولية 9:16 مجهزة خصيصاً للمنصات الرقمية."},
                {"q": "هل يمكن دمج لقطات حقيقية لطنجة بالدرون داخل الفيديو؟", "a": "بالتأكيد، نمزج ببراعة بين مشاهد درون حقيقية لساحل طنجة والمشاهد ثلاثية الأبعاد للمشروع لإعطاء سياق جغرافي جذاب."}
            ]
        },
        'related_services': ['modelisation-3d', 'visites-virtuelles', 'photographie'],
        'related_projects': ['residence-malabata-tanger', 'villa-californie-tanger']
    },
    'branding-visuel': {
        'turnaround': {
            'fr': "7 à 14 jours ouvrés selon le périmètre graphique (TODO_OWNER: valider les délais de charte complète).",
            'en': "7 to 14 business days depending on design scope (TODO_OWNER: confirm brand identity turnaround).",
            'ar': "من 7 إلى 14 يوم عمل حسب نطاق الهوية البصرية (TODO_OWNER: تأكيد مواعيد تصميم الهوية الكاملة).",
        },
        'target_audience': {
            'fr': "Promoteurs lançant un nouveau programme neuf, marques émergentes, hôtels, cabinets d'architecture et commerces à Tanger.",
            'en': "Real estate developers launching new residential projects, emerging brands, hotels, architecture studios, and upscale retail venues in Tanger.",
            'ar': "شركات التطوير العقاري التي تطلق مشاريع سكنية جديدة، العلامات التجارية الناشئة، الفنادق والمحلات الفاخرة بطنجة.",
        },
        'deliverables': {
            'fr': [
                {"title": "Logotype vectoriel & Déclinaisons", "desc": "Logo principal, monogramme et déclinaisons en noir, blanc et couleurs pour tous fonds."},
                {"title": "Charte graphique complète (Brand Guidelines)", "desc": "Guide de normes : typographies, palette chromatique, règles d'usage et interdictions."},
                {"title": "Supports de vente & Plaquettes commerciales", "desc": "Mise en page de brochures luxueuses, chemises à rabat et fiches descriptives pour vos agents commerciaux."},
                {"title": "Signalétique & Panneaux de chantier", "desc": "Fichiers prêts pour impression grand format : habillage de palissades de chantier et totems d'accueil."}
            ],
            'en': [
                {"title": "Vector Logo & Brand System", "desc": "Primary logo, emblem variations, and monochrome/color adaptations for all background contexts."},
                {"title": "Comprehensive Brand Guidelines Manual", "desc": "Complete reference: typography hierarchy, color codes (Pantone/CMYK/RGB), and usage rules."},
                {"title": "Sales Collateral & Luxury Brochures", "desc": "Editorial layouts for sales booklets, presentation folders, and apartment fact sheets."},
                {"title": "On-Site Signage & Hoardings", "desc": "Print-ready vectors for 4×3m construction boards, flags, hoardings, and on-site sales booths."}
            ],
            'ar': [
                {"title": "شعار فيكتوري وتطبيقات الهوية", "desc": "الشعار الرئيسي، الرمز المصغر، ونسخ ملونة وأحادية تلائم مختلف الخلفيات والوسائط."},
                {"title": "دليل الهوية البصرية المتكامل (Brand Guidelines)", "desc": "دليل شامل يحدد الخطوط، درجات الألوان بدقة، وقواعد الاستخدام الصحيح للشعار."},
                {"title": "تصاميم الكتيبات والمجلدات التسويقية", "desc": "تصميم كتيبات ترويجية فخمة ومطويات تفصيلية تساعد فريق مبيعاتكم على الإقناع."},
                {"title": "لوحات الورش واللافتات التوجيهية", "desc": "ملفات مجهزة للطباعة الكبيرة لتغطية واجهات ورش البناء واللوحات الترحيبية."}
            ]
        },
        'process': {
            'fr': [
                {"step": 1, "title": "Audit d'image & Positionnement de marque", "desc": "Analyse du public cible, de l'environnement concurrentiel à Tanger et définition des valeurs clés."},
                {"step": 2, "title": "Pistes créatives & Moodboards", "desc": "Exploration de 2 à 3 directions artistiques distinctes et présentation de planches d'ambiance."},
                {"step": 3, "title": "Affinage du concept retenu", "desc": "Perfectionnement typographique, ajustement de la palette de couleurs et équilibre visuel."},
                {"step": 4, "title": "Déclinaison sur les supports prioritaires", "desc": "Mise en page des cartes de visite, brochures de vente, kakémonos et panneaux de chantier."},
                {"step": 5, "title": "Remise du pack complet & Charte", "desc": "Livraison de tous les fichiers sources vectoriels (AI, EPS, PDF, PNG) et du guide de marque."}
            ],
            'en': [
                {"step": 1, "title": "Brand Discovery & Market Positioning", "desc": "Target buyer analysis, competitive benchmarking in Tanger, and core value definition."},
                {"step": 2, "title": "Creative Directions & Moodboards", "desc": "Exploration of 2 to 3 distinctive artistic routes with moodboards and preliminary sketches."},
                {"step": 3, "title": "Concept Refinement & Polishing", "desc": "Typography selection, precise Pantone matching, and logo proportionality tuning."},
                {"step": 4, "title": "Collateral & Marketing Asset Layout", "desc": "Designing sales brochures, stationery, hoardings, and digital advertising templates."},
                {"step": 5, "title": "Final Brand Kit Delivery", "desc": "Delivery of complete vector master files (AI, EPS, PDF, SVG, PNG) and corporate guidelines."}
            ],
            'ar': [
                {"step": 1, "title": "دراسة التموضع والجمهور المستهدف", "desc": "تحليل تطلعات المشترين والمنافسين في سوق طنجة وتحديد طابع الهوية المناسب."},
                {"step": 2, "title": "اقتراح مسارات إبداعية ونماذج أولية", "desc": "تقديم 2 إلى 3 مسارات فنية متباينة تعبر عن روح وفخامة المشروع."},
                {"step": 3, "title": "تطوير وضبط الاتجاه المختار", "desc": "تنقيح الخطوط، تنسيق درجات الألوان، وموازنة النسب البصرية للشعار."},
                {"step": 4, "title": "تصميم المطبوعات والوسائط الإعلانية", "desc": "إعداد كتيبات المبيعات، بطاقات الأعمال، لافتات الورش، وقوالب النشر الرقمي."},
                {"step": 5, "title": "تسليم حزمة الهوية الكاملة", "desc": "تسليم كافة الملفات المصدرية المفتوحة (AI, EPS, PDF, PNG) مع دليل المعايير."}
            ]
        },
        'faqs': {
            'fr': [
                {"q": "Fournissez-vous les fichiers sources modifiables du logo ?", "a": "Oui, nous vous remettons l'ensemble des fichiers sources vectoriels natifs (Adobe Illustrator .AI, .EPS, .PDF) ainsi que les versions optimisées pour le web (.PNG, .SVG)."},
                {"q": "Combien de propositions de logos présentez-vous ?", "a": "Nous présentons systématiquement 2 à 3 pistes créatives aux univers graphiques bien distincts, avant d'affiner celle que vous sélectionnez."},
                {"q": "Pouvez-vous adapter le logo aux langues arabe et française ?", "a": "Absolument. Nous maîtrisons la calligraphie arabe contemporaine et la typographie latine pour concevoir des identités bilingues parfaitement équilibrées."},
                {"q": "Prenez-vous en charge l'impression de nos brochures et panneaux ?", "a": "Nous préparons tous les fichiers certifiés pour l'imprimerie (traits de coupe, fond perdu, profils CMJN) et pouvons vous recommander nos imprimeurs partenaires de confiance à Tanger."},
                {"q": "Quel est le délai de création d'une identité visuelle complète ?", "a": "Une charte graphique de programme immobilier est généralement finalisée sous 7 à 14 jours ouvrés en concertation avec vos équipes."},
                {"q": "Que contient le document de charte graphique remis ?", "a": "Il détaille les règles d'usage du logo, les codes couleur précis (CMJN, RVB, Pantone, Hexadécimal), la typographie d'entreprise et des exemples d'applications concrètes."}
            ],
            'en': [
                {"q": "Do you provide editable source files for the logo?", "a": "Yes, you receive complete vector source files (Adobe Illustrator .AI, .EPS, .PDF) and digital formats (.SVG, high-res .PNG)."},
                {"q": "How many initial logo concepts do you present?", "a": "We present 2 to 3 distinct artistic routes with different styling and typography before developing your preferred direction."},
                {"q": "Can you design bilingual Arabic and French branding?", "a": "Yes, we specialize in harmonizing modern Arabic typography and calligraphy with Latin letterforms for balanced bilingual identities."},
                {"q": "Do you handle the physical printing of brochures and site signage?", "a": "We provide certified press-ready files (bleed, trim marks, CMYK profiles) and can coordinate directly with trusted print partners in Tanger."},
                {"q": "What is the typical timeframe to create a comprehensive brand identity?", "a": "A full corporate brand package is typically finalized within 7 to 14 business days."},
                {"q": "What is included inside the Brand Guidelines manual?", "a": "It outlines logo clearspace rules, minimum sizing, official color codes (CMYK, RGB, Pantone, HEX), typography pairings, and layout examples."}
            ],
            'ar': [
                {"q": "هل تسلمون الملفات المصدرية المفتوحة للشعار؟", "a": "نعم، نسلمكم كافة الملفات المصدرية الأصلية (AI, EPS, PDF) إلى جانب صيغ الويب عالية النقاء (SVG, PNG)."},
                {"q": "كم عدد النماذج المقترحة للشعار في البداية؟", "a": "نقدم من نموذجَين إلى 3 نماذج إبداعية متباينة في الأسلوب والخطوط لاختيار الأنسب منها والتطوير عليه."},
                {"q": "هل يمكن تصميم شعار ثنائي اللغة يجمع العربية والفرنسية؟", "a": "بالتأكيد، نتخصص في تصميم شعارات ثنائية اللغة تجمع بين أصالة الخط العربي وأناقة الحروف اللاتينية بتناغم بصري متقن."},
                {"q": "هل تشمل الخدمة طباعة الكتيبات ولوحات الورش؟", "a": "نسلمكم ملفات معتمدة ومجهزة بالمقاييس الطباعية الدقيقة، ويمكننا التنسيق مع أفضل المطابع الشريكة بطنجة لتنفيذ الطباعة."},
                {"q": "ما هي المدة اللازمة لإنجاز هوية بصرية متكاملة؟", "a": "يستغرق العمل عادة من 7 إلى 14 يوم عمل مع جولات مراجعة تشاركية معكم."},
                {"q": "ماذا يتضمن دليل الهوية البصرية (Brand Guidelines)؟", "a": "يتضمن نسب الشعار ومساحات الأمان، الأكواد الدقيقة للألوان (Pantone, CMYK, RGB)، نوع الخطوط المعتمدة، وأمثلة عملية للتطبيق."}
            ]
        },
        'related_services': ['lead-generation', 'modelisation-3d', 'photographie'],
        'related_projects': ['concept-store-tanger', 'residence-malabata-tanger']
    },
    'lead-generation': {
        'turnaround': {
            'fr': "5 à 7 jours ouvrés pour la mise en place de l'écosystème publicitaire et de la landing page (TODO_OWNER: valider les délais de paramétrage).",
            'en': "5 to 7 business days to launch the ad setup and dedicated landing page (TODO_OWNER: confirm setup timeline).",
            'ar': "من 5 إلى 7 أيام عمل لإطلاق المنظومة الإعلانية وصفحة الهبوط (TODO_OWNER: تأكيد مواعيد الإطلاق).",
        },
        'target_audience': {
            'fr': "Promoteurs immobiliers à Tanger, agences de commercialisation, résidences hôtelières et gestionnaires de projets neufs.",
            'en': "Real estate developers in Tanger, sales brokerage agencies, serviced residences, and property project managers.",
            'ar': "شركات التطوير العقاري بطنجة، وكالات التسويق العقاري، والإقامات الفندقية الساعية لاستقطاب مشترين جادين.",
        },
        'deliverables': {
            'fr': [
                {"title": "Landing Page immersive orientée conversion", "desc": "Page web dédiée intégrant vos rendus 3D, visite virtuelle et formulaire de capture ultra-rapide."},
                {"title": "Campagnes publicitaires ciblées (Meta & Google Ads)", "desc": "Ciblage géographique et d'intérêts précis : investisseurs au Maroc, acquéreurs locaux et MRE en Europe."},
                {"title": "Tableau de bord de suivi des prospects en temps réel", "desc": "Accès instantané aux coordonnées des prospects qualifiés avec qualification budgétaire."},
                {"title": "Connexion WhatsApp & Synchronisation commerciale", "desc": "Alerte immédiate transmise à vos commerciaux par WhatsApp dès qu'un prospect soumet ses coordonnées."}
            ],
            'en': [
                {"title": "High-Converting Immersive Landing Page", "desc": "Dedicated conversion page integrating 3D renders, virtual tours, and streamlined capture forms."},
                {"title": "Targeted Meta & Google Ads Campaigns", "desc": "Precision demographic targeting: domestic Moroccan buyers, regional investors, and European diaspora."},
                {"title": "Real-Time Lead Dashboard & CRM Sync", "desc": "Live monitoring of verified buyer leads including budget qualifications and preferred unit types."},
                {"title": "Instant WhatsApp Lead Notifications", "desc": "Instant WhatsApp notifications routed directly to your sales agents as soon as inquiries arrive."}
            ],
            'ar': [
                {"title": "صفحة هبوط تفاعلية مجهزة لجمع الطلبات", "desc": "صفحة مخصصة تدمج التصاميم ثلاثية الأبعاد والجولة الافتراضية مع استمارة حجز سريعة وسهلة."},
                {"title": "حملات إعلانية دقيقة على ميتا وجوجل", "desc": "استهداف جغرافي ذكي للمشترين بطنجة والمغرب وأفراد الجالية المغربية المقيمة بأوروبا."},
                {"title": "لوحة متابعة فورية للمهتمين المؤهلين", "desc": "متابعة بيانات الزبناء في الوقت الفعلي مع تصنيفهم حسب الميزانية ونوع الشقة المطلوبة."},
                {"title": "تنبيهات فورية عبر واتساب لفريق المبيعات", "desc": "إشعار فوري لفريقكم التجاري عبر واتساب بمجرد إرسال الزبون لطلب المعاينة."}
            ]
        },
        'process': {
            'fr': [
                {"step": 1, "title": "Définition de la cible & Grille de qualification", "desc": "Identification du profil d'acquéreur idéal (budget, typologie d'appartement, pays de résidence)."},
                {"step": 2, "title": "Création de la Landing Page immersive", "desc": "Conception d'une page de vente percutante mettant en valeur les rendus 3D et l'emplacement à Tanger."},
                {"step": 3, "title": "Lancement des campagnes sponsorisées", "desc": "Diffusion des annonces sur Facebook, Instagram et Google Ads auprès des audiences qualifiées."},
                {"step": 4, "title": "Filtrage et qualification des demandes", "desc": "Validation des numéros de téléphone et vérification de la concordance budgétaire avant transfert."},
                {"step": 5, "title": "Optimisation continue du coût par prospect", "desc": "Ajustement quotidien des enchères et des visuels pour maximiser le retour sur investissement."}
            ],
            'en': [
                {"step": 1, "title": "Buyer Persona & Lead Criteria Definition", "desc": "Profiling the ideal buyer demographics, investment capacity, preferred layouts, and locations."},
                {"step": 2, "title": "Conversion Landing Page Development", "desc": "Building an engaging landing page showcasing your 3D assets, amenities, and project advantages."},
                {"step": 3, "title": "Campaign Launch across Meta & Google Ads", "desc": "Ad deployment across Instagram, Facebook, and Google Search reaching high-intent prospects."},
                {"step": 4, "title": "Lead Verification & Qualification", "desc": "Filtering verified phone numbers and checking budget eligibility before notifying your sales team."},
                {"step": 5, "title": "Continuous CPL & ROI Optimization", "desc": "Daily budget recalibration and creative testing to minimize cost per qualified lead."}
            ],
            'ar': [
                {"step": 1, "title": "تحديد الجمهور المستهدف ومعايير التأهيل", "desc": "تحديد مواصفات المشتري المثالي (الميزانية، نوع السكن، ودول الإقامة لمغاربة العالم)."},
                {"step": 2, "title": "تصميم وبرمجة صفحة الهبوط التفاعلية", "desc": "إنشاء صفحة سريعة تبرز جمالية التصاميم 3D وتفاصيل المشروع لتشجيع التسجيل."},
                {"step": 3, "title": "إطلاق الحملات الممولة على ميتا وجوجل", "desc": "نشر الإعلانات على إنستغرام وفيسبوك ومحرك بحث جوجل للوصول للباحثين الفعليين."},
                {"step": 4, "title": "فرز وتأكيد أرقام وبيانات المهتمين", "desc": "التحقق من صحة أرقام الهواتف وجدية الميزانية قبل توجيه الطلب إلى فريقكم."},
                {"step": 5, "title": "التحسين المستمر لتكلفة الزبون المحتمل", "desc": "متابعة يومية للحملات وضبط الميزانيات لتحقيق أعلى عائد على الاستثمار الإعلاني."}
            ]
        },
        'faqs': {
            'fr': [
                {"q": "Comment garantissez-vous que les prospects générés sont réellement qualifiés ?", "a": "Nos formulaires comportent des filtres stricts : sélection de la typologie d'appartement, fourchette budgétaire minimale et confirmation du numéro de téléphone par WhatsApp."},
                {"q": "Sur quelles plateformes publicitaires diffusez-vous les annonces ?", "a": "Nous ciblons principalement Meta (Instagram et Facebook) pour les visuels d'impact, et Google Ads (Search & Display) pour capter les acquéreurs en recherche active de biens neufs à Tanger."},
                {"q": "Pouvons-nous cibler les Marocains résidant à l'étranger (MRE) ?", "a": "Oui, c'est l'un de nos atouts majeurs : nous déployons des campagnes ultra-ciblées en France, Belgique, Espagne, Pays-Bas et dans les pays du Golfe pour toucher la diaspora marocaine."},
                {"q": "Comment notre équipe commerciale est-elle informée des nouveaux contacts ?", "a": "Dès qu'un prospect valide le formulaire, une alerte instantanée avec ses coordonnées complètes est envoyée par WhatsApp et e-mail à vos commerciaux, avec synchronisation optionnelle sur votre CRM."},
                {"q": "Quel budget publicitaire faut-il prévoir en plus de vos honoraires ?", "a": "Le budget média dépend de vos objectifs de vente. Nous recommandons généralement une enveloppe de départ adaptée que nous optimisons pour obtenir le coût par prospect qualifié le plus bas possible."},
                {"q": "Fournissez-vous des rapports de performance réguliers ?", "a": "Oui, vous disposez d'un tableau de bord consultable 24h/24 et nous vous transmettons un bilan chiffré hebdomadaire détaillant les clics, leads générés et coûts d'acquisition."}
            ],
            'en': [
                {"q": "How do you guarantee that generated leads are truly qualified buyers?", "a": "Our intake flows enforce multi-step validation: apartment layout choice, budget ranges, and phone number verification before reaching your team."},
                {"q": "Which digital advertising platforms do you utilize?", "a": "We primarily leverage Meta (Instagram & Facebook) for high-impact visual storytelling, alongside Google Search Ads targeting active buyers searching in Tanger."},
                {"q": "Can you target the Moroccan diaspora living in Europe (MRE)?", "a": "Yes, targeting the diaspora across France, Belgium, Spain, the Netherlands, and the Gulf is a core specialization of our agency."},
                {"q": "How quickly are incoming leads routed to our sales personnel?", "a": "Instantly. As soon as a lead submits their details, your sales team receives an immediate WhatsApp alert containing the verified contact data."},
                {"q": "What ad spend budget should be planned alongside agency fees?", "a": "Ad budgets vary depending on your sales targets. We help you calibrate an optimal starting budget designed to maximize qualified inquiries at the lowest cost."},
                {"q": "Do you provide real-time marketing reporting dashboards?", "a": "Yes, you have 24/7 access to live metrics and receive weekly digests highlighting impressions, qualified leads, and overall acquisition costs."}
            ],
            'ar': [
                {"q": "كيف تضمنون جودة وجدية الزبناء المحتملين؟", "a": "تعتمد استماراتنا تصنيفات دقيقة: تحديد نوع العقار، النطاق المالي المتاح، والتأكد من صحة أرقام الهواتف قبل التمرير لفريقكم."},
                {"q": "ما هي المنصات الإعلانية التي تعتمدون عليها في النشر؟", "a": "نعتمد بشكل رئيسي على إنستغرام وفيسبوك للمحتوى البصري الجذاب، وإعلانات محرك بحث جوجل (Google Search) للوصول للباحثين الفعليين عن شقق بطنجة."},
                {"q": "هل يمكن استهداف مغاربة العالم في الدول الأوروبية (MRE)؟", "a": "نعم، هذه نقطة قوتنا الأساسية، حيث نوجه إعلانات ممولة في فرنسا، بلجيكا، إسبانيا، هولندا ودول الخليج لاستقطاب الجالية الراغبة في الاستثمار بالمغرب."},
                {"q": "كيف يتوصل فريقنا التجاري ببيانات الزبائن الجدد؟", "a": "فور إرسال الزبون لطلبه، يتوصل مسؤول المبيعات بإشعار فوري عبر واتساب ورسالة إلكترونية تتضمن كافة بيانات التواصل والميزانية المحددة."},
                {"q": "ما هي الميزانية الإعلانية المقترحة لحملة الانطلاق؟", "a": "تختلف الميزانية حسب وتيرة المبيعات المستهدفة، ونساعدكم في تحديد الميزانية الملائمة لضمان أدنى تكلفة ممكنة لكل زبون محتمل مؤهل."},
                {"q": "هل توفرون تقارير دورية لقياس نتائج الحملات؟", "a": "نعم، نقدم لوحة تحكم فورية لمتابعة النتائج على مدار الساعة، إضافة إلى تقرير أسبوعي يلخص عدد الزيارات والطلبات وتكلفة كل فرصة بيعية."}
            ]
        },
        'related_services': ['visites-virtuelles', 'branding-visuel', 'modelisation-3d'],
        'related_projects': ['residence-malabata-tanger', 'concept-store-tanger']
    }
}


def get_service_enrichment(service_slug):
    """Retrieve localized enrichment data for a given service slug."""
    # Normalize aliases
    if service_slug in ('site-web-digital', 'site-web-experience-digitale'):
        service_slug = 'lead-generation'
    return SERVICE_ENRICHMENT.get(service_slug)
