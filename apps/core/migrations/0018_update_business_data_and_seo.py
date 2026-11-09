"""
Migration: Update business data, rename service, update process steps, seed SEO data.
"""
from django.db import migrations


def update_site_settings(apps, schema_editor):
    SiteSettings = apps.get_model('core', 'SiteSettings')
    try:
        s = SiteSettings.objects.get(pk=1)
    except SiteSettings.DoesNotExist:
        return

    s.email = 'contact@vrcreationcompany.com'
    s.phone = '+212 625 07 1498'
    s.address = 'Ibn Batouta bureaux, Av. Youssef Ibn Tachfine, Tangier 90000'
    s.address_fr = 'Ibn Batouta bureaux, Av. Youssef Ibn Tachfine, Tanger 90000'
    s.address_en = 'Ibn Batouta offices, Av. Youssef Ibn Tachfine, Tangier 90000'
    s.address_ar = '\u0645\u0643\u0627\u062a\u0628 \u0627\u0628\u0646 \u0628\u0637\u0648\u0637\u0629\u060c \u0634\u0627\u0631\u0639 \u064a\u0648\u0633\u0641 \u0628\u0646 \u062a\u0627\u0634\u0641\u064a\u0646\u060c \u0637\u0646\u062c\u0629 90000'
    s.social_whatsapp = '212625071498'
    s.google_maps_embed_url = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3238.2!2d-5.834!3d35.7595!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMzXCsDQ1JzM0LjIiTiA1wrA1MCcwMi40Ilc!5e0!3m2!1sfr!2sma!4v1'

    # Update hero headlines to be general, not immobilier-specific
    s.hero_headline_fr = "Sublimez votre image de marque avec la production visuelle haut de gamme \u2014 VR Creation \u00e0 Tanger"
    s.hero_headline_en = "Elevate your brand image with premium visual production \u2014 VR Creation in Tangier"
    s.hero_headline_ar = "\u0627\u0631\u062a\u0642\u0650 \u0628\u0635\u0648\u0631\u0629 \u0639\u0644\u0627\u0645\u062a\u0643 \u0627\u0644\u062a\u062c\u0627\u0631\u064a\u0629 \u0645\u0639 \u0627\u0644\u0625\u0646\u062a\u0627\u062c \u0627\u0644\u0628\u0635\u0631\u064a \u0627\u0644\u0631\u0627\u0642\u064a \u2014 VR Creation \u0641\u064a \u0637\u0646\u062c\u0629"
    s.hero_subheadline_fr = "Mod\u00e9lisation 3D, photographie, visites virtuelles, branding et communication visuelle \u2014 nous transformons vos projets en exp\u00e9riences visuelles qui s\u00e9duisent et convertissent."
    s.hero_subheadline_en = "3D modeling, photography, virtual tours, branding and visual communication \u2014 we transform your projects into visual experiences that captivate and convert."
    s.hero_subheadline_ar = "\u0646\u0645\u0630\u062c\u0629 \u062b\u0644\u0627\u062b\u064a\u0629 \u0627\u0644\u0623\u0628\u0639\u0627\u062f\u060c \u062a\u0635\u0648\u064a\u0631\u060c \u062c\u0648\u0644\u0627\u062a \u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0629\u060c \u0628\u0631\u0627\u0646\u062f\u064a\u0646\u063a \u0648\u062a\u0648\u0627\u0635\u0644 \u0628\u0635\u0631\u064a \u2014 \u0646\u062d\u0648\u0644 \u0645\u0634\u0627\u0631\u064a\u0639\u0643\u0645 \u0625\u0644\u0649 \u062a\u062c\u0627\u0631\u0628 \u0628\u0635\u0631\u064a\u0629 \u062a\u0623\u0633\u0631 \u0648\u062a\u064f\u0642\u0646\u0639."

    s.footer_text_fr = "VR Creation Company \u2014 Agence de production visuelle, 3D, photographie et branding \u00e0 Tanger. Nous allions esth\u00e9tique et technologie de pointe pour transformer vos projets en exp\u00e9riences visuelles immersives."
    s.footer_text_en = "VR Creation Company \u2014 Visual production, 3D, photography and branding agency in Tangier. We combine aesthetics and cutting-edge technology to transform your projects into immersive visual experiences."
    s.footer_text_ar = "\u0634\u0631\u0643\u0629 \u0641\u064a \u0622\u0631 \u0643\u0631\u064a\u064a\u0634\u0646 \u2014 \u0648\u0643\u0627\u0644\u0629 \u0625\u0646\u062a\u0627\u062c \u0628\u0635\u0631\u064a\u060c 3D\u060c \u062a\u0635\u0648\u064a\u0631 \u0648\u0628\u0631\u0627\u0646\u062f\u064a\u0646\u063a \u0641\u064a \u0637\u0646\u062c\u0629. \u0646\u062c\u0645\u0639 \u0628\u064a\u0646 \u0627\u0644\u062c\u0645\u0627\u0644\u064a\u0629 \u0648\u0627\u0644\u062a\u0643\u0646\u0648\u0644\u0648\u062c\u064a\u0627 \u0627\u0644\u0645\u062a\u0637\u0648\u0631\u0629."

    s.save()


