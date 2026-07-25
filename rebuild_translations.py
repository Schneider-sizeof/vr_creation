"""Complete translation rebuild: extract ALL strings, translate ALL to EN + AR."""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

TEMPLATES_DIR = r'c:\Users\Athen\Desktop\vr_creation\templates'
APPS_DIR = r'c:\Users\Athen\Desktop\vr_creation\apps'
LOCALE_DIR = r'c:\Users\Athen\Desktop\vr_creation\locale'

trans_strings = set()
pattern = re.compile(r"""\{%\s*trans\s+['"](.+?)['"]\s*%\}""")
py_pattern = re.compile(r"""_\(\s*['"](.+?)['"]\s*\)""")
py_pattern2 = re.compile(r"""_\(\s*'(.+?)'\s*\)""")

for root, dirs, files in os.walk(TEMPLATES_DIR):
    for f in files:
        if f.endswith('.html'):
            with open(os.path.join(root, f), 'r', encoding='utf-8') as fh:
                trans_strings.update(pattern.findall(fh.read()))

for root, dirs, files in os.walk(APPS_DIR):
    for f in files:
        if f.endswith('.py'):
            with open(os.path.join(root, f), 'r', encoding='utf-8') as fh:
                content = fh.read()
                trans_strings.update(py_pattern.findall(content))

print(f'Extracted {len(trans_strings)} unique strings\n')

