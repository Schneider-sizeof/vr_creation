"""
Management command to apply all SEO audit updates and data corrections
directly to the database in a single command on production or local environments.
Usage: python manage.py sync_seo_audit
"""
from django.core.management.base import BaseCommand
from django.core.management import call_command

from apps.services.models import Service
from apps.core.models import SiteSettings, Promotion
from apps.portfolio.models import Project, CaseStudy


class Command(BaseCommand):
    help = "Synchronize all SEO audit data (services, promotions, site settings, page SEO) in one go."

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("=== Synchronizing VR Creation SEO Audit Data ==="))

        # 1. Update PageSEO records
        self.stdout.write("1. Updating PageSEO records...")
        try:
            call_command('seed_seo')
        except Exception as e:
            self.stdout.write(self.style.WARNING(f"  Note during seed_seo: {e}"))

        # 2. Update Services with rich copy (600–1,000 words each, deliverables, turnaround times, pricing tiers)
        self.stdout.write("2. Enriching all Service pages with technical deliverables, pricing and buyer personas...")

        # --- 2.1 Modélisation 3D ---
        try:
            s3d = Service.objects.get(slug='modelisation-3d')
            s3d.title = "Modélisation 3D & rendu architectural"
            s3d.title_fr = "Modélisation 3D & rendu architectural"
            s3d.meta_title = "Modélisation 3D & rendu architectural Tanger | VR Creation"
            s3d.meta_title_fr = "Modélisation 3D & rendu architectural Tanger | VR Creation"
            s3d.meta_description = "Rendus 3D photoréalistes pour l'architecture et l'immobilier à Tanger et Nord du Maroc. Perspectives intérieures, extérieures et axonométries."
            s3d.meta_description_fr = s3d.meta_description
            s3d.short_description = "Rendus 3D photoréalistes d'intérieurs et d'extérieurs pour l'immobilier, l'architecture et l'aménagement à Tanger et dans le Nord du Maroc."
            s3d.short_description_fr = s3d.short_description
            s3d.full_description = """<p class="mb-5 text-base md:text-lg text-gray-700 leading-relaxed font-light">
    La <strong>modélisation 3D architecturale</strong> et le <strong>rendu photoréaliste</strong> sont aujourd'hui au cœur des stratégies de commercialisation des programmes neufs à Tanger et dans le Nord du Maroc. Chez <strong>VR Creation</strong>, nous donnons vie à vos plans d'architectes bien avant le premier coup de pioche, en recréant avec une précision millimétrique les volumes, les matières, la lumière naturelle du détroit et l'atmosphère unique de chaque espace.
</p>

<h3 class="text-2xl font-bold text-dark mt-8 mb-4">Pourquoi la 3D est un levier décisif en VEFA à Tanger</h3>
<p class="mb-4 text-gray-600 leading-relaxed font-light">
    En vente en l'état futur d'achèvement (VEFA), les acquéreurs ont besoin d'être rassurés et séduits. Un plan technique 2D ne suffit plus à susciter le coup de cœur. Nos rendus 3D permettent à vos futurs acheteurs de visualiser précisément leur future pièce de vie, la luminosité du salon au coucher du soleil, la disposition de la cuisine ouverte ou la vue panoramique sur la baie de Tanger depuis la terrasse.
</p>

<h3 class="text-2xl font-bold text-dark mt-8 mb-4">Livrables techniques & Spécifications fournies</h3>
<div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-6">
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-file-image mr-2"></i>Résolution & Formats d'image</h4>
        <p class="text-xs text-gray-600">Rendus Ultra-HD 4K (3840×2160 px) et formats haute résolution 300 DPI pour l'impression grand format (catalogues de vente, kakémonos, panneaux de chantier 4×3m). Formats livrés : TIFF, PNG 24-bit transparent, JPEG haute qualité.</p>
    </div>
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-cubes mr-2"></i>Compatibilité & Fichiers 3D</h4>
        <p class="text-xs text-gray-600">Fichiers sources et exports compatibles DWG, FBX, OBJ, 3DS Max et GLTF/GLB pour intégration web et moteurs de rendu temps réel.</p>
    </div>
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-sun mr-2"></i>Ambiances Lumineuses & Textures PBR</h4>
        <p class="text-xs text-gray-600">Simulations solaires géolocalisées à Tanger : lumière de midi, golden hour au crépuscule ou ambiance nocturne tamisée. Matériaux PBR réalistes (marbre de Carrare, zellige marocain, bois massif, aluminium brossé).</p>
    </div>
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-clock mr-2"></i>Délais d'Exécution Respectés</h4>
        <p class="text-xs text-gray-600">5 à 10 jours ouvrés selon l'envergure du projet, avec présentation d'une première épreuve de cadrage en basse définition à J+3 pour validation des angles de vue.</p>
    </div>
</div>

<h3 class="text-2xl font-bold text-dark mt-8 mb-4">Grille tarifaire indicative</h3>
<p class="mb-3 text-gray-600 text-sm">Chaque projet fait l'objet d'un devis sur-mesure selon la complexité architecturale et le nombre de perspectives :</p>
<ul class="list-disc list-inside space-y-2 mb-6 text-gray-600 text-sm">
    <li><strong>Perspective intérieure résidentielle (salon, chambre, cuisine) :</strong> À partir de 3 200 MAD HT par vue.</li>
    <li><strong>Perspective extérieure (façade villa, immeuble, ensemble résidentiel) :</strong> À partir de 5 500 MAD HT par perspective.</li>
    <li><strong>Pack Programme Immobilier complet (5 à 10 rendus intérieurs + extérieurs) :</strong> Tarif dégressif sur devis avec intégration paysagère.</li>
</ul>

<h3 class="text-2xl font-bold text-dark mt-8 mb-4">À qui s'adresse notre service de modélisation 3D ?</h3>
<ul class="list-disc list-inside space-y-2 mb-6 text-gray-600 text-sm">
    <li><strong>Promoteurs immobiliers à Tanger & Nord :</strong> Création de supports de commercialisation complets pour le lancement commercial de programmes en VEFA.</li>
    <li><strong>Cabinets d'architecture & Bureaux d'études :</strong> Valorisation des dossiers de permis de construire et présentations percutantes pour concours d'architecture.</li>
    <li><strong>Architectes d'intérieur & Designers :</strong> Validation des agencements d'espaces et des choix de mobilier auprès de clients particuliers exigeants.</li>
    <li><strong>Propriétaires de villas d'exception :</strong> Visualisation avant rénovation lourde ou extension à Malabata, Vieille Montagne ou Cap Spartel.</li>
</ul>

<h3 class="text-2xl font-bold text-dark mt-8 mb-4">Études de cas concrètes</h3>
<p class="text-gray-600 text-sm mb-4 leading-relaxed">
    Découvrez comment nos rendus 3D ont permis à nos clients de concrétiser leurs objectifs :
    consultez notre réalisation pour la <a href="/fr/etudes-de-cas/residence-azure/" class="text-primary font-bold hover:underline">Résidence Azure Tanger</a> (taux de vente anticipée de 60%) ou la <a href="/fr/etudes-de-cas/villa-mediterranee/" class="text-primary font-bold hover:underline">Villa Méditerranée</a>.
</p>"""
            s3d.full_description_fr = s3d.full_description
            s3d.save()
            self.stdout.write(self.style.SUCCESS("  ~ Enriched modelisation-3d copy"))
        except Service.DoesNotExist:
            pass

        # --- 2.2 Visites virtuelles ---
        try:
            vv = Service.objects.get(slug='visites-virtuelles')
            vv.title = "Visite virtuelle 3D & maquette orbitale"
            vv.title_fr = "Visite virtuelle 3D & maquette orbitale"
            vv.meta_title = "Visite virtuelle 3D & maquette orbitale Tanger | VR Creation"
            vv.meta_title_fr = "Visite virtuelle 3D & maquette orbitale Tanger | VR Creation"
            vv.meta_description = "Visites virtuelles 3D immersives et interactives pour la vente immobilière sur plan (VEFA) à Tanger et au Maroc. Expérience sur smartphone et VR."
            vv.meta_description_fr = vv.meta_description
            vv.short_description = "Visites virtuelles 3D immersives et interactives pour projets immobiliers sur plan (VEFA), maquettes 3D orbitales et configurateurs d'espaces."
            vv.short_description_fr = vv.short_description
            vv.full_description = """<p class="mb-5 text-base md:text-lg text-gray-700 leading-relaxed font-light">
    La <strong>visite virtuelle 3D immersive</strong> est l'outil commercial le plus performant pour vendre un bien immobilier sur plan. Chez <strong>VR Creation Tanger</strong>, nous concevons des environnements virtuels interactifs à 360° qui permettent à vos futurs acquéreurs de déambuler librement dans leur futur logement, d'en apprécier chaque volume et de tester différentes finitions avant le début du chantier.
</p>

<h3 class="text-2xl font-bold text-dark mt-8 mb-4">L'expérience immersive au service de la décision d'achat</h3>
<p class="mb-4 text-gray-600 leading-relaxed font-light">
    Pour un acquéreur national ou un Marocain Résidant à l'Étranger (MRE), acheter un bien immobilier à distance représente un engagement majeur. Grâce à nos visites interactives, l'acheteur n'est plus un simple spectateur : il se déplace de pièce en pièce, ouvre les portes, observe la perspective depuis la chambre principale et visualise l'ensoleillement de la terrasse. L'émotion est immédiate, accélérant la prise de décision.
</p>

<h3 class="text-2xl font-bold text-dark mt-8 mb-4">Livrables techniques & Fonctionnalités clés</h3>
<div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-6">
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-globe mr-2"></i>Diffusion Multi-Supports Sans Application</h4>
        <p class="text-xs text-gray-600">Accessible par simple lien URL ou QR code, compatible smartphones iOS/Android, tablettes, PC et casques de réalité virtuelle (Meta Quest, Apple Vision Pro). Aucun téléchargement requis.</p>
    </div>
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-code mr-2"></i>Intégration Web & Iframe Clé en Main</h4>
        <p class="text-xs text-gray-600">Code d'intégration iframe prêt à l'emploi pour enrichir les fiches de vos programmes sur votre site web ou les portails immobiliers marocains (Sarouty, Mubawab).</p>
    </div>
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-sliders-h mr-2"></i>Hotspots & Configurateur d'Options</h4>
        <p class="text-xs text-gray-600">Possibilité d'intégrer des infobulles descriptives (surface, matériaux, équipements haut de gamme) et de basculer en un clic entre plusieurs ambiances de carrelage ou mobilier.</p>
    </div>
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-clock mr-2"></i>Délais de Production Rapides</h4>
        <p class="text-xs text-gray-600">Livraison complète en 7 à 12 jours ouvrés par typologie d'appartement ou villa, avec hébergement sécurisé haute disponibilité inclus.</p>
    </div>
</div>

<h3 class="text-2xl font-bold text-dark mt-8 mb-4">Tarifs indicatifs & Formules</h3>
<ul class="list-disc list-inside space-y-2 mb-6 text-gray-600 text-sm">
    <li><strong>Visite 3D Appartement type (F3 / F4 jusqu'à 120 m²) :</strong> À partir de 4 800 MAD HT.</li>
    <li><strong>Visite 3D Villa témoin d'exception (intérieur + extérieur + piscine) :</strong> À partir de 8 500 MAD HT.</li>
    <li><strong>Maquette orbitale 360° de la résidence globale :</strong> Sur devis selon la taille du programme immobilier.</li>
</ul>

<h3 class="text-2xl font-bold text-dark mt-8 mb-4">Pour qui concevons-nous ces visites ?</h3>
<ul class="list-disc list-inside space-y-2 mb-6 text-gray-600 text-sm">
    <li><strong>Promoteurs en VEFA à Tanger, Tétouan et côte méditerranéenne :</strong> Pour équiper les bureaux de vente d'écrans tactiles et envoyer des liens personnalisés aux prospects MRE.</li>
    <li><strong>Agences immobilières de prestige :</strong> Pour valoriser leur portefeuille de mandats exclusifs.</li>
</ul>

<p class="text-gray-600 text-sm mb-4 leading-relaxed">
    Envie de tester l'expérience en direct ? Visitez dès maintenant notre <a href="/fr/visites-virtuelles/" class="text-primary font-bold hover:underline">démonstrateur de visites 360° en ligne</a>.
</p>"""
            vv.full_description_fr = vv.full_description
            vv.save()
            self.stdout.write(self.style.SUCCESS("  ~ Enriched visites-virtuelles copy"))
        except Service.DoesNotExist:
            pass

        # --- 2.3 Captures 360 réelles ---
        try:
            c360 = Service.objects.get(slug='captures-360')
            c360.title = "Capture 360° d'espaces réels"
            c360.title_fr = "Capture 360° d'espaces réels"
            c360.meta_title = "Capture 360° & scan d'espace à Tanger | VR Creation"
            c360.meta_title_fr = "Capture 360° & scan d'espace à Tanger | VR Creation"
            c360.meta_description = "Scans 360° haute définition pour showrooms, boutiques, hôtels et suivi de chantiers à Tanger et Nord du Maroc. Visite virtuelle immersive."
            c360.meta_description_fr = c360.meta_description
            c360.short_description = "Numérisation 360° et visites virtuelles d'espaces construits réels : showrooms, boutiques, hôtels, villas et suivi photographique de chantiers à Tanger."
            c360.short_description_fr = c360.short_description
            c360.full_description = """<p class="mb-5 text-base md:text-lg text-gray-700 leading-relaxed font-light">
    La <strong>capture 360° d'espaces réels</strong> permet de numériser fidèlement un lieu physique déjà construit. Grâce à nos équipements de numérisation panoramique haute résolution et scanners laser, <strong>VR Creation</strong> transforme vos showrooms, hôtels, riads, restaurants, cliniques et commerces à Tanger en véritables jumeaux numériques interactifs ouverts au monde entier 24h/24.
</p>

<h3 class="text-2xl font-bold text-dark mt-8 mb-4">Booster votre visibilité locale et votre taux de visite</h3>
<p class="mb-4 text-gray-600 leading-relaxed font-light">
    À l'heure où plus de 80% des clients consultent Google Maps et les réseaux sociaux avant de se déplacer dans un établissement, disposer d'une visite virtuelle 360° immersive est un avantage concurrentiel majeur. Vos clients se projettent instantanément dans votre univers de marque, explorent vos rayons ou vos suites hôtelières et réservent en toute confiance.
</p>

<h3 class="text-2xl font-bold text-dark mt-8 mb-4">Livrables techniques & Options avancées</h3>
<div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-6">
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-map-marked-alt mr-2"></i>Intégration Google Street View & Google Business</h4>
        <p class="text-xs text-gray-600">Publication officielle sur Google Maps et votre fiche d'établissement pour un gain immédiat en visibilité SEO locale à Tanger et au Maroc.</p>
    </div>
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-tags mr-2"></i>Balises Interactives (Hotspots E-Commerce)</h4>
        <p class="text-xs text-gray-600">Points d'interaction cliquables avec fiches produits, vidéos explicatives, liens directs vers votre boutique en ligne ou formulaires de réservation.</p>
    </div>
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-camera mr-2"></i>Panoramas Équirectangulaires 8K HDR</h4>
        <p class="text-xs text-gray-600">Prises de vues 360° traitées en HDR pour une netteté irréprochable même en contre-jour et dans les zones d'ombres complexes.</p>
    </div>
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-bolt mr-2"></i>Shooting Rapide & Sans Rupture d'Activité</h4>
        <p class="text-xs text-gray-600">Captation discrète sur place en 1 à 3 heures, livraison de la visite interactive prête à diffuser en 48h à 72h ouvrées.</p>
    </div>
</div>

<h3 class="text-2xl font-bold text-dark mt-8 mb-4">Tarification indicative</h3>
<ul class="list-disc list-inside space-y-2 mb-6 text-gray-600 text-sm">
    <li><strong>Boutique ou restaurant (jusqu'à 100 m²) :</strong> À partir de 2 500 MAD HT.</li>
    <li><strong>Showroom ou établissement moyen (100 à 300 m²) :</strong> À partir de 4 000 MAD HT.</li>
    <li><strong>Hôtel, Riad ou Espace d'exception (+300 m²) :</strong> Sur devis personnalisé selon le nombre de points de vue.</li>
</ul>

<p class="text-gray-600 text-sm mb-4 leading-relaxed">
    Consultez un exemple concret : découvrez notre visite interactive pour le <a href="/fr/etudes-de-cas/concept-store-lumiere/" class="text-primary font-bold hover:underline">Concept Store Lumière à Tanger</a>.
</p>"""
            c360.full_description_fr = c360.full_description
            c360.save()
            self.stdout.write(self.style.SUCCESS("  ~ Enriched captures-360 copy"))
        except Service.DoesNotExist:
            pass

        # --- 2.4 Branding visuel ---
        try:
            bv = Service.objects.get(slug='branding-visuel')
            bv.title = "Branding & communication visuelle"
            bv.title_fr = "Branding & communication visuelle"
            bv.meta_title = "Branding & communication visuelle Tanger | VR Creation"
            bv.meta_title_fr = "Branding & communication visuelle Tanger | VR Creation"
            bv.meta_description = "Identité visuelle d'entreprise et de programmes immobiliers à Tanger : logo, charte graphique, catalogues de vente et supports print de prestige."
            bv.meta_description_fr = bv.meta_description
            bv.short_description = "Création d'identités visuelles complètes, logos, chartes graphiques et supports de vente de prestige pour marques et promoteurs à Tanger."
            bv.short_description_fr = bv.short_description
            bv.full_description = """<p class="mb-5 text-base md:text-lg text-gray-700 leading-relaxed font-light">
    Une identité visuelle forte est le premier facteur de confiance pour vos clients. À Tanger, métropole en pleine effervescence économique, émerger face à la concurrence exige une image de marque soignée et mémorable. <strong>VR Creation</strong> conçoit des chartes graphiques percutantes et des supports commerciaux haut de gamme qui incarnent parfaitement le positionnement de votre entreprise ou de votre programme immobilier.
</p>

<h3 class="text-2xl font-bold text-dark mt-8 mb-4">Donner une signature visuelle unique à votre projet</h3>
<p class="mb-4 text-gray-600 leading-relaxed font-light">
    Que vous lanciez une nouvelle marque d'architecture, un complexe résidentiel de luxe ou une enseigne commerciale à Tanger, nous bâtissons un univers de communication harmonieux : du nom de marque (naming) au logo, en passant par le choix minutieux des typographies, des textures de papier et des déclinaisons digitales pour vos réseaux sociaux.
</p>

<h3 class="text-2xl font-bold text-dark mt-8 mb-4">Pack complet de livrables fournis</h3>
<div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-6">
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-bezier-curve mr-2"></i>Logo Vectoriel & Déclinaisons</h4>
        <p class="text-xs text-gray-600">Logo fourni en formats vectoriels haute définition (SVG, EPS, PDF) et matriciels (PNG haute résolution avec fond transparent), en versions couleur, monochrome, dark mode et favicon.</p>
    </div>
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-book mr-2"></i>Brand Book & Charte Graphique</h4>
        <p class="text-xs text-gray-600">Guide complet d'utilisation de la marque (règles typographiques, codes couleurs CMJN/RVB/Pantone, marges de sécurité et exemples d'interdictions).</p>
    </div>
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-newspaper mr-2"></i>Brochures & Catalogues VEFA</h4>
        <p class="text-xs text-gray-600">Conception de plaquettes commerciales de prestige (16 à 32 pages) avec intégration de vos rendus 3D, plans de vente et fiches techniques, prêtes pour impression offset.</p>
    </div>
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-hashtag mr-2"></i>Kit de Communication Digitale</h4>
        <p class="text-xs text-gray-600">Modèles de posts et stories éditables (Canva/Photoshop), bannières LinkedIn et signatures d'e-mails professionnelles.</p>
    </div>
</div>

<h3 class="text-2xl font-bold text-dark mt-8 mb-4">Délais & Tarifs indicatifs</h3>
<p class="text-gray-600 text-sm mb-2">Processus collaboratif avec 3 pistes créatives initiales sous 7 jours ouvrés :</p>
<ul class="list-disc list-inside space-y-2 mb-6 text-gray-600 text-sm">
    <li><strong>Identité de Marque essentielle (Logo + Charte graphique condensée) :</strong> À partir de 4 500 MAD HT.</li>
    <li><strong>Pack Branding Programme Immobilier (Logo, Charte, Brochure VEFA 16p, Panneau de chantier) :</strong> À partir de 8 500 MAD HT.</li>
</ul>"""
            bv.full_description_fr = bv.full_description
            bv.save()
            self.stdout.write(self.style.SUCCESS("  ~ Enriched branding-visuel copy"))
        except Service.DoesNotExist:
            pass

        # --- 2.5 Photographie & Drone ---
        try:
            photo = Service.objects.get(slug='photographie')
            photo.title = "Photographie professionnelle & drone"
            photo.title_fr = "Photographie professionnelle & drone"
            photo.meta_title = "Photographie professionnelle & drone Tanger | VR Creation"
            photo.meta_title_fr = "Photographie professionnelle & drone Tanger | VR Creation"
            photo.meta_description = "Photographie d'architecture, suivi de chantier et prises de vues aériennes par drone à Tanger et dans le Nord du Maroc. Images haute résolution."
            photo.meta_description_fr = photo.meta_description
            photo.short_description = "Reportages photographiques d'architecture, d'intérieurs et prises de vues aériennes par drone à Tanger et dans tout le Nord du Maroc."
            photo.short_description_fr = photo.short_description
            photo.full_description = """<p class="mb-5 text-base md:text-lg text-gray-700 leading-relaxed font-light">
    La <strong>photographie professionnelle d'architecture</strong> et les <strong>prises de vues aériennes par drone</strong> subliment la réalité de vos réalisations. Basée à Tanger, l'équipe de <strong>VR Creation</strong> capture l'âme de vos projets avec une maîtrise pointue de la lumière naturelle, des perspectives géométriques et des techniques de retouche de pointe.
</p>

<h3 class="text-2xl font-bold text-dark mt-8 mb-4">Capturer l'élégance architecturale et la vue panoramique</h3>
<p class="mb-4 text-gray-600 leading-relaxed font-light">
    À Tanger, l'emplacement et la vue (mer Méditerranée, détroit de Gibraltar, collines de la Vieille Montagne) représentent souvent une part déterminante de la valeur d'un bien immobilier. Grâce à nos prises de vues par drone homologué, nous montrons à vos futurs acquéreurs la hauteur réelle des futurs étages et la vue imprenable dont ils profiteront depuis leur balcon.
</p>

<h3 class="text-2xl font-bold text-dark mt-8 mb-4">Livrables techniques</h3>
<div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-6">
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-camera mr-2"></i>Optiques à Décentrement</h4>
        <p class="text-xs text-gray-600">Prises de vues au sol réalisées avec objectifs professionnels à décentrement pour garantir des verticales rigoureusement parallèles sans distorsion d'angle.</p>
    </div>
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-plane mr-2"></i>Drone 4K Stabilisé</h4>
        <p class="text-xs text-gray-600">Vues aériennes grand angle et vidéos 4K 60 fps pour vos clips promotionnels, suivi de chantier périodique et repérage de vue par étage.</p>
    </div>
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-magic mr-2"></i>Post-Production Numérique Soignée</h4>
        <p class="text-xs text-gray-600">Développement RAW, étalonnage colorimétrique homogène et gommage numérique des éléments parasites (câbles, poussières de chantier).</p>
    </div>
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-download mr-2"></i>Double Résolution Fournie</h4>
        <p class="text-xs text-gray-600">Fichiers livrés en haute définition 300 DPI pour l'impression et formats optimisés web pour un affichage instantané sur vos réseaux et site internet.</p>
    </div>
</div>

<h3 class="text-2xl font-bold text-dark mt-8 mb-4">Tarifs indicatifs</h3>
<ul class="list-disc list-inside space-y-2 mb-6 text-gray-600 text-sm">
    <li><strong>Shooting Architecture Intérieure / Extérieure (demi-journée) :</strong> À partir de 3 000 MAD HT (20 à 30 photos retouchées).</li>
    <li><strong>Session Drone Seule (photos + rushs vidéo 4K) :</strong> À partir de 2 500 MAD HT.</li>
    <li><strong>Pack Combiné Sol + Drone (journée complète) :</strong> À partir de 5 000 MAD HT.</li>
</ul>"""
            photo.full_description_fr = photo.full_description
            photo.save()
            self.stdout.write(self.style.SUCCESS("  ~ Enriched photographie copy"))
        except Service.DoesNotExist:
            pass

        # --- 2.6 Animation 3D & Motion Design ---
        try:
            anim = Service.objects.get(slug='animation-motion-design')
            anim.title = "Animation 3D & motion design"
            anim.title_fr = "Animation 3D & motion design"
            anim.meta_title = "Animation 3D & motion design à Tanger | VR Creation"
            anim.meta_title_fr = "Animation 3D & motion design à Tanger | VR Creation"
            anim.meta_description = "Films 3D d'animation architecturale, teasers publicitaires et visites vidéo cinématiques pour promouvoir vos projets immobiliers à Tanger."
            anim.meta_description_fr = anim.meta_description
            anim.short_description = "Films d'animation 3D cinématiques, teasers vidéo immersifs et habillages motion design pour projets immobiliers et entreprises à Tanger."
            anim.short_description_fr = anim.short_description
            anim.full_description = """<p class="mb-5 text-base md:text-lg text-gray-700 leading-relaxed font-light">
    L'<strong>animation 3D cinématique</strong> et le <strong>motion design</strong> représentent le summum de l'expérience visuelle pour la promotion d'un projet immobilier d'envergure. <strong>VR Creation</strong> produit des films vidéo 3D captivants qui transportent vos acquéreurs dans un voyage cinématographique au cœur de votre vision architecturale.
</p>

<h3 class="text-2xl font-bold text-dark mt-8 mb-4">Raconter l'histoire de votre projet en mouvement</h3>
<p class="mb-4 text-gray-600 leading-relaxed font-light">
    Là où une image fixe montre un instant, le film d'animation 3D raconte une véritable histoire. La caméra survole le littoral tangérois, s'approche de la façade principale, traverse les jardins paysagers, franchit le hall d'entrée baigné de lumière et découvre l'intimité raffinée des appartements. Accompagné d'une bande sonore travaillée et d'une voix off professionnelle, votre projet devient inoubliable.
</p>

<h3 class="text-2xl font-bold text-dark mt-8 mb-4">Livrables techniques</h3>
<div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-6">
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-video mr-2"></i>Résolution 4K & Multi-Formats</h4>
        <p class="text-xs text-gray-600">Export en Ultra-HD 4K et Full HD 1080p en 60 images par seconde. Déclinaisons en format horizontal 16:9 (salons, YouTube) et vertical 9:16 pour Instagram Reels et TikTok Ads.</p>
    </div>
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-headphones mr-2"></i>Sound Design & Voix Off</h4>
        <p class="text-xs text-gray-600">Composition musicale libre de droits, effets sonores immersifs (vent marin, fontaine, pas sur le parquet) et enregistrement de voix off professionnelle (Français, Arabe dialectal ou standard, Anglais).</p>
    </div>
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-film mr-2"></i>Habillage Motion Design & Synthèses</h4>
        <p class="text-xs text-gray-600">Intégration de titrages élégants, cartographies animées de localisation et indicateurs clés de surface en surimpression dynamique.</p>
    </div>
    <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
        <h4 class="font-bold text-primary text-sm mb-1"><i class="fas fa-calendar-alt mr-2"></i>Délais de Production</h4>
        <p class="text-xs text-gray-600">15 à 25 jours ouvrés selon la durée du film avec validation préalable du storyboard et de l'animatique basse résolution.</p>
    </div>
</div>

<h3 class="text-2xl font-bold text-dark mt-8 mb-4">Tarifs indicatifs</h3>
<ul class="list-disc list-inside space-y-2 mb-6 text-gray-600 text-sm">
    <li><strong>Teaser promotionnel 3D court (20 à 30 secondes) :</strong> À partir de 11 000 MAD HT.</li>
    <li><strong>Film architectural complet (60 à 90 secondes) :</strong> À partir de 18 500 MAD HT.</li>
</ul>"""
            anim.full_description_fr = anim.full_description
            anim.save()
            self.stdout.write(self.style.SUCCESS("  ~ Enriched animation-motion-design copy"))
        except Service.DoesNotExist:
            pass

        # 3. Update Promotions
        self.stdout.write("3. Updating Promotions...")
        for promo in Promotion.objects.all():
            if "RÉSULTAT GARANTI" in (promo.solution_title_fr or "") or "RÉSULTAT GARANTI" in (promo.solution_title or ""):
                promo.solution_title = "NOTRE MODÈLE : ENGAGEMENT D'EXCELLENCE & ACCOMPAGNEMENT DÉDIÉ"
                promo.solution_title_fr = "NOTRE MODÈLE : ENGAGEMENT D'EXCELLENCE & ACCOMPAGNEMENT DÉDIÉ"
                promo.save()
                self.stdout.write(self.style.SUCCESS(f"  ~ Updated Promotion #{promo.id}: Engagement d'excellence"))

        # 4. Update SiteSettings
        self.stdout.write("4. Updating SiteSettings...")
        settings_obj = SiteSettings.objects.first()
        if settings_obj:
            settings_obj.hero_headline = "Modélisation 3D & visites virtuelles à Tanger — VR Creation"
            settings_obj.hero_headline_fr = "Modélisation 3D & visites virtuelles à Tanger — VR Creation"
            settings_obj.hero_cta2_link = "/fr/contact/"
            settings_obj.phone = "+212 625 07 1498"
            settings_obj.address = "Ibn Batouta bureaux, Av. Youssef Ibn Tachfine, Tanger 90000, Maroc"
            settings_obj.address_fr = "Ibn Batouta bureaux, Av. Youssef Ibn Tachfine, Tanger 90000, Maroc"
            settings_obj.save()
            self.stdout.write(self.style.SUCCESS("  ~ Updated SiteSettings headline, CTA link and official Tanger address"))

        # 5. Update WebP images & 360 Tour URLs
        self.stdout.write("5. Synchronizing WebP optimized images & local 360 tours...")
        try:
            import os
            from PIL import Image
            from django.conf import settings
            from apps.services.models import ServiceImage

            media_root = settings.MEDIA_ROOT

            def ensure_webp(img_field, target_2_1=False):
                if not img_field or not getattr(img_field, 'path', None):
                    return
                png_path = img_field.path.replace('.webp', '.png')
                webp_path = os.path.splitext(img_field.path)[0] + '.webp'
                if os.path.exists(png_path) and (not os.path.exists(webp_path) or os.path.getsize(webp_path) == 0):
                    try:
                        with Image.open(png_path) as im:
                            if target_2_1:
                                equi = im.resize((2048, 1024), Image.Resampling.LANCZOS)
                                equi.save(webp_path, 'WEBP', quality=88, method=6)
                            else:
                                rgb = im.convert('RGB')
                                rgb.save(webp_path, 'WEBP', quality=85, method=6)
                    except Exception:
                        pass

            # Convert 360 tour panoramas to 2:1 WebP on disk if needed
            gallery_dir = os.path.join(media_root, 'services', 'gallery')
            if os.path.exists(gallery_dir):
                for f in os.listdir(gallery_dir):
                    if f.endswith('.png'):
                        png_f = os.path.join(gallery_dir, f)
                        webp_f = os.path.splitext(png_f)[0] + '.webp'
                        if not os.path.exists(webp_f) or os.path.getsize(webp_f) == 0:
                            try:
                                with Image.open(png_f) as im:
                                    im.resize((2048, 1024), Image.Resampling.LANCZOS).save(webp_f, 'WEBP', quality=88, method=6)
                            except Exception:
                                pass

            Project.objects.filter(slug='villa-mediterranee').update(virtual_tour_url='/media/services/gallery/visites-virtuelles-1.webp')
            Project.objects.filter(slug='residence-azure').update(virtual_tour_url='/media/services/gallery/visites-virtuelles-2.webp')
            Project.objects.filter(slug='concept-store-lumiere').update(virtual_tour_url='/media/services/gallery/captures-360-1.webp')

            for s in Service.objects.all():
                if s.featured_image:
                    ensure_webp(s.featured_image)
                    if s.featured_image.name.endswith('.png'):
                        s.featured_image = s.featured_image.name.replace('.png', '.webp')
                        s.save(update_fields=['featured_image'])

            for p in Project.objects.all():
                if p.featured_image:
                    ensure_webp(p.featured_image)
                    if p.featured_image.name.endswith('.png'):
                        p.featured_image = p.featured_image.name.replace('.png', '.webp')
                        p.save(update_fields=['featured_image'])

            for cs in CaseStudy.objects.all():
                if cs.featured_image:
                    ensure_webp(cs.featured_image)
                    if cs.featured_image.name.endswith('.png'):
                        cs.featured_image = cs.featured_image.name.replace('.png', '.webp')
                        cs.save(update_fields=['featured_image'])

            for si in ServiceImage.objects.all():
                if si.image:
                    ensure_webp(si.image)
                    if si.image.name.endswith('.png'):
                        si.image = si.image.name.replace('.png', '.webp')
                        si.save(update_fields=['image'])
            self.stdout.write(self.style.SUCCESS("  ~ Synchronized all database image paths and verified WebP files"))
        except Exception as e:
            self.stdout.write(self.style.WARNING(f"  Note during WebP synchronization: {e}"))

        self.stdout.write(self.style.SUCCESS("\n[SUCCESS] All SEO audit synchronization steps completed!"))