def rename_branding_service(apps, schema_editor):
    """Rename Branding immobilier to Branding & communication visuelle."""
    Service = apps.get_model('services', 'Service')
    # Check for old slug or old title
    for svc in Service.objects.filter(slug__in=['branding-immobilier', 'branding-visuel']):
        if 'immobilier' in (svc.title_fr or '').lower() or svc.slug == 'branding-immobilier':
            svc.title_fr = 'Branding & communication visuelle'
            svc.title_en = 'Branding & Visual Communication'
            svc.title_ar = '\u0627\u0644\u0639\u0644\u0627\u0645\u0629 \u0627\u0644\u062a\u062c\u0627\u0631\u064a\u0629 \u0648\u0627\u0644\u062a\u0648\u0627\u0635\u0644 \u0627\u0644\u0628\u0635\u0631\u064a'
            svc.slug = 'branding-communication-visuelle'
            svc.short_description_fr = "Construisez une identit\u00e9 visuelle m\u00e9morable : logo, charte graphique, supports print et digitaux, visuels r\u00e9seaux sociaux \u2014 adapt\u00e9s aux entreprises de Tanger et du Nord du Maroc."
            svc.short_description_en = "Build a memorable visual identity: logo, brand guidelines, print and digital materials, social media visuals \u2014 tailored for businesses in Tangier and Northern Morocco."
            svc.short_description_ar = "\u0627\u0628\u0646\u0650 \u0647\u0648\u064a\u0629 \u0628\u0635\u0631\u064a\u0629 \u0644\u0627 \u062a\u064f\u0646\u0633\u0649: \u0634\u0639\u0627\u0631\u060c \u0645\u064a\u062b\u0627\u0642 \u063a\u0631\u0627\u0641\u064a\u0643\u064a\u060c \u0645\u0648\u0627\u062f \u0645\u0637\u0628\u0648\u0639\u0629 \u0648\u0631\u0642\u0645\u064a\u0629 \u2014 \u0645\u0635\u0645\u0645\u0629 \u0644\u0644\u0634\u0631\u0643\u0627\u062a \u0641\u064a \u0637\u0646\u062c\u0629 \u0648\u0634\u0645\u0627\u0644 \u0627\u0644\u0645\u063a\u0631\u0628."
            svc.full_description_fr = """<h3>Votre image de marque, votre premier ambassadeur</h3>
<p>Chez VR Creation, nous concevons des identit\u00e9s visuelles compl\u00e8tes qui refl\u00e8tent l\u2019ADN de votre entreprise et captent l\u2019attention de votre audience cible \u00e0 Tanger et dans tout le Nord du Maroc.</p>

<h3>Ce que nous proposons</h3>
<ul>
<li><strong>Cr\u00e9ation de logo</strong> \u2014 Design original, m\u00e9morable et d\u00e9clinable sur tous supports</li>
<li><strong>Charte graphique</strong> \u2014 Palette de couleurs, typographies, r\u00e8gles d\u2019usage de la marque</li>
<li><strong>Supports print</strong> \u2014 Cartes de visite, brochures, flyers, kakemonos, enseignes</li>
<li><strong>Visuels digitaux</strong> \u2014 Banni\u00e8res web, posts r\u00e9seaux sociaux, newsletters</li>
<li><strong>Communication visuelle</strong> \u2014 Strat\u00e9gie visuelle globale pour votre pr\u00e9sence en ligne et hors ligne</li>
</ul>

<h3>Pour qui ?</h3>
<p>Commerces, restaurants, cabinets, startups, promoteurs, agences\u2026 Toute entreprise de Tanger, T\u00e9touan, Asilah, Chefchaouen ou du Nord du Maroc qui souhaite se d\u00e9marquer avec une image professionnelle et coh\u00e9rente.</p>"""

            svc.full_description_en = """<h3>Your brand image, your first ambassador</h3>
<p>At VR Creation, we design complete visual identities that reflect your company\u2019s DNA and capture the attention of your target audience in Tangier and throughout Northern Morocco.</p>

<h3>What we offer</h3>
<ul>
<li><strong>Logo design</strong> \u2014 Original, memorable and adaptable across all media</li>
<li><strong>Brand guidelines</strong> \u2014 Color palette, typography, brand usage rules</li>
<li><strong>Print materials</strong> \u2014 Business cards, brochures, flyers, banners, signage</li>
<li><strong>Digital visuals</strong> \u2014 Web banners, social media posts, newsletters</li>
<li><strong>Visual communication</strong> \u2014 Global visual strategy for your online and offline presence</li>
</ul>

<h3>Who is it for?</h3>
<p>Shops, restaurants, offices, startups, developers, agencies\u2026 Any business in Tangier, Tetouan, Asilah, Chefchaouen or Northern Morocco looking for a professional and consistent brand image.</p>"""

            svc.full_description_ar = """<h3>\u0635\u0648\u0631\u0629 \u0639\u0644\u0627\u0645\u062a\u0643 \u0627\u0644\u062a\u062c\u0627\u0631\u064a\u0629\u060c \u0633\u0641\u064a\u0631\u0643 \u0627\u0644\u0623\u0648\u0644</h3>
<p>\u0641\u064a VR Creation\u060c \u0646\u0635\u0645\u0645 \u0647\u0648\u064a\u0627\u062a \u0628\u0635\u0631\u064a\u0629 \u0643\u0627\u0645\u0644\u0629 \u062a\u0639\u0643\u0633 \u062c\u0648\u0647\u0631 \u0634\u0631\u0643\u062a\u0643 \u0648\u062a\u062c\u0630\u0628 \u0627\u0646\u062a\u0628\u0627\u0647 \u062c\u0645\u0647\u0648\u0631\u0643 \u0627\u0644\u0645\u0633\u062a\u0647\u062f\u0641 \u0641\u064a \u0637\u0646\u062c\u0629 \u0648\u0634\u0645\u0627\u0644 \u0627\u0644\u0645\u063a\u0631\u0628.</p>"""
            svc.save()
            break