# === COMPLETE EN TRANSLATIONS ===
EN = {
    # Nav
    "Accueil": "Home", "À propos": "About", "Services": "Services",
    "Réalisations": "Portfolio", "Blog": "Blog", "Contact": "Contact",
    "Navigation": "Navigation",
    # Home hero
    "Agence de Réalité Virtuelle": "Virtual Reality Agency",
    "Sublimez vos projets avec la": "Elevate your projects with",
    "Réalité Virtuelle": "Virtual Reality",
    "VR CREATION COMPANY incarne l'alliance entre esthétique et technologie pour donner vie à vos concepts avant même leur réalisation.": "VR CREATION COMPANY embodies the alliance between aesthetics and technology to bring your concepts to life before they are even realized.",
    "Découvrir nos projets": "Discover Our Projects",
    "Nous contacter": "Contact Us",
    "Expertise": "Expertise", "Reconnue": "Recognized",
    # Home mission
    "Notre Mission": "Our Mission",
    "Pourquoi choisir VR Creation ?": "Why Choose VR Creation?",
    "Nous transformons vos visions en réalités immersives avec une approche centrée sur l'excellence.": "We transform your visions into immersive realities with an excellence-centered approach.",
    "Créativité": "Creativity", "Précision": "Precision", "Professionnalisme": "Professionalism", "Innovation": "Innovation",
    "Sublimer vos projets par des approches visuelles innovantes et esthétiques.": "Enhance your projects with innovative and aesthetic visual approaches.",
    "Un souci du détail minutieux pour des rendus ultra-réalistes.": "Meticulous attention to detail for ultra-realistic renders.",
    "Respect des délais et accompagnement sur-mesure à chaque étape.": "On-time delivery and custom support at every stage.",
    "Utilisation des dernières technologies pour accélérer vos ventes.": "Using the latest technologies to accelerate your sales.",
    # Home services
    "Nos Services": "Our Services", "Notre Expertise": "Our Expertise",
    "Voir tous les services": "View All Services",
    "En savoir plus": "Learn More",
    "Aucun service disponible pour le moment.": "No services available at the moment.",
    # Home strengths
    "Avantages": "Advantages", "Nos Points Forts": "Our Strengths",
    "Différenciation": "Differentiation", "Gain de temps": "Time Savings",
    "Expérience immersive": "Immersive Experience",
    "Rentabilité": "Profitability", "Flexibilité": "Flexibility",
    # Home CTA
    "Prêt à sublimer votre prochain projet ?": "Ready to elevate your next project?",
    "Contactez-nous pour discuter de vos besoins et obtenir un devis personnalisé.": "Contact us to discuss your needs and get a personalized quote.",
    "Démarrer un projet": "Start a Project",
    # About page
    "À Propos de Nous": "About Us", "Notre Histoire": "Our Story",
    "L'alliance entre": "The alliance between", "esthétique": "aesthetics", "et technologie.": "and technology.",
    "VR CREATION COMPANY est une agence spécialisée dans la création de contenus 3D et de visites virtuelles interactives. Nous accompagnons les professionnels de l'immobilier, de l'architecture et de l'aménagement d'intérieur dans la mise en valeur de leurs projets.": "VR CREATION COMPANY is an agency specialized in creating 3D content and interactive virtual tours. We support professionals in real estate, architecture, and interior design to showcase their projects.",
    "Notre équipe d'experts passionnés met son savoir-faire technique et sa sensibilité artistique à votre service pour créer des expériences visuelles immersives et impactantes.": "Our team of passionate experts puts their technical expertise and artistic sensitivity at your service to create immersive and impactful visual experiences.",
    "Notre Processus": "Our Process", "Comment nous travaillons": "How We Work",
    "Analyse et Conseil": "Analysis & Consulting",
    "Étude de vos besoins, récupération de vos plans et brief créatif pour définir l'ambiance.": "Study of your needs, plan retrieval, and creative brief to define the atmosphere.",
    "Étude de vos besoins, récupération de vos plans et brief créatif.": "Study of your needs and retrieval of your plans.",
    "Modélisation 3D": "3D Modeling",
    "Création de l'architecture, du mobilier et des éléments décoratifs en 3D avec une grande précision.": "Creating architecture, furniture, and decorative elements in 3D with great precision.",
    "Création de l'architecture et du mobilier en 3D.": "Creating architecture and furniture in 3D.",
    "Éclairage et Textures": "Lighting & Textures",
    "Application des matériaux réalistes et configuration de la lumière pour une atmosphère parfaite.": "Applying realistic materials and light configuration for a perfect atmosphere.",
    "Rendu et Post-production": "Rendering & Post-production",
    "Génération des images haute résolution et retouches finales pour un résultat optimal.": "High-resolution image generation and final retouching for optimal results.",
    # Contact
    "Contactez-nous": "Contact Us",
    "Vous avez un projet ? Discutons-en et donnons vie à vos idées.": "Have a project? Let's discuss it and bring your ideas to life.",
    "Nos Coordonnées": "Our Contact Info",
    "Adresse": "Address", "Téléphone": "Phone", "Email": "Email",
    "Suivez-nous": "Follow Us",
    "Envoyez-nous un message": "Send Us a Message",
    "Nom complet": "Full Name", "Secteur": "Sector", "Sujet": "Subject", "Message": "Message",
    "Envoyer le message": "Send Message",
    "Nous trouver": "Find Us",
    "Votre nom complet": "Your full name", "votre@email.com": "your@email.com",
    "Votre numéro de téléphone": "Your phone number",
    "Sujet de votre message": "Subject of your message",
    "Décrivez votre projet...": "Describe your project...",
    "Votre réponse": "Your answer",
    "Question de sécurité": "Security Question",
    "Réponse incorrecte. Veuillez réessayer.": "Incorrect answer. Please try again.",
    "Spam detected.": "Spam detected.",
    "Vous avez envoyé trop de messages. Veuillez réessayer dans quelques minutes.": "You have sent too many messages. Please try again in a few minutes.",
    # Contact confirmation
    "Message Envoyé !": "Message Sent!",
    "Merci de nous avoir contactés. Nous avons bien reçu votre message et nous vous répondrons dans les plus brefs délais.": "Thank you for contacting us. We have received your message and will get back to you as soon as possible.",
    "Retour à l'accueil": "Back to Home",
    # Portfolio
    "Notre Portfolio": "Our Portfolio", "Portfolio": "Portfolio",
    "Voir le projet": "View Project",
    "Aucun projet disponible pour le moment.": "No projects available at the moment.",
    "À propos du projet": "About the Project",
    "Le Défi": "The Challenge", "Notre Solution": "Our Solution", "Le Résultat": "The Result",
    "Visite Virtuelle": "Virtual Tour", "Détails": "Details",
    "Client": "Client", "Date": "Date",
    "Projet Similaire ?": "Similar Project?",
    # Case studies
    "Études de Cas": "Case Studies",
    "Découvrez comment nos solutions de réalité virtuelle apportent une valeur mesurable à nos clients.": "Discover how our virtual reality solutions bring measurable value to our clients.",
    "Lire l'étude": "Read the Study",
    "Aucune étude de cas disponible.": "No case studies available.",
    "Le Problème": "The Problem",
    "Importance du Service": "Service Importance",
    "Efficacité": "Efficiency", "Résultat": "Result",
    "Voir le projet détaillé": "View Detailed Project",
    # Virtual tours
    "Visites Virtuelles": "Virtual Tours",
    "Immergez-vous dans nos réalisations interactives et découvrez nos projets sous tous les angles.": "Immerse yourself in our interactive projects and discover them from every angle.",
    "Voir les détails du projet": "View Project Details",
    "Aucune visite virtuelle disponible pour le moment.": "No virtual tours available at the moment.",
    # Services
    "Découvrir ce service": "Discover This Service",
    "Aperçu du Service": "Service Overview",
    "Autres Services": "Other Services",
    "Besoin d'un devis ?": "Need a Quote?",
    "Contactez-nous pour discuter de votre projet et obtenir une estimation gratuite.": "Contact us to discuss your project and get a free estimate.",
    "Nous Contacter": "Contact Us",
    # Blog
    "Actualités & Blog": "News & Blog",
    "Découvrez nos derniers articles, conseils et tendances sur la réalité virtuelle et l'immobilier.": "Discover our latest articles, tips and trends on virtual reality and real estate.",
    "Lire la suite": "Read More",
    "Aucun article publié pour le moment.": "No articles published yet.",
    "Retour aux articles": "Back to Articles",
    "Partager :": "Share:",
    # Footer
    "Nos services": "Our Services",
    "Visites virtuelles": "Virtual Tours", "Captures 360°": "360° Captures",
    "Animation 3D": "3D Animation", "Branding visuel": "Visual Branding",
    "Tous droits réservés.": "All rights reserved.",
    "Mentions légales": "Legal Notices", "Confidentialité": "Privacy", "Cookies": "Cookies",
    # Legal / cookie / privacy pages
    "Mentions Légales": "Legal Notices",
    "Politique de Confidentialité": "Privacy Policy",
    "Politique de Cookies": "Cookie Policy",
    # Cookie banner
    "We use cookies to improve your experience.": "We use cookies to improve your experience.",
    "Accepter": "Accept", "Refuser": "Decline",
    # 404/500
    "Page non trouvée": "Page Not Found",
    "Désolé, la page que vous recherchez n'existe pas ou a été déplacée.": "Sorry, the page you are looking for does not exist or has been moved.",
    "Erreur Serveur": "Server Error",
    "Désolé, une erreur interne est survenue. Veuillez réessayer plus tard.": "Sorry, an internal error occurred. Please try again later.",
    # Misc
    "Thank You!": "Thank You!",
    # Python form/model strings (keep French as source)
    "Nom": "Name", "Prénom": "First Name",
    "Titre": "Title", "Slug": "Slug", "Description": "Description",
    "Icône": "Icon", "Ordre": "Order", "Secteur": "Sector",
    "Secteurs": "Sectors", "Projet": "Project", "Projets": "Projects",
    "Créé le": "Created on", "Modifié le": "Modified on",
    "Mis en avant": "Featured",
    "Visite virtuelle": "Virtual Tour",
    "Image principale": "Main Image",
    "Date de réalisation": "Completion Date",
    "URL visite virtuelle": "Virtual Tour URL",
    "URL iframe de la visite virtuelle 360° (Pannellum, Matterport, etc.)": "360° virtual tour iframe URL (Pannellum, Matterport, etc.)",
    "Défi / Problématique": "Challenge / Issue",
    "Solution apportée": "Solution Provided",
    "Résultat obtenu": "Result Achieved",
    # Admin / Model fields
    "Actif": "Active",
    "Ajouter noindex à cette page": "Add noindex to this page",
    "Aperçu": "Preview",
    "Architecture": "Architecture",
    "Article": "Article", "Articles": "Articles",
    "Auteur": "Author", "Autre": "Other",
    "Behance": "Behance", "Biographie": "Biography",
    "Catégorie": "Category", "Catégories": "Categories",
    "Chiffre clé": "Key Figure",
    "Classe d'icône (ex: fas fa-lightbulb) ou emoji": "Icon class (e.g. fas fa-lightbulb) or emoji",
    "Classe d'icône ou emoji": "Icon class or emoji",
    "Code de vérification Google Search Console (contenu de la balise meta)": "Google Search Console verification code (meta tag content)",
    "Collecte des données": "Data Collection",
    "Combien font %(num1)d + %(num2)d ?": "What is %(num1)d + %(num2)d?",
    "Contenu": "Content",
    "Coordonnées": "Contact Information",
    "Date de publication": "Publication Date",
    "Description SEO": "SEO Description",
    "Description complète": "Full Description",
    "Description courte": "Short Description",
    "Efficacité / Impact": "Efficiency / Impact",
    "Email de contact": "Contact Email",
    "En poursuivant votre navigation sur ce site, vous acceptez l'utilisation de cookies pour améliorer votre expérience utilisateur et réaliser des statistiques de visites.": "By continuing to browse this site, you accept the use of cookies to improve your user experience and generate visitor statistics.",
    "Envoyé le": "Sent on",
    "Ex: 150+, 98%, 10 ans": "E.g.: 150+, 98%, 10 years",
    "Ex: G-XXXXXXXXXX. Chargé uniquement après consentement cookies.": "E.g.: G-XXXXXXXXXX. Loaded only after cookie consent.",
    "Expéditeur": "Sender",
    "Extrait": "Excerpt",
    "Facebook": "Facebook", "Favicon": "Favicon",
    "Google / Analytics / SEO": "Google / Analytics / SEO",
    "Google Analytics ID": "Google Analytics ID",
    "Google Search Console": "Google Search Console",
    "Hébergement": "Hosting",
    "ID objet": "Object ID",
    "Icône CSS": "CSS Icon",
    "Identifiant de page": "Page Identifier",
    "Identifiant unique : home, about, services, portfolio, contact, blog, etc.": "Unique identifier: home, about, services, portfolio, contact, blog, etc.",
    "Identité du site": "Site Identity",
    "Image 1200x630px recommandée": "1200x630px image recommended",
    "Image 360°": "360° Image",
    "Image OG par défaut": "Default OG Image",
    "Image Open Graph": "Open Graph Image",
    "Image de fond du hero de la page d'accueil": "Homepage hero background image",
    "Image du projet": "Project Image",
    "Image du service": "Service Image",
    "Image hero accueil": "Homepage Hero Image",
    "Image page À propos": "About Page Image",
    "Image par défaut pour le partage social (1200x630px recommandé)": "Default image for social sharing (1200x630px recommended)",
    "Images du projet": "Project Images",
    "Images du service": "Service Images",
    "Images principales": "Main Images",
    "Immobilier": "Real Estate",
    "Importance du service": "Service Importance",
    "Instagram": "Instagram", "LinkedIn": "LinkedIn", "Logo": "Logo",
    "Lu": "Read",
    "Membre de l'équipe": "Team Member",
    "Membres de l'équipe": "Team Members",
    "Message de contact": "Contact Message",
    "Messages de contact": "Contact Messages",
    "Métadonnées": "Metadata",
    "Ne pas indexer": "Do Not Index",
    "Nom du site": "Site Name",
    "Numéro WhatsApp au format international (ex: +33612345678)": "WhatsApp number in international format (e.g.: +33612345678)",
    "Page introuvable": "Page Not Found",
    "Paramètres du site": "Site Settings",
    "Photo": "Photo",
    "Pied de page": "Footer",
    "Point fort": "Strength", "Points forts": "Strengths",
    "Politique des Cookies": "Cookie Policy",
    "Problème / Contexte": "Problem / Context",
    "Projet lié": "Related Project",
    "Propriété intellectuelle": "Intellectual Property",
    "Publié": "Published",
    "Qu'est-ce qu'un cookie ?": "What is a cookie?",
    "Retail / Commerce": "Retail / Commerce",
    "Réseaux sociaux": "Social Networks",
    "Résumé affiché dans les cartes (max 300 caractères)": "Summary displayed in cards (max 300 characters)",
    "Résumé de l'article (max 500 caractères)": "Article summary (max 500 characters)",
    "Rôle": "Role",
    "SEO — Métadonnées objet": "SEO — Object Metadata",
    "SEO — Métadonnées objets": "SEO — Object Metadata",
    "SEO — Page statique": "SEO — Static Page",
    "SEO — Pages statiques": "SEO — Static Pages",
    "Secteur d'activité": "Business Sector",
    "Slogan": "Slogan",
    "Statut": "Status",
    "Temps de lecture (min)": "Reading Time (min)",
    "Texte alternatif": "Alt Text",
    "Texte copyright": "Copyright Text",
    "Texte du pied de page": "Footer Text",
    "TikTok": "TikTok", "Twitter / X": "Twitter / X",
    "Titre SEO": "SEO Title",
    "Tourisme": "Tourism",
    "Type de contenu": "Content Type",
    "URL Google Maps (embed)": "Google Maps URL (embed)",
    "URL canonique": "Canonical URL",
    "URL iframe Google Maps pour la page contact": "Google Maps iframe URL for contact page",
    "Une erreur inattendue s'est produite. Nos équipes ont été alertées.": "An unexpected error occurred. Our teams have been notified.",
    "Utilisation des données": "Data Usage",
    "Valeur": "Value", "Valeurs": "Values",
    "WhatsApp": "WhatsApp", "YouTube": "YouTube",
    # URL slugs (keep same)
    "a-propos/": "a-propos/", "blog/": "blog/", "confidentialite/": "confidentialite/",
    "contact/": "contact/", "contact/merci/": "contact/merci/", "cookies/": "cookies/",
    "etudes-de-cas/": "etudes-de-cas/", "mentions-legales/": "mentions-legales/",
    "realisations/": "realisations/", "services/": "services/", "visites-virtuelles/": "visites-virtuelles/",
    # Admin sections
    "Éditeur du site": "Site Editor",
    "Étape du processus": "Process Step", "Étapes du processus": "Process Steps",
    "Étude de cas": "Case Study", "Études de cas": "Case Studies",
    "Événementiel": "Events",
    # Escaped-quote strings
    "Classe d\'icône (ex: fas fa-lightbulb) ou emoji": "Icon class (e.g. fas fa-lightbulb) or emoji",
    "Classe d\'icône ou emoji": "Icon class or emoji",
    "Image de fond du hero de la page d\'accueil": "Homepage hero background image",
    "Label du chiffre": "Figure Label",
    "Membre de l\'\u00e9quipe": "Team Member",
    "Membres de l\'\u00e9quipe": "Team Members",
    "R\u00e9sum\u00e9 de l\'article (max 500 caract\u00e8res)": "Article summary (max 500 characters)",
    "Secteur d\'activit\u00e9": "Business Sector",
    "Image": "Image",
    "Service": "Service",
    # Cookie Consent Banner Strings
    "Gestion des cookies": "Cookie management",
    "Personnaliser mes choix": "Customize my choices",
    "Cookies Nécessaires": "Necessary Cookies",
    "Requis pour le bon fonctionnement et la sécurité du site.": "Required for the proper functioning and security of the site.",
    "Toujours actif": "Always active",
    "Cookies de statistiques et d'analyse": "Statistics and analysis cookies",
    "Permettent de mesurer l'audience et d'analyser l'utilisation du site pour l'améliorer.": "Allow measuring audience and analyzing site usage to improve it.",
    "Cookies de marketing et réseaux sociaux": "Marketing and social media cookies",
    "Permettent de vous proposer des publicités personnalisées et de partager du contenu.": "Allow offering personalized advertisements and sharing content.",
    "Enregistrer mes choix": "Save my choices",
    "Retour": "Back",
    "Personnaliser": "Customize",
    # Cookie Policy Details
    "Préférences de cookies": "Cookie preferences",
    "Vous pouvez à tout moment modifier vos préférences de cookies, accepter ou refuser le chargement des scripts analytiques ou marketing.": "You can modify your cookie preferences at any time, accepting or declining the loading of analytical or marketing scripts.",
    "Gérer mes choix": "Manage my choices",
    "Un cookie est un petit fichier texte déposé sur votre terminal (ordinateur, tablette ou smartphone) lors de la visite d'un site internet. Il permet de conserver des données utilisateur afin de faciliter la navigation et de permettre certaines fonctionnalités.": "A cookie is a small text file deposited on your device (computer, tablet, or smartphone) when visiting a website. It stores user data to make navigation easier and enable certain features.",
    "Quels cookies utilisons-nous ?": "Which cookies do we use?",
    "Cookies nécessaires": "Necessary cookies",
    "Ces cookies sont essentiels au fonctionnement du site et ne peuvent pas être désactivés dans nos systèmes.": "These cookies are essential for the website to function and cannot be disabled in our systems.",
    "Cookies analytiques (Google Analytics)": "Analytical cookies (Google Analytics)",
    "Ces cookies nous aident à mesurer l'audience de notre site, à analyser la navigation et à identifier d'éventuels dysfonctionnements pour améliorer votre expérience utilisateur.": "These cookies help us measure our website's audience, analyze navigation, and identify potential malfunctions to improve your user experience.",
    "Cookies de marketing et de partage": "Marketing and sharing cookies",
    "Ces cookies sont liés au partage sur les réseaux sociaux et peuvent être installés pour suivre l'activité sur d'autres sites.": "These cookies are linked to sharing on social networks and can be installed to track activity on other websites.",
    "Durée de conservation": "Retention period",
    "Conformément à la réglementation RGPD, le consentement donné pour le dépôt de cookies a une durée de validité de 13 mois maximum. À l'issue de cette période, votre consentement sera à nouveau demandé.": "In accordance with GDPR regulations, consent given for cookies has a maximum validity of 13 months. At the end of this period, your consent will be requested again.",
    # Slider navigation
    "Précédent": "Previous",
    "Suivant": "Next",
    # HeroSlide Model Names
    "Diapositive Hero": "Hero Slide",
    "Diapositives Hero": "Hero Slides",
    # Immersive Mode and Floating Controls
    "Mode Immersif VR": "VR Immersive Mode",
    "Retour en haut": "Back to top",
    # VR mode explanation
    "Mode Cyber-VR": "Cyber-VR Mode",
    "Simule un espace virtuel 3D (ambiance néon et particules cosmiques).": "Simulates an interactive 3D space (neon styling & cosmic particles).",
    "Simule un espace virtuel 3D en transformant le site avec un design néon et des particules cosmiques flottantes !": "Simulates an interactive 3D space by transforming the site with a neon design and floating cosmic particles!",
}