def update_process_steps(apps, schema_editor):
    """Replace existing process steps with 6 generic ones."""
    ProcessStep = apps.get_model('core', 'ProcessStep')
    ProcessStep.objects.all().delete()
    
    steps = [
        {
            'title_fr': 'D\u00e9couverte & consultation',
            'title_en': 'Discovery & consultation',
            'title_ar': '\u0627\u0644\u0627\u0643\u062a\u0634\u0627\u0641 \u0648\u0627\u0644\u0627\u0633\u062a\u0634\u0627\u0631\u0629',
            'description_fr': "Nous \u00e9coutons vos besoins, analysons votre march\u00e9 et d\u00e9finissons ensemble les objectifs du projet.",
            'description_en': "We listen to your needs, analyze your market and define the project objectives together.",
            'description_ar': '\u0646\u0633\u062a\u0645\u0639 \u0644\u0627\u062d\u062a\u064a\u0627\u062c\u0627\u062a\u0643\u060c \u0646\u062d\u0644\u0644 \u0633\u0648\u0642\u0643 \u0648\u0646\u062d\u062f\u062f \u0645\u0639\u064b\u0627 \u0623\u0647\u062f\u0627\u0641 \u0627\u0644\u0645\u0634\u0631\u0648\u0639.',
            'icon': 'fas fa-comments', 'order': 1,
        },
        {
            'title_fr': 'Proposition & devis',
            'title_en': 'Proposal & quote',
            'title_ar': '\u0627\u0644\u0639\u0631\u0636 \u0648\u0627\u0644\u062a\u0633\u0639\u064a\u0631',
            'description_fr': "Nous vous pr\u00e9sentons une proposition d\u00e9taill\u00e9e avec planning, livrables et tarifs transparents.",
            'description_en': "We present a detailed proposal with timeline, deliverables and transparent pricing.",
            'description_ar': '\u0646\u0642\u062f\u0645 \u0644\u0643 \u0639\u0631\u0636\u064b\u0627 \u0645\u0641\u0635\u0644\u064b\u0627 \u0645\u0639 \u062c\u062f\u0648\u0644 \u0632\u0645\u0646\u064a \u0648\u0645\u062e\u0631\u062c\u0627\u062a \u0648\u0623\u0633\u0639\u0627\u0631 \u0634\u0641\u0627\u0641\u0629.',
            'icon': 'fas fa-file-invoice', 'order': 2,
        },
        {
            'title_fr': 'Planification cr\u00e9ative',
            'title_en': 'Creative planning',
            'title_ar': '\u0627\u0644\u062a\u062e\u0637\u064a\u0637 \u0627\u0644\u0625\u0628\u062f\u0627\u0639\u064a',
            'description_fr': "Nous \u00e9laborons le concept cr\u00e9atif, les moodboards et les premi\u00e8res esquisses pour valider la direction artistique.",
            'description_en': "We develop the creative concept, moodboards and initial sketches to validate the artistic direction.",
            'description_ar': '\u0646\u0637\u0648\u0631 \u0627\u0644\u0645\u0641\u0647\u0648\u0645 \u0627\u0644\u0625\u0628\u062f\u0627\u0639\u064a \u0648\u0627\u0644\u0631\u0633\u0648\u0645\u0627\u062a \u0627\u0644\u0623\u0648\u0644\u064a\u0629 \u0644\u0644\u062a\u062d\u0642\u0642 \u0645\u0646 \u0627\u0644\u0627\u062a\u062c\u0627\u0647 \u0627\u0644\u0641\u0646\u064a.',
            'icon': 'fas fa-lightbulb', 'order': 3,
        },
        {
            'title_fr': 'Production & ex\u00e9cution',
            'title_en': 'Production & execution',
            'title_ar': '\u0627\u0644\u0625\u0646\u062a\u0627\u062c \u0648\u0627\u0644\u062a\u0646\u0641\u064a\u0630',
            'description_fr': "Notre \u00e9quipe r\u00e9alise le projet : mod\u00e9lisation, shooting, design, d\u00e9veloppement ou montage selon le service.",
            'description_en': "Our team executes the project: modeling, shooting, design, development or editing depending on the service.",
            'description_ar': '\u064a\u0646\u0641\u0630 \u0641\u0631\u064a\u0642\u0646\u0627 \u0627\u0644\u0645\u0634\u0631\u0648\u0639: \u0646\u0645\u0630\u062c\u0629\u060c \u062a\u0635\u0648\u064a\u0631\u060c \u062a\u0635\u0645\u064a\u0645\u060c \u062a\u0637\u0648\u064a\u0631 \u0623\u0648 \u0645\u0648\u0646\u062a\u0627\u062c \u062d\u0633\u0628 \u0627\u0644\u062e\u062f\u0645\u0629.',
            'icon': 'fas fa-cogs', 'order': 4,
        },
        {
            'title_fr': 'R\u00e9vision & ajustements',
            'title_en': 'Review & revisions',
            'title_ar': '\u0627\u0644\u0645\u0631\u0627\u062c\u0639\u0629 \u0648\u0627\u0644\u062a\u0639\u062f\u064a\u0644\u0627\u062a',
            'description_fr': "Nous pr\u00e9sentons les r\u00e9sultats et int\u00e9grons vos retours pour atteindre la perfection.",
            'description_en': "We present the results and incorporate your feedback to achieve perfection.",
            'description_ar': '\u0646\u0639\u0631\u0636 \u0627\u0644\u0646\u062a\u0627\u0626\u062c \u0648\u0646\u062f\u0645\u062c \u0645\u0644\u0627\u062d\u0638\u0627\u062a\u0643 \u0644\u0644\u0648\u0635\u0648\u0644 \u0625\u0644\u0649 \u0627\u0644\u0643\u0645\u0627\u0644.',
            'icon': 'fas fa-sync-alt', 'order': 5,
        },
        {
            'title_fr': 'Livraison & accompagnement',
            'title_en': 'Delivery & support',
            'title_ar': '\u0627\u0644\u062a\u0633\u0644\u064a\u0645 \u0648\u0627\u0644\u062f\u0639\u0645',
            'description_fr': "Livraison des fichiers finaux dans tous les formats requis, avec un suivi et un support post-projet.",
            'description_en': "Delivery of final files in all required formats, with post-project follow-up and support.",
            'description_ar': '\u062a\u0633\u0644\u064a\u0645 \u0627\u0644\u0645\u0644\u0641\u0627\u062a \u0627\u0644\u0646\u0647\u0627\u0626\u064a\u0629 \u0628\u062c\u0645\u064a\u0639 \u0627\u0644\u062a\u0646\u0633\u064a\u0642\u0627\u062a \u0627\u0644\u0645\u0637\u0644\u0648\u0628\u0629\u060c \u0645\u0639 \u0645\u062a\u0627\u0628\u0639\u0629 \u0648\u062f\u0639\u0645 \u0628\u0639\u062f \u0627\u0644\u0645\u0634\u0631\u0648\u0639.',
            'icon': 'fas fa-check-circle', 'order': 6,
        },
    ]
    for s in steps:
        ProcessStep.objects.create(**s)