# === COMPLETE AR TRANSLATIONS ===
AR = {
    # Nav
    "Accueil": "الرئيسية", "À propos": "من نحن", "Services": "الخدمات",
    "Réalisations": "الأعمال", "Blog": "المدونة", "Contact": "اتصل بنا",
    "Navigation": "التنقل",
    # Home hero
    "Agence de Réalité Virtuelle": "وكالة الواقع الافتراضي",
    "Sublimez vos projets avec la": "ارتقِ بمشاريعك مع",
    "Réalité Virtuelle": "الواقع الافتراضي",
    "VR CREATION COMPANY incarne l'alliance entre esthétique et technologie pour donner vie à vos concepts avant même leur réalisation.": "شركة VR CREATION تجسد التحالف بين الجمال والتكنولوجيا لإحياء مفاهيمك قبل تحقيقها.",
    "Découvrir nos projets": "اكتشف مشاريعنا",
    "Nous contacter": "اتصل بنا",
    "Expertise": "خبرة", "Reconnue": "معترف بها",
    # Home mission
    "Notre Mission": "مهمتنا",
    "Pourquoi choisir VR Creation ?": "لماذا تختار VR Creation؟",
    "Nous transformons vos visions en réalités immersives avec une approche centrée sur l'excellence.": "نحول رؤاك إلى واقع غامر بنهج يركز على التميز.",
    "Créativité": "الإبداع", "Précision": "الدقة", "Professionnalisme": "الاحترافية", "Innovation": "الابتكار",
    "Sublimer vos projets par des approches visuelles innovantes et esthétiques.": "تحسين مشاريعك بأساليب بصرية مبتكرة وجمالية.",
    "Un souci du détail minutieux pour des rendus ultra-réalistes.": "اهتمام دقيق بالتفاصيل لتصييرات فائقة الواقعية.",
    "Respect des délais et accompagnement sur-mesure à chaque étape.": "الالتزام بالمواعيد والمرافقة المخصصة في كل مرحلة.",
    "Utilisation des dernières technologies pour accélérer vos ventes.": "استخدام أحدث التقنيات لتسريع مبيعاتك.",
    # Home services
    "Nos Services": "خدماتنا", "Notre Expertise": "خبراتنا",
    "Voir tous les services": "عرض جميع الخدمات",
    "En savoir plus": "اعرف المزيد",
    "Aucun service disponible pour le moment.": "لا توجد خدمات متاحة حالياً.",
    # Home strengths
    "Avantages": "المزايا", "Nos Points Forts": "نقاط قوتنا",
    "Différenciation": "التميز", "Gain de temps": "توفير الوقت",
    "Expérience immersive": "تجربة غامرة",
    "Rentabilité": "الربحية", "Flexibilité": "المرونة",
    # Home CTA
    "Prêt à sublimer votre prochain projet ?": "مستعد للارتقاء بمشروعك القادم؟",
    "Contactez-nous pour discuter de vos besoins et obtenir un devis personnalisé.": "تواصل معنا لمناقشة احتياجاتك والحصول على عرض أسعار مخصص.",
    "Démarrer un projet": "ابدأ مشروعاً",
    # About page
    "À Propos de Nous": "عنّا", "Notre Histoire": "تاريخنا",
    "L'alliance entre": "التحالف بين", "esthétique": "الجمال", "et technologie.": "والتكنولوجيا.",
    "VR CREATION COMPANY est une agence spécialisée dans la création de contenus 3D et de visites virtuelles interactives. Nous accompagnons les professionnels de l'immobilier, de l'architecture et de l'aménagement d'intérieur dans la mise en valeur de leurs projets.": "شركة VR CREATION هي وكالة متخصصة في إنشاء محتوى ثلاثي الأبعاد وجولات افتراضية تفاعلية. نرافق المهنيين في العقارات والهندسة المعمارية والتصميم الداخلي لإبراز مشاريعهم.",
    "Notre équipe d'experts passionnés met son savoir-faire technique et sa sensibilité artistique à votre service pour créer des expériences visuelles immersives et impactantes.": "فريقنا من الخبراء الشغوفين يضع خبرته التقنية وحسه الفني في خدمتك لإنشاء تجارب بصرية غامرة ومؤثرة.",
    "Notre Processus": "عمليتنا", "Comment nous travaillons": "كيف نعمل",
    "Analyse et Conseil": "التحليل والاستشارة",
    "Étude de vos besoins, récupération de vos plans et brief créatif pour définir l'ambiance.": "دراسة احتياجاتك، استلام المخططات وملخص إبداعي لتحديد الأجواء.",
    "Étude de vos besoins, récupération de vos plans et brief créatif.": "دراسة احتياجاتك واستلام المخططات.",
    "Modélisation 3D": "النمذجة ثلاثية الأبعاد",
    "Création de l'architecture, du mobilier et des éléments décoratifs en 3D avec une grande précision.": "إنشاء الهندسة المعمارية والأثاث والعناصر الزخرفية بدقة عالية بتقنية 3D.",
    "Création de l'architecture et du mobilier en 3D.": "إنشاء الهندسة والأثاث بتقنية 3D.",
    "Éclairage et Textures": "الإضاءة والقوام",
    "Application des matériaux réalistes et configuration de la lumière pour une atmosphère parfaite.": "تطبيق المواد الواقعية وإعداد الإضاءة لأجواء مثالي.",
    "Rendu et Post-production": "التصيير وما بعد الإنتاج",
    "Génération des images haute résolution et retouches finales pour un résultat optimal.": "إنشاء صور عالية الدقة ولمسات نهائية لنتيجة مثالية.",
    # Contact
    "Contactez-nous": "اتصل بنا",
    "Vous avez un projet ? Discutons-en et donnons vie à vos idées.": "لديك مشروع؟ دعنا نناقشه ونحقق أفكارك.",
    "Nos Coordonnées": "معلومات الاتصال",
    "Adresse": "العنوان", "Téléphone": "الهاتف", "Email": "البريد الإلكتروني",
    "Suivez-nous": "تابعنا",
    "Envoyez-nous un message": "أرسل لنا رسالة",
    "Nom complet": "الاسم الكامل", "Secteur": "القطاع", "Sujet": "الموضوع", "Message": "الرسالة",
    "Envoyer le message": "إرسال الرسالة",
    "Nous trouver": "موقعنا",
    "Votre nom complet": "اسمك الكامل", "votre@email.com": "بريدك@مثال.com",
    "Votre numéro de téléphone": "رقم هاتفك",
    "Sujet de votre message": "موضوع رسالتك",
    "Décrivez votre projet...": "صف مشروعك...",
    "Votre réponse": "إجابتك",
    "Question de sécurité": "سؤال أمان",
    "Réponse incorrecte. Veuillez réessayer.": "إجابة خاطئة. يرجى المحاولة مرة أخرى.",
    "Spam detected.": "تم اكتشاف رسائل غير مرغوب فيها.",
    "Vous avez envoyé trop de messages. Veuillez réessayer dans quelques minutes.": "لقد أرسلت رسائل كثيرة. يرجى المحاولة بعد بضع دقائق.",
    # Contact confirmation
    "Message Envoyé !": "تم إرسال الرسالة!",
    "Merci de nous avoir contactés. Nous avons bien reçu votre message et nous vous répondrons dans les plus brefs délais.": "شكراً لتواصلكم معنا. لقد تلقينا رسالتكم وسنرد عليكم في أقرب وقت ممكن.",
    "Retour à l'accueil": "العودة للرئيسية",
    # Portfolio
    "Notre Portfolio": "معرض أعمالنا", "Portfolio": "الأعمال",
    "Voir le projet": "عرض المشروع",
    "Aucun projet disponible pour le moment.": "لا توجد مشاريع متاحة حالياً.",
    "À propos du projet": "عن المشروع",
    "Le Défi": "التحدي", "Notre Solution": "حلنا", "Le Résultat": "النتيجة",
    "Visite Virtuelle": "جولة افتراضية", "Détails": "التفاصيل",
    "Client": "العميل", "Date": "التاريخ",
    "Projet Similaire ?": "مشروع مماثل؟",
    # Case studies
    "Études de Cas": "دراسات الحالة",
    "Découvrez comment nos solutions de réalité virtuelle apportent une valeur mesurable à nos clients.": "اكتشف كيف توفر حلول الواقع الافتراضي لدينا قيمة قابلة للقياس لعملائنا.",
    "Lire l'étude": "قراءة الدراسة",
    "Aucune étude de cas disponible.": "لا توجد دراسات حالة متاحة.",
    "Le Problème": "المشكلة",
    "Importance du Service": "أهمية الخدمة",
    "Efficacité": "الكفاءة", "Résultat": "النتيجة",
    "Voir le projet détaillé": "عرض المشروع بالتفصيل",
    # Virtual tours
    "Visites Virtuelles": "الجولات الافتراضية",
    "Immergez-vous dans nos réalisations interactives et découvrez nos projets sous tous les angles.": "انغمس في أعمالنا التفاعلية واكتشف مشاريعنا من كل الزوايا.",
    "Voir les détails du projet": "عرض تفاصيل المشروع",
    "Aucune visite virtuelle disponible pour le moment.": "لا توجد جولات افتراضية متاحة حالياً.",
    # Services
    "Découvrir ce service": "اكتشف هذه الخدمة",
    "Aperçu du Service": "نظرة عامة على الخدمة",
    "Autres Services": "خدمات أخرى",
    "Besoin d'un devis ?": "تحتاج عرض أسعار؟",
    "Contactez-nous pour discuter de votre projet et obtenir une estimation gratuite.": "تواصل معنا لمناقشة مشروعك والحصول على تقدير مجاني.",
    "Nous Contacter": "اتصل بنا",
    # Blog
    "Actualités & Blog": "الأخبار والمدونة",
    "Découvrez nos derniers articles, conseils et tendances sur la réalité virtuelle et l'immobilier.": "اكتشف أحدث مقالاتنا ونصائحنا واتجاهاتنا حول الواقع الافتراضي والعقارات.",
    "Lire la suite": "اقرأ المزيد",
    "Aucun article publié pour le moment.": "لا توجد مقالات منشورة حالياً.",
    "Retour aux articles": "العودة إلى المقالات",
    "Partager :": "مشاركة:",
    # Footer
    "Nos services": "خدماتنا",
    "Visites virtuelles": "الجولات الافتراضية", "Captures 360°": "تصوير 360°",
    "Animation 3D": "الرسوم المتحركة 3D", "Branding visuel": "العلامة التجارية البصرية",
    "Tous droits réservés.": "جميع الحقوق محفوظة.",
    "Mentions légales": "إشعارات قانونية", "Confidentialité": "الخصوصية", "Cookies": "ملفات تعريف الارتباط",
    # Legal
    "Mentions Légales": "إشعارات قانونية",
    "Politique de Confidentialité": "سياسة الخصوصية",
    "Politique de Cookies": "سياسة ملفات تعريف الارتباط",
    # Cookie banner
    "We use cookies to improve your experience.": "نستخدم ملفات تعريف الارتباط لتحسين تجربتك.",
    "Accepter": "قبول", "Refuser": "رفض",
    # 404/500
    "Page non trouvée": "الصفحة غير موجودة",
    "Désolé, la page que vous recherchez n'existe pas ou a été déplacée.": "عذراً، الصفحة التي تبحث عنها غير موجودة أو تم نقلها.",
    "Erreur Serveur": "خطأ في الخادم",
    "Désolé, une erreur interne est survenue. Veuillez réessayer plus tard.": "عذراً، حدث خطأ داخلي. يرجى المحاولة لاحقاً.",
    "Thank You!": "شكراً!",
    "Nom": "اللقب", "Prénom": "الاسم الأول",
    # Escaped-quote + missing model strings
    "Classe d\'icône (ex: fas fa-lightbulb) ou emoji": "فئة الأيقونة (مثال: fas fa-lightbulb) أو إيموجي",
    "Classe d\'icône ou emoji": "فئة الأيقونة أو إيموجي",
    "Image de fond du hero de la page d\'accueil": "صورة خلفية البانر الرئيسي",
    "Label du chiffre": "علامة الرقم",
    "Membre de l\'\u00e9quipe": "عضو الفريق",
    "Membres de l\'\u00e9quipe": "أعضاء الفريق",
    "R\u00e9sum\u00e9 de l\'article (max 500 caract\u00e8res)": "ملخص المقال (حد أقصى 500 حرف)",
    "Secteur d\'activit\u00e9": "قطاع النشاط",
    "Image": "صورة",
    "Service": "خدمة",
    "Cr\u00e9\u00e9 le": "أنشئ في", "Modifi\u00e9 le": "عُدل في",
    "Date de r\u00e9alisation": "تاريخ الإنجاز",
    "Description": "الوصف",
    "D\u00e9fi / Probl\u00e9matique": "التحدي / الإشكالية",
    "Ic\u00f4ne": "أيقونة", "Ordre": "الترتيب",
    "Image principale": "الصورة الرئيسية",
    "Mis en avant": "مميز",
    "Projet": "مشروع", "Projets": "مشاريع",
    "R\u00e9sultat obtenu": "النتيجة المحققة",
    "Solution apport\u00e9e": "الحل المقدم",
    "URL visite virtuelle": "رابط الجولة الافتراضية",
    "Visite virtuelle": "جولة افتراضية",
    "URL iframe de la visite virtuelle 360\u00b0 (Pannellum, Matterport, etc.)": "رابط iframe للجولة الافتراضية 360\u00b0",
    "Titre": "عنوان", "Slug": "Slug", "Secteur": "القطاع",
    "Secteurs": "القطاعات",
    "Ajouter noindex à cette page": "إضافة noindex لهذه الصفحة",
    "Aperçu": "معاينة",
    "Architecture": "هندسة معمارية",
    "Article": "مقال", "Articles": "مقالات",
    "Auteur": "الكاتب", "Autre": "أخرى",
    "Behance": "Behance", "Biographie": "السيرة الذاتية",
    "Catégorie": "الفئة", "Catégories": "الفئات",
    "Chiffre clé": "رقم رئيسي",
    "Classe d'icône (ex: fas fa-lightbulb) ou emoji": "فئة الأيقونة (مثال: fas fa-lightbulb) أو إيموجي",
    "Classe d'icône ou emoji": "فئة الأيقونة أو إيموجي",
    "Code de vérification Google Search Console (contenu de la balise meta)": "رمز التحقق من Google Search Console (محتوى علامة meta)",
    "Collecte des données": "جمع البيانات",
    "Combien font %(num1)d + %(num2)d ?": "كم يساوي %(num1)d + %(num2)d؟",
    "Contenu": "المحتوى",
    "Coordonnées": "معلومات الاتصال",
    "Date de publication": "تاريخ النشر",
    "Description SEO": "وصف SEO",
    "Description complète": "الوصف الكامل",
    "Description courte": "وصف مختصر",
    "Efficacité / Impact": "الكفاءة / التأثير",
    "Email de contact": "بريد الاتصال",
    "En poursuivant votre navigation sur ce site, vous acceptez l'utilisation de cookies pour améliorer votre expérience utilisateur et réaliser des statistiques de visites.": "بمتابعة تصفح هذا الموقع، فإنك توافق على استخدام ملفات تعريف الارتباط لتحسين تجربة المستخدم وإنشاء إحصائيات الزيارات.",
    "Envoyé le": "أُرسل في",
    "Ex: 150+, 98%, 10 ans": "مثال: +150، 98%، 10 سنوات",
    "Ex: G-XXXXXXXXXX. Chargé uniquement après consentement cookies.": "مثال: G-XXXXXXXXXX. يتم تحميله فقط بعد الموافقة على ملفات تعريف الارتباط.",
    "Expéditeur": "المُرسل",
    "Extrait": "مقتطف",
    "Facebook": "فيسبوك", "Favicon": "Favicon",
    "Google / Analytics / SEO": "Google / Analytics / SEO",
    "Google Analytics ID": "معرف Google Analytics",
    "Google Search Console": "Google Search Console",
    "Hébergement": "الاستضافة",
    "ID objet": "معرف الكائن",
    "Icône CSS": "أيقونة CSS",
    "Identifiant de page": "معرف الصفحة",
    "Identifiant unique : home, about, services, portfolio, contact, blog, etc.": "معرف فريد: home, about, services, portfolio, contact, blog, إلخ.",
    "Identité du site": "هوية الموقع",
    "Image 1200x630px recommandée": "صورة 1200x630 بكسل موصى بها",
    "Image 360°": "صورة 360°",
    "Image OG par défaut": "صورة OG الافتراضية",
    "Image Open Graph": "صورة Open Graph",
    "Image de fond du hero de la page d'accueil": "صورة خلفية البانر الرئيسي للصفحة الرئيسية",
    "Image du projet": "صورة المشروع",
    "Image du service": "صورة الخدمة",
    "Image hero accueil": "صورة البانر الرئيسي",
    "Image page À propos": "صورة صفحة من نحن",
    "Image par défaut pour le partage social (1200x630px recommandé)": "صورة افتراضية للمشاركة الاجتماعية (1200x630 بكسل موصى بها)",
    "Images du projet": "صور المشروع",
    "Images du service": "صور الخدمة",
    "Images principales": "الصور الرئيسية",
    "Immobilier": "عقارات",
    "Importance du service": "أهمية الخدمة",
    "Instagram": "إنستغرام", "LinkedIn": "لينكد إن", "Logo": "شعار",
    "Lu": "مقروء",
    "Membre de l'équipe": "عضو الفريق",
    "Membres de l'équipe": "أعضاء الفريق",
    "Message de contact": "رسالة اتصال",
    "Messages de contact": "رسائل الاتصال",
    "Métadonnées": "البيانات الوصفية",
    "Ne pas indexer": "عدم الفهرسة",
    "Nom du site": "اسم الموقع",
    "Numéro WhatsApp au format international (ex: +33612345678)": "رقم واتساب بالصيغة الدولية (مثال: +33612345678)",
    "Page introuvable": "الصفحة غير موجودة",
    "Paramètres du site": "إعدادات الموقع",
    "Photo": "صورة",
    "Pied de page": "تذييل الصفحة",
    "Point fort": "نقطة قوة", "Points forts": "نقاط القوة",
    "Politique des Cookies": "سياسة ملفات تعريف الارتباط",
    "Problème / Contexte": "المشكلة / السياق",
    "Projet lié": "مشروع مرتبط",
    "Propriété intellectuelle": "الملكية الفكرية",
    "Publié": "منشور",
    "Qu'est-ce qu'un cookie ?": "ما هو ملف تعريف الارتباط؟",
    "Retail / Commerce": "تجارة التجزئة",
    "Réseaux sociaux": "شبكات التواصل الاجتماعي",
    "Résumé affiché dans les cartes (max 300 caractères)": "ملخص يظهر في البطاقات (حد أقصى 300 حرف)",
    "Résumé de l'article (max 500 caractères)": "ملخص المقال (حد أقصى 500 حرف)",
    "Rôle": "الدور",
    "SEO — Métadonnées objet": "SEO — بيانات وصفية للكائن",
    "SEO — Métadonnées objets": "SEO — بيانات وصفية للكائنات",
    "SEO — Page statique": "SEO — صفحة ثابتة",
    "SEO — Pages statiques": "SEO — صفحات ثابتة",
    "Secteur d'activité": "قطاع النشاط",
    "Slogan": "شعار",
    "Statut": "الحالة",
    "Temps de lecture (min)": "وقت القراءة (دقيقة)",
    "Texte alternatif": "نص بديل",
    "Texte copyright": "نص حقوق النشر",
    "Texte du pied de page": "نص التذييل",
    "TikTok": "تيك توك", "Twitter / X": "تويتر / X",
    "Titre SEO": "عنوان SEO",
    "Tourisme": "سياحة",
    "Type de contenu": "نوع المحتوى",
    "URL Google Maps (embed)": "رابط خرائط جوجل (مضمن)",
    "URL canonique": "الرابط الأساسي",
    "URL iframe Google Maps pour la page contact": "رابط iframe خرائط جوجل لصفحة الاتصال",
    "Une erreur inattendue s'est produite. Nos équipes ont été alertées.": "حدث خطأ غير متوقع. تم تنبيه فرقنا.",
    "Utilisation des données": "استخدام البيانات",
    "Valeur": "قيمة", "Valeurs": "القيم",
    "WhatsApp": "واتساب", "YouTube": "يوتيوب",
    # URL slugs (keep same)
    "a-propos/": "a-propos/", "blog/": "blog/", "confidentialite/": "confidentialite/",
    "contact/": "contact/", "contact/merci/": "contact/merci/", "cookies/": "cookies/",
    "etudes-de-cas/": "etudes-de-cas/", "mentions-legales/": "mentions-legales/",
    "realisations/": "realisations/", "services/": "services/", "visites-virtuelles/": "visites-virtuelles/",
    # Admin sections
    "Éditeur du site": "محرر الموقع",
    "Étape du processus": "خطوة العملية", "Étapes du processus": "خطوات العملية",
    "Étude de cas": "دراسة حالة", "Études de cas": "دراسات الحالة",
    "Événementiel": "فعاليات",
    # Cookie Consent Banner Strings
    "Gestion des cookies": "إدارة ملفات تعريف الارتباط",
    "Personnaliser mes choix": "تخصيص خياراتي",
    "Cookies Nécessaires": "ملفات تعريف الارتباط الضرورية",
    "Requis pour le bon fonctionnement et la sécurité du site.": "مطلوبة للتشغيل السليم للموقع وأمانه.",
    "Toujours actif": "نشط دائماً",
    "Cookies de statistiques et d'analyse": "ملفات تعريف ارتباط الإحصاءات والتحليل",
    "Permettent de mesurer l'audience et d'analyser l'utilisation du site pour l'améliorer.": "تتيح قياس الجمهور وتحليل استخدام الموقع لتحسينه.",
    "Cookies de marketing et réseaux sociaux": "ملفات تعريف ارتباط التسويق ووسائل التواصل الاجتماعي",
    "Permettent de vous proposer des publicités personnalisées et de partager du contenu.": "تتيح تقديم إعلانات مخصصة ومشاركة المحتوى.",
    "Enregistrer mes choix": "حفظ خياراتي",
    "Retour": "عودة",
    "Personnaliser": "تخصيص",
    # Cookie Policy Details
    "Préférences de cookies": "تفضيلات ملفات تعريف الارتباط",
    "Vous pouvez à tout moment modifier vos préférences de cookies, accepter ou refuser le chargement des scripts analytiques ou marketing.": "يمكنك تعديل تفضيلات ملفات تعريف الارتباط الخاصة بك في أي وقت، وقبول أو رفض تحميل نصوص التحليل أو التسويق.",
    "Gérer mes choix": "إدارة خياراتي",
    "Un cookie est un petit fichier texte déposé sur votre terminal (ordinateur, tablette ou smartphone) lors de la visite d'un site internet. Il permet de conserver des données utilisateur afin de faciliter la navigation et de permettre certaines fonctionnalités.": "ملف تعريف الارتباط (الكوكيز) هو ملف نصي صغير يتم حفظه على جهازك (كمبيوتر، جهاز لوحي أو هاتف ذكي) عند زيارة موقع ويب. وهو يسمح بحفظ بيانات المستخدم لتسهيل التصفح وتفعيل ميزات معينة.",
    "Quels cookies utilisons-nous ?": "ما هي ملفات تعريف الارتباط التي نستخدمها؟",
    "Cookies nécessaires": "ملفات تعريف الارتباط الضرورية",
    "Ces cookies sont essentiels au fonctionnement du site et ne peuvent pas être désactivés dans nos systèmes.": "ملفات تعريف الارتباط هذه ضرورية لتشغيل الموقع ولا يمكن إلغاء تفعيلها في أنظمتنا.",
    "Cookies analytiques (Google Analytics)": "ملفات تعريف الارتباط التحليلية (جوجل أناليتكس)",
    "Ces cookies nous aident à mesurer l'audience de notre site, à analyser la navigation et à identifier d'éventuels dysfonctionnements pour améliorer votre expérience utilisateur.": "تساعدنا ملفات تعريف الارتباط هذه في قياس جمهور موقعنا، وتحليل التصفح وتحديد أي أعطال لتحسين تجربة المستخدم الخاصة بك.",
    "Cookies de marketing et de partage": "ملفات تعريف ارتباط التسويق والمشاركة",
    "Ces cookies sont liés au partage sur les réseaux sociaux et peuvent être installés pour suivre l'activité sur d'autres sites.": "ترتبط ملفات تعريف الارتباط هذه بالمشاركة على الشبكات الاجتماعية ويمكن تثبيتها لتتبع النشاط على مواقع أخرى.",
    "Durée de conservation": "مدة الاحتفاظ بها",
    "Conformément à la réglementation RGPD, le consentement donné pour le dépôt de cookies a une durée de validité de 13 mois maximum. À l'issue de cette période, votre consentement sera à nouveau demandé.": "وفقًا للوائح العامة لحماية البيانات (GDPR)، فإن صلاحية الموافقة الممنوحة لملفات تعريف الارتباط هي 13 شهرًا كحد أقصى. وفي نهاية هذه الفترة، سيتم طلب موافقتك مرة أخرى.",
    # Slider navigation
    "Précédent": "السابق",
    "Suivant": "التالي",
    # HeroSlide Model Names
    "Diapositive Hero": "شريحة البانر الرئيسي",
    "Diapositives Hero": "شرائح البانر الرئيسي",
    # Immersive Mode and Floating Controls
    "Mode Immersif VR": "وضع الواقع الافتراضي",
    "Retour en haut": "العودة للأعلى",
    # VR mode explanation
    "Mode Cyber-VR": "وضع الواقع الافتراضي السيبراني",
    "Simule un espace virtuel 3D (ambiance néon et particules cosmiques).": "يحاكي مساحة ثلاثية الأبعاد تفاعلية (تصميم نيون وجزيئات كونية).",
    "Simule un espace virtuel 3D en transformant le site avec un design néon et des particules cosmiques flottantes !": "يحاكي مساحة ثلاثية الأبعاد تفاعلية عن طريق تحويل الموقع بتصميم نيون وجزيئات كونية عائمة!",
}