def seed_page_seo(apps, schema_editor):
    """Create/update PageSEO records with Tangier-optimized content."""
    PageSEO = apps.get_model('seo', 'PageSEO')
    
    pages = [
        {
            'page_identifier': 'home',
            'meta_title': 'VR Creation | Production visuelle & 3D \u00e0 Tanger',
            'meta_title_fr': 'VR Creation | Production visuelle & 3D \u00e0 Tanger',
            'meta_title_en': 'VR Creation | Visual Production & 3D in Tangier',
            'meta_title_ar': 'VR Creation | \u0625\u0646\u062a\u0627\u062c \u0628\u0635\u0631\u064a \u0648 3D \u0641\u064a \u0637\u0646\u062c\u0629',
            'meta_description': 'Agence de mod\u00e9lisation 3D, photographie, branding et visites virtuelles \u00e0 Tanger. Production visuelle haut de gamme pour le Nord du Maroc.',
            'meta_description_fr': 'Agence de mod\u00e9lisation 3D, photographie, branding et visites virtuelles \u00e0 Tanger. Production visuelle haut de gamme pour le Nord du Maroc.',
            'meta_description_en': '3D modeling, photography, branding and virtual tour agency in Tangier. Premium visual production for Northern Morocco.',
            'meta_description_ar': '\u0648\u0643\u0627\u0644\u0629 \u0646\u0645\u0630\u062c\u0629 3D\u060c \u062a\u0635\u0648\u064a\u0631\u060c \u0628\u0631\u0627\u0646\u062f\u064a\u0646\u063a \u0648\u062c\u0648\u0644\u0627\u062a \u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0629 \u0641\u064a \u0637\u0646\u062c\u0629.',
            'keywords': 'mod\u00e9lisation 3D Tanger, photographie Tanger, branding Tanger, visite virtuelle Nord Maroc, production visuelle',
        },
        {
            'page_identifier': 'about',
            'meta_title': '\u00c0 propos de VR Creation | Agence visuelle Tanger',
            'meta_title_fr': '\u00c0 propos de VR Creation | Agence visuelle Tanger',
            'meta_title_en': 'About VR Creation | Visual Agency Tangier',
            'meta_title_ar': '\u062d\u0648\u0644 VR Creation | \u0648\u0643\u0627\u0644\u0629 \u0628\u0635\u0631\u064a\u0629 \u0637\u0646\u062c\u0629',
            'meta_description': 'D\u00e9couvrez VR Creation, agence de production visuelle \u00e0 Tanger sp\u00e9cialis\u00e9e en 3D, photo, branding. \u00c9quipe cr\u00e9ative au service du Nord du Maroc.',
            'meta_description_fr': 'D\u00e9couvrez VR Creation, agence de production visuelle \u00e0 Tanger sp\u00e9cialis\u00e9e en 3D, photo, branding. \u00c9quipe cr\u00e9ative au service du Nord du Maroc.',
            'meta_description_en': 'Discover VR Creation, visual production agency in Tangier specializing in 3D, photo, branding. Creative team serving Northern Morocco.',
            'meta_description_ar': '\u0627\u0643\u062a\u0634\u0641 VR Creation\u060c \u0648\u0643\u0627\u0644\u0629 \u0625\u0646\u062a\u0627\u062c \u0628\u0635\u0631\u064a \u0641\u064a \u0637\u0646\u062c\u0629 \u0645\u062a\u062e\u0635\u0635\u0629 \u0641\u064a 3D \u0648\u0627\u0644\u062a\u0635\u0648\u064a\u0631 \u0648\u0627\u0644\u0628\u0631\u0627\u0646\u062f\u064a\u0646\u063a.',
            'keywords': 'agence visuelle Tanger, VR Creation, production 3D Maroc, branding Nord Maroc',
        },
        {
            'page_identifier': 'services',
            'meta_title': 'Nos services | VR Creation Tanger',
            'meta_title_fr': 'Nos services | VR Creation Tanger',
            'meta_title_en': 'Our Services | VR Creation Tangier',
            'meta_title_ar': '\u062e\u062f\u0645\u0627\u062a\u0646\u0627 | VR Creation \u0637\u0646\u062c\u0629',
            'meta_description': '3D, visites virtuelles 360\u00b0, photographie, branding, animation, marketing digital. Services de production visuelle \u00e0 Tanger, Nord du Maroc.',
            'meta_description_fr': '3D, visites virtuelles 360\u00b0, photographie, branding, animation, marketing digital. Services de production visuelle \u00e0 Tanger, Nord du Maroc.',
            'meta_description_en': '3D, 360\u00b0 virtual tours, photography, branding, animation, digital marketing. Visual production services in Tangier, Northern Morocco.',
            'meta_description_ar': '3D\u060c \u062c\u0648\u0644\u0627\u062a \u0627\u0641\u062a\u0631\u0627\u0636\u064a\u0629 360\u00b0\u060c \u062a\u0635\u0648\u064a\u0631\u060c \u0628\u0631\u0627\u0646\u062f\u064a\u0646\u063a\u060c \u0631\u0633\u0648\u0645 \u0645\u062a\u062d\u0631\u0643\u0629. \u062e\u062f\u0645\u0627\u062a \u0625\u0646\u062a\u0627\u062c \u0628\u0635\u0631\u064a \u0641\u064a \u0637\u0646\u062c\u0629.',
            'keywords': 'services 3D Tanger, photographie professionnelle Tanger, branding Maroc, visite virtuelle 360',
        },
        {
            'page_identifier': 'contact',
            'meta_title': 'Contact | VR Creation Tanger \u2014 Devis gratuit',
            'meta_title_fr': 'Contact | VR Creation Tanger \u2014 Devis gratuit',
            'meta_title_en': 'Contact | VR Creation Tangier \u2014 Free Quote',
            'meta_title_ar': '\u0627\u062a\u0635\u0644 \u0628\u0646\u0627 | VR Creation \u0637\u0646\u062c\u0629 \u2014 \u0639\u0631\u0636 \u0623\u0633\u0639\u0627\u0631 \u0645\u062c\u0627\u0646\u064a',
            'meta_description': 'Contactez VR Creation \u00e0 Tanger pour un devis gratuit. T\u00e9l\u00e9phone, WhatsApp, email. Bureaux Ibn Batouta, Av. Youssef Ibn Tachfine.',
            'meta_description_fr': 'Contactez VR Creation \u00e0 Tanger pour un devis gratuit. T\u00e9l\u00e9phone, WhatsApp, email. Bureaux Ibn Batouta, Av. Youssef Ibn Tachfine.',
            'meta_description_en': 'Contact VR Creation in Tangier for a free quote. Phone, WhatsApp, email. Ibn Batouta offices, Av. Youssef Ibn Tachfine.',
            'meta_description_ar': '\u062a\u0648\u0627\u0635\u0644 \u0645\u0639 VR Creation \u0641\u064a \u0637\u0646\u062c\u0629 \u0644\u0644\u062d\u0635\u0648\u0644 \u0639\u0644\u0649 \u0639\u0631\u0636 \u0623\u0633\u0639\u0627\u0631 \u0645\u062c\u0627\u0646\u064a.',
            'keywords': 'contact VR Creation, devis 3D Tanger, agence visuelle Tanger',
        },
        {
            'page_identifier': 'blog',
            'meta_title': 'Blog | VR Creation \u2014 Actualit\u00e9s visuelles',
            'meta_title_fr': 'Blog | VR Creation \u2014 Actualit\u00e9s visuelles',
            'meta_title_en': 'Blog | VR Creation \u2014 Visual News',
            'meta_title_ar': '\u0627\u0644\u0645\u062f\u0648\u0646\u0629 | VR Creation \u2014 \u0623\u062e\u0628\u0627\u0631 \u0628\u0635\u0631\u064a\u0629',
            'meta_description': 'Conseils, tendances et actualit\u00e9s sur la 3D, la photographie, le branding et le marketing visuel par VR Creation Tanger.',
            'meta_description_fr': 'Conseils, tendances et actualit\u00e9s sur la 3D, la photographie, le branding et le marketing visuel par VR Creation Tanger.',
            'meta_description_en': 'Tips, trends and news on 3D, photography, branding and visual marketing by VR Creation Tangier.',
            'meta_description_ar': '\u0646\u0635\u0627\u0626\u062d \u0648\u0627\u062a\u062c\u0627\u0647\u0627\u062a \u0648\u0623\u062e\u0628\u0627\u0631 \u062d\u0648\u0644 3D \u0648\u0627\u0644\u062a\u0635\u0648\u064a\u0631 \u0648\u0627\u0644\u0628\u0631\u0627\u0646\u062f\u064a\u0646\u063a.',
            'keywords': 'blog 3D, photographie tendances, marketing visuel Maroc',
        },
        {
            'page_identifier': 'promotions',
            'meta_title': 'Offres & Packs | VR Creation Tanger',
            'meta_title_fr': 'Offres & Packs | VR Creation Tanger',
            'meta_title_en': 'Offers & Packages | VR Creation Tangier',
            'meta_title_ar': '\u0627\u0644\u0639\u0631\u0648\u0636 | VR Creation \u0637\u0646\u062c\u0629',
            'meta_description': 'D\u00e9couvrez nos packs et offres sp\u00e9ciales en production visuelle, 3D et branding \u00e0 Tanger. Tarifs comp\u00e9titifs pour le Nord du Maroc.',
            'meta_description_fr': 'D\u00e9couvrez nos packs et offres sp\u00e9ciales en production visuelle, 3D et branding \u00e0 Tanger. Tarifs comp\u00e9titifs pour le Nord du Maroc.',
            'meta_description_en': 'Discover our packages and special offers in visual production, 3D and branding in Tangier. Competitive rates for Northern Morocco.',
            'meta_description_ar': '\u0627\u0643\u062a\u0634\u0641 \u0628\u0627\u0642\u0627\u062a\u0646\u0627 \u0648\u0639\u0631\u0648\u0636\u0646\u0627 \u0627\u0644\u062e\u0627\u0635\u0629 \u0641\u064a \u0627\u0644\u0625\u0646\u062a\u0627\u062c \u0627\u0644\u0628\u0635\u0631\u064a.',
            'keywords': 'offres VR Creation, packs 3D Tanger, promotions branding',
        },
        {
            'page_identifier': 'legal',
            'meta_title': 'Mentions l\u00e9gales | VR Creation',
            'meta_description': 'Mentions l\u00e9gales du site VR Creation Company, agence de production visuelle \u00e0 Tanger, Maroc.',
            'no_index': True,
            'keywords': '',
        },
        {
            'page_identifier': 'privacy',
            'meta_title': 'Politique de confidentialit\u00e9 | VR Creation',
            'meta_description': 'Politique de confidentialit\u00e9 et protection des donn\u00e9es personnelles de VR Creation Company.',
            'no_index': True,
            'keywords': '',
        },
        {
            'page_identifier': 'cookies',
            'meta_title': 'Politique de cookies | VR Creation',
            'meta_description': 'Informations sur l\u2019utilisation des cookies sur le site VR Creation Company.',
            'no_index': True,
            'keywords': '',
        },
    ]
    
    for p in pages:
        ident = p.pop('page_identifier')
        obj, created = PageSEO.objects.get_or_create(page_identifier=ident, defaults=p)
        if not created:
            for k, v in p.items():
                setattr(obj, k, v)
            obj.save()


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0017_seed_promotions_and_fix_photos'),
        ('services', '0001_initial'),
        ('seo', '0002_pageseo_keywords_pageseo_keywords_ar_and_more'),
    ]
    
    operations = [
        migrations.RunPython(update_site_settings, migrations.RunPython.noop),
        migrations.RunPython(rename_branding_service, migrations.RunPython.noop),
        migrations.RunPython(update_process_steps, migrations.RunPython.noop),
        migrations.RunPython(seed_page_seo, migrations.RunPython.noop),
    ]