# FR just maps to itself
FR = {s: s for s in trans_strings}

def generate_po(lang, translations, strings):
    header = f'''# VR Creation - {lang} translations
msgid ""
msgstr ""
"Project-Id-Version: VR Creation 1.0\\n"
"Language: {lang}\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"

'''
    entries = []
    for s in sorted(strings):
        escaped = s.replace('\\', '\\\\').replace('"', '\\"')
        tr = translations.get(s, s)  # fallback to source if no translation
        tr_escaped = tr.replace('\\', '\\\\').replace('"', '\\"')
        entries.append(f'msgid "{escaped}"\nmsgstr "{tr_escaped}"\n')
    return header + '\n'.join(entries)

# Check coverage
missing_en = [s for s in trans_strings if s not in EN]
missing_ar = [s for s in trans_strings if s not in AR]

if missing_en:
    print(f"EN missing {len(missing_en)} strings:")
    for s in sorted(missing_en)[:20]:
        print(f"  - {s[:80]}")

if missing_ar:
    print(f"\nAR missing {len(missing_ar)} strings:")
    for s in sorted(missing_ar)[:20]:
        print(f"  - {s[:80]}")

for lang, trans in [('fr', FR), ('en', EN), ('ar', AR)]:
    po = generate_po(lang, trans, trans_strings)
    path = os.path.join(LOCALE_DIR, lang, 'LC_MESSAGES', 'django.po')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(po)
    covered = sum(1 for s in trans_strings if s in trans)
    print(f'{lang}: {covered}/{len(trans_strings)} translated')

print('\nDone!')
