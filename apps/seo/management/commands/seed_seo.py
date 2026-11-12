"""
Management command to seed initial SEO data with locally-relevant keywords
for Tanger/Morocco VR real estate audience.
All titles â‰¤ 60 chars, all descriptions â‰¤ 155 chars, keyword first, zero emojis.
"""
from django.core.management.base import BaseCommand
from apps.seo.models import PageSEO


SEO_DATA = [
    {
        'page_identifier': 'home',
        'meta_title_fr': 'ModÃ©lisation 3D & visites 360Â° Ã  Tanger',
        'meta_title_en': '3D Modeling & Virtual Tours in Tanger',
        'meta_title_ar': 'Ù†Ù…Ø°Ø¬Ø© Ø«Ù„Ø§Ø«ÙŠØ© Ø§Ù„Ø£Ø¨Ø¹Ø§Ø¯ ÙˆØ¬ÙˆÙ„Ø§Øª Ø§ÙØªØ±Ø§Ø¶ÙŠØ© Ø¨Ø·Ù†Ø¬Ø©',
        'meta_description_fr': 'Agence 3D Ã  Tanger : modÃ©lisation 3D, visites virtuelles 360Â°, drone et marketing immobilier au Maroc. Devis gratuit et accompagnement dÃ©diÃ©.',
        'meta_description_en': 'Tanger 3D studio: 3D modeling, 360Â° virtual tours, drone capture and real estate marketing in Morocco. Free quote & dedicated support.',
        'meta_description_ar': 'Ø§Ø³ØªÙˆØ¯ÙŠÙˆ Ø«Ù„Ø§Ø«ÙŠ Ø§Ù„Ø£Ø¨Ø¹Ø§Ø¯ Ø¨Ø·Ù†Ø¬Ø©: Ù†Ù…Ø°Ø¬Ø© Ø«Ù„Ø§Ø«ÙŠØ© Ø§Ù„Ø£Ø¨Ø¹Ø§Ø¯ØŒ Ø¬ÙˆÙ„Ø§Øª Ø§ÙØªØ±Ø§Ø¶ÙŠØ© 360Â°ØŒ ØªØµÙˆÙŠØ± Ø¬ÙˆÙŠ ÙˆØªØ³ÙˆÙŠÙ‚ Ø¹Ù‚Ø§Ø±ÙŠ Ø¨Ø§Ù„Ù…ØºØ±Ø¨. Ø¹Ø±Ø¶ Ø£Ø³Ø¹Ø§Ø± Ù…Ø¬Ø§Ù†ÙŠ.',
        'keywords_fr': 'modÃ©lisation 3D Tanger, visite virtuelle immobilier Maroc, rendu 3D promoteur, rÃ©alitÃ© virtuelle Tanger',
        'keywords_en': '3D modeling Tanger, virtual tour Morocco, 3D rendering real estate, virtual reality Tanger',
        'keywords_ar': 'Ù†Ù…Ø°Ø¬Ø© Ø«Ù„Ø§Ø«ÙŠØ© Ø§Ù„Ø£Ø¨Ø¹Ø§Ø¯ Ø·Ù†Ø¬Ø©, Ø¬ÙˆÙ„Ø© Ø§ÙØªØ±Ø§Ø¶ÙŠØ© Ø¹Ù‚Ø§Ø±Ø§Øª Ø§Ù„Ù…ØºØ±Ø¨, ÙˆØ§Ù‚Ø¹ Ø§ÙØªØ±Ø§Ø¶ÙŠ Ø·Ù†Ø¬Ø©',
    },
    {
        'page_identifier': 'services',
        'meta_title_fr': 'Services 3D, visite virtuelle & branding',
        'meta_title_en': '3D Services, Virtual Tour & Branding',
        'meta_title_ar': 'Ø®Ø¯Ù…Ø§Øª Ø«Ù„Ø§Ø«ÙŠØ© Ø§Ù„Ø£Ø¨Ø¹Ø§Ø¯ ÙˆØ¬ÙˆÙ„Ø§Øª Ø§ÙØªØ±Ø§Ø¶ÙŠØ© Ø¨Ø·Ù†Ø¬Ø©',
        'meta_description_fr': 'DÃ©couvrez nos solutions 3D Ã  Tanger : modÃ©lisation 3D, visites 360Â°, photographie drone, branding et lead generation pour promoteurs immobiliers.',
        'meta_description_en': 'Explore our 3D solutions in Tanger: 3D modeling, 360 tours, drone photography, visual branding and lead generation for property developers.',
        'meta_description_ar': 'Ø§ÙƒØªØ´Ù Ø­Ù„ÙˆÙ„Ù†Ø§ Ø«Ù„Ø§Ø«ÙŠØ© Ø§Ù„Ø£Ø¨Ø¹Ø§Ø¯ Ø¨Ø·Ù†Ø¬Ø©: Ù†Ù…Ø°Ø¬Ø© 3DØŒ Ø¬ÙˆÙ„Ø§Øª 360ØŒ ØªØµÙˆÙŠØ± Ø¯Ø±ÙˆÙ†ØŒ Ù‡ÙˆÙŠØ© Ø¨ØµØ±ÙŠØ© ÙˆØ¬Ù„Ø¨ Ø¹Ù…Ù„Ø§Ø¡ Ù„Ù„Ù…Ø·ÙˆØ±ÙŠÙ† Ø§Ù„Ø¹Ù‚Ø§Ø±ÙŠÙŠÙ†.',
        'keywords_fr': 'rendu 3D immobilier Tanger, visite virtuelle 360 Maroc, capture 360 Tanger, branding promoteur immobilier',
        'keywords_en': '3D rendering Tanger, 360 virtual tour Morocco, drone capture Tanger, real estate branding',
        'keywords_ar': 'Ø¹Ø±Ø¶ Ø«Ù„Ø§Ø«ÙŠ Ø§Ù„Ø£Ø¨Ø¹Ø§Ø¯ Ø¹Ù‚Ø§Ø±Ø§Øª Ø·Ù†Ø¬Ø©, Ø¬ÙˆÙ„Ø© Ø§ÙØªØ±Ø§Ø¶ÙŠØ© 360 Ø§Ù„Ù…ØºØ±Ø¨, ØªØµÙˆÙŠØ± Ø¬ÙˆÙŠ Ø·Ù†Ø¬Ø©',
    },
    {
        'page_identifier': 'portfolio',
        'meta_title_fr': 'RÃ©alisations 3D & visites immersives Tanger',
        'meta_title_en': '3D Projects & Virtual Tours Tanger',
        'meta_title_ar': 'Ù…Ø´Ø§Ø±ÙŠØ¹ Ø«Ù„Ø§Ø«ÙŠØ© Ø§Ù„Ø£Ø¨Ø¹Ø§Ø¯ ÙˆØ¬ÙˆÙ„Ø§Øª ØºØ§Ù…Ø±Ø© Ø·Ù†Ø¬Ø©',
        'meta_description_fr': 'Explorez nos rendus 3D photorÃ©alistes, visites virtuelles immersives et vidÃ©os dâ€™architecture pour promoteurs Ã  Tanger et au Maroc.',
        'meta_description_en': 'Explore our photorealistic 3D renders, immersive virtual tours and architectural videos for property developers in Tanger and Morocco.',
        'meta_description_ar': 'Ø§Ø³ØªÙƒØ´Ù Ø¹Ø±ÙˆØ¶Ù†Ø§ Ø§Ù„ÙˆØ§Ù‚Ø¹ÙŠØ© Ø«Ù„Ø§Ø«ÙŠØ© Ø§Ù„Ø£Ø¨Ø¹Ø§Ø¯ ÙˆØ¬ÙˆÙ„Ø§ØªÙ†Ø§ Ø§Ù„Ø§ÙØªØ±Ø§Ø¶ÙŠØ© Ø§Ù„ØºØ§Ù…Ø±Ø© Ù„Ù„Ù…Ø·ÙˆØ±ÙŠÙ† Ø§Ù„Ø¹Ù‚Ø§Ø±ÙŠÙŠÙ† ÙÙŠ Ø·Ù†Ø¬Ø© ÙˆØ§Ù„Ù…ØºØ±Ø¨.',
        'keywords_fr': 'projets 3D immobilier Tanger, rÃ©alisations visite virtuelle Maroc, portfolio rendu 3D Tanger',
        'keywords_en': '3D real estate projects Tanger, virtual tour portfolio Morocco, 3D architectural renders',
        'keywords_ar': 'Ù…Ø´Ø§Ø±ÙŠØ¹ Ø«Ù„Ø§Ø«ÙŠØ© Ø§Ù„Ø£Ø¨Ø¹Ø§Ø¯ Ø¹Ù‚Ø§Ø±Ø§Øª Ø·Ù†Ø¬Ø©, Ù…Ø¹Ø±Ø¶ Ø¬ÙˆÙ„Ø§Øª Ø§ÙØªØ±Ø§Ø¶ÙŠØ© Ø§Ù„Ù…ØºØ±Ø¨',
    },
    {
        'page_identifier': 'about',
        'meta_title_fr': 'Agence 3D & rÃ©alitÃ© virtuelle Ã  Tanger',
        'meta_title_en': '3D Agency & Virtual Reality in Tanger',
        'meta_title_ar': 'ÙˆÙƒØ§Ù„Ø© Ø«Ù„Ø§Ø«ÙŠØ© Ø§Ù„Ø£Ø¨Ø¹Ø§Ø¯ ÙˆÙˆØ§Ù‚Ø¹ Ø§ÙØªØ±Ø§Ø¶ÙŠ Ø¨Ø·Ù†Ø¬Ø©',
        'meta_description_fr': 'VR Creation est le studio de modÃ©lisation 3D et de production visuelle haut de gamme Ã  Tanger, dÃ©diÃ© aux promoteurs et architectes.',
        'meta_description_en': 'VR Creation is the premium 3D modeling and visual production agency in Tanger, dedicated to architects and real estate developers.',
        'meta_description_ar': 'ÙÙŠ Ø¢Ø± ÙƒØ±ÙŠÙŠØ´Ù† Ù‡ÙŠ Ø§Ù„ÙˆÙƒØ§Ù„Ø© Ø§Ù„Ø±Ø§Ø¦Ø¯Ø© ÙÙŠ Ø§Ù„Ù†Ù…Ø°Ø¬Ø© Ø«Ù„Ø§Ø«ÙŠØ© Ø§Ù„Ø£Ø¨Ø¹Ø§Ø¯ ÙˆØ§Ù„Ø¥Ù†ØªØ§Ø¬ Ø§Ù„Ø¨ØµØ±ÙŠ Ø¨Ø·Ù†Ø¬Ø© Ù„Ø®Ø¯Ù…Ø© Ø§Ù„Ù…Ù‡Ù†Ø¯Ø³ÙŠÙ† ÙˆØ§Ù„Ù…Ø·ÙˆØ±ÙŠÙ† Ø§Ù„Ø¹Ù‚Ø§Ø±ÙŠÙŠÙ†.',
        'keywords_fr': 'agence 3D Tanger, entreprise rÃ©alitÃ© virtuelle Maroc, VR Creation Tanger, studio modÃ©lisation 3D',
        'keywords_en': '3D agency Tanger, virtual reality company Morocco, VR Creation Tanger, 3D modeling studio',
        'keywords_ar': 'ÙˆÙƒØ§Ù„Ø© Ø«Ù„Ø§Ø«ÙŠØ© Ø§Ù„Ø£Ø¨Ø¹Ø§Ø¯ Ø·Ù†Ø¬Ø©, Ø´Ø±ÙƒØ© ÙˆØ§Ù‚Ø¹ Ø§ÙØªØ±Ø§Ø¶ÙŠ Ø§Ù„Ù…ØºØ±Ø¨',
    },
    {
        'page_identifier': 'contact',
        'meta_title_fr': 'Contact & devis gratuit Ã  Tanger',
        'meta_title_en': 'Contact & Free Quote in Tanger',
        'meta_title_ar': 'Ø§ØªØµÙ„ Ø¨Ù†Ø§ ÙˆØ¹Ø±Ø¶ Ø£Ø³Ø¹Ø§Ø± Ù…Ø¬Ø§Ù†ÙŠ Ø¨Ø·Ù†Ø¬Ø©',
        'meta_description_fr': 'Demandez votre devis gratuit sous 24h pour vos projets 3D, visites virtuelles et supports visuels Ã  Tanger. Ã‰quipe Ã  votre Ã©coute.',
        'meta_description_en': 'Request your free quote within 24h for 3D renderings, virtual tours and visual assets in Tanger. Dedicated team at your service.',
        'meta_description_ar': 'Ø§Ø·Ù„Ø¨ Ø¹Ø±Ø¶ Ø£Ø³Ø¹Ø§Ø± Ù…Ø¬Ø§Ù†ÙŠ Ø®Ù„Ø§Ù„ 24 Ø³Ø§Ø¹Ø© Ù„Ù…Ø´Ø§Ø±ÙŠØ¹Ùƒ Ø«Ù„Ø§Ø«ÙŠØ© Ø§Ù„Ø£Ø¨Ø¹Ø§Ø¯ ÙˆØ§Ù„Ø¬ÙˆÙ„Ø§Øª Ø§Ù„Ø§ÙØªØ±Ø§Ø¶ÙŠØ© Ø¨Ø·Ù†Ø¬Ø©. ÙØ±ÙŠÙ‚Ù†Ø§ ÙÙŠ Ø®Ø¯Ù…ØªÙƒÙ….',
        'keywords_fr': 'devis modÃ©lisation 3D Tanger, contact agence VR Maroc, prix visite virtuelle immobilier',
        'keywords_en': '3D modeling quote Tanger, contact VR agency Morocco, virtual tour price Morocco',
        'keywords_ar': 'Ø¹Ø±Ø¶ Ø£Ø³Ø¹Ø§Ø± Ù†Ù…Ø°Ø¬Ø© Ø«Ù„Ø§Ø«ÙŠØ© Ø§Ù„Ø£Ø¨Ø¹Ø§Ø¯ Ø·Ù†Ø¬Ø©, Ø§ØªØµØ§Ù„ ÙˆÙƒØ§Ù„Ø© ÙˆØ§Ù‚Ø¹ Ø§ÙØªØ±Ø§Ø¶ÙŠ',
    },
    {
        'page_identifier': 'blog',
        'meta_title_fr': 'Blog 3D, visite virtuelle & immobilier',
        'meta_title_en': '3D, Virtual Tour & Real Estate Blog',
        'meta_title_ar': 'Ù…Ø¯ÙˆÙ†Ø© Ø«Ù„Ø§Ø«ÙŠ Ø§Ù„Ø£Ø¨Ø¹Ø§Ø¯ ÙˆØ§Ù„ÙˆØ§Ù‚Ø¹ Ø§Ù„Ø§ÙØªØ±Ø§Ø¶ÙŠ',
        'meta_description_fr': 'Conseils pratiques, tendances 3D, visites virtuelles et stratÃ©gies de commercialisation immobiliÃ¨re Ã  Tanger et au Maroc.',
        'meta_description_en': 'Practical advice, 3D trends, virtual tours and property marketing strategies in Tanger and Morocco.',
        'meta_description_ar': 'Ù†ØµØ§Ø¦Ø­ Ø¹Ù…Ù„ÙŠØ© ÙˆØ§ØªØ¬Ø§Ù‡Ø§Øª Ø§Ù„Ù†Ù…Ø°Ø¬Ø© Ø«Ù„Ø§Ø«ÙŠØ© Ø§Ù„Ø£Ø¨Ø¹Ø§Ø¯ ÙˆØ§Ù„Ø¬ÙˆÙ„Ø§Øª Ø§Ù„Ø§ÙØªØ±Ø§Ø¶ÙŠØ© ÙˆØ§Ù„ØªØ³ÙˆÙŠÙ‚ Ø§Ù„Ø¹Ù‚Ø§Ø±ÙŠ ÙÙŠ Ø·Ù†Ø¬Ø© ÙˆØ§Ù„Ù…ØºØ±Ø¨.',
        'keywords_fr': 'actualitÃ©s immobilier 3D Maroc, blog rÃ©alitÃ© virtuelle Tanger, conseils marketing immobilier',
        'keywords_en': '3D real estate news Morocco, virtual reality blog Tanger, real estate marketing tips',
        'keywords_ar': 'Ø£Ø®Ø¨Ø§Ø± Ø¹Ù‚Ø§Ø±Ø§Øª Ø«Ù„Ø§Ø«ÙŠØ© Ø§Ù„Ø£Ø¨Ø¹Ø§Ø¯ Ø§Ù„Ù…ØºØ±Ø¨, Ù…Ø¯ÙˆÙ†Ø© ÙˆØ§Ù‚Ø¹ Ø§ÙØªØ±Ø§Ø¶ÙŠ Ø·Ù†Ø¬Ø©',
    },
    {
        'page_identifier': 'promotions',
        'meta_title_fr': 'Packs marketing promoteur immobilier',
        'meta_title_en': 'Real Estate Marketing Packs Tanger',
        'meta_title_ar': 'Ø¨Ø§Ù‚Ø§Øª ØªØ³ÙˆÙŠÙ‚ Ù„Ù„Ù…Ø·ÙˆØ±ÙŠÙ† Ø§Ù„Ø¹Ù‚Ø§Ø±ÙŠÙŠÙ†',
        'meta_description_fr': 'Packs marketing tout-en-un pour promoteurs immobiliers Ã  Tanger : 3D, visites virtuelles, branding et vente sur commission.',
        'meta_description_en': 'All-in-one marketing packs for property developers in Tanger: 3D, virtual tours, branding and commission-based sales.',
        'meta_description_ar': 'Ø¨Ø§Ù‚Ø§Øª ØªØ³ÙˆÙŠÙ‚ÙŠØ© Ø´Ø§Ù…Ù„Ø© Ù„Ù„Ù…Ø·ÙˆØ±ÙŠÙ† Ø§Ù„Ø¹Ù‚Ø§Ø±ÙŠÙŠÙ† ÙÙŠ Ø·Ù†Ø¬Ø©: 3DØŒ Ø¬ÙˆÙ„Ø§Øª Ø§ÙØªØ±Ø§Ø¶ÙŠØ©ØŒ Ù‡ÙˆÙŠØ© Ø¨ØµØ±ÙŠØ© ÙˆØ¹Ø±ÙˆØ¶ Ø¨Ø§Ù„Ø¹Ù…ÙˆÙ„Ø©.',
        'keywords_fr': 'pack promoteur immobilier Tanger, offre visite virtuelle Maroc, marketing immobilier commission',
        'keywords_en': 'real estate developer pack Tanger, virtual tour offer Morocco, property marketing package',
        'keywords_ar': 'Ø¨Ø§Ù‚Ø© Ù…Ø·ÙˆØ± Ø¹Ù‚Ø§Ø±ÙŠ Ø·Ù†Ø¬Ø©, Ø¹Ø±Ø¶ Ø¬ÙˆÙ„Ø© Ø§ÙØªØ±Ø§Ø¶ÙŠØ© Ø§Ù„Ù…ØºØ±Ø¨',
    },
    {
        'page_identifier': 'virtual_tours',
        'meta_title_fr': 'Visites 360Â° & visites virtuelles Tanger',
        'meta_title_en': '360Â° Virtual Tours Showcase in Tanger',
        'meta_title_ar': 'Ø¬ÙˆÙ„Ø§Øª Ø§ÙØªØ±Ø§Ø¶ÙŠØ© 360 Ø¯Ø±Ø¬Ø© ÙÙŠ Ø·Ù†Ø¬Ø©',
        'meta_description_fr': 'DÃ©couvrez nos visites virtuelles 360Â° immersives pour l\'immobilier, showrooms et commerces Ã  Tanger. ExpÃ©rience interactive haut de gamme.',
        'meta_description_en': 'Explore our immersive 360Â° virtual tours for real estate, showrooms and shops in Tanger. High-end interactive experience.',
        'meta_description_ar': 'Ø§ÙƒØªØ´Ù Ø¬ÙˆÙ„Ø§ØªÙ†Ø§ Ø§Ù„Ø§ÙØªØ±Ø§Ø¶ÙŠØ© 360Â° Ø§Ù„ØºØ§Ù…Ø±Ø© Ù„Ù„Ø¹Ù‚Ø§Ø±Ø§Øª ÙˆØ§Ù„Ù…Ø¹Ø§Ø±Ø¶ ÙˆØ§Ù„Ù…Ø­Ù„Ø§Øª Ø§Ù„ØªØ¬Ø§Ø±ÙŠØ© ÙÙŠ Ø·Ù†Ø¬Ø©. ØªØ¬Ø±Ø¨Ø© ØªÙØ§Ø¹Ù„ÙŠØ© Ù…ØªÙ…ÙŠØ²Ø©.',
        'keywords_fr': 'visite virtuelle 360 Tanger, visite 360 immobilier Maroc, showroom virtuel Tanger',
        'keywords_en': '360 virtual tour Tanger, property virtual tour Morocco, virtual showroom Tanger',
        'keywords_ar': 'Ø¬ÙˆÙ„Ø© Ø§ÙØªØ±Ø§Ø¶ÙŠØ© 360 Ø·Ù†Ø¬Ø©, Ø¬ÙˆÙ„Ø© Ø¹Ù‚Ø§Ø±ÙŠØ© Ø§ÙØªØ±Ø§Ø¶ÙŠØ© Ø§Ù„Ù…ØºØ±Ø¨',
    },
    {
        'page_identifier': 'case_studies',
        'meta_title_fr': 'Ã‰tudes de cas & rÃ©sultats 3D Ã  Tanger',
        'meta_title_en': 'Case Studies & 3D Results in Tanger',
        'meta_title_ar': 'Ø¯Ø±Ø§Ø³Ø§Øª Ø§Ù„Ø­Ø§Ù„Ø© ÙˆÙ†ØªØ§Ø¦Ø¬ Ø§Ù„Ù…Ø´Ø§Ø±ÙŠØ¹ ÙÙŠ Ø·Ù†Ø¬Ø©',
        'meta_description_fr': 'DÃ©couvrez comment nos visuels 3D et visites virtuelles ont boostÃ© les ventes de nos clients promoteurs immobiliers Ã  Tanger.',
        'meta_description_en': 'Discover how our 3D renderings and virtual tours boosted property sales for real estate developers in Tanger.',
        'meta_description_ar': 'Ø§ÙƒØªØ´Ù ÙƒÙŠÙ Ø³Ø§Ù‡Ù…Øª Ø¹Ø±ÙˆØ¶Ù†Ø§ Ø«Ù„Ø§Ø«ÙŠØ© Ø§Ù„Ø£Ø¨Ø¹Ø§Ø¯ ÙˆØ¬ÙˆÙ„Ø§ØªÙ†Ø§ Ø§Ù„Ø§ÙØªØ±Ø§Ø¶ÙŠØ© ÙÙŠ ØªØ³Ø±ÙŠØ¹ Ù…Ø¨ÙŠØ¹Ø§Øª Ø§Ù„Ù…Ø·ÙˆØ±ÙŠÙ† Ø§Ù„Ø¹Ù‚Ø§Ø±ÙŠÙŠÙ† ÙÙŠ Ø·Ù†Ø¬Ø©.',
        'keywords_fr': 'Ã©tudes de cas 3D Tanger, ROI visite virtuelle immobilier, succÃ¨s marketing immobilier Maroc',
        'keywords_en': '3D case studies Tanger, virtual tour ROI real estate, property marketing success Morocco',
        'keywords_ar': 'Ø¯Ø±Ø§Ø³Ø§Øª Ø­Ø§Ù„Ø© Ø«Ù„Ø§Ø«ÙŠØ© Ø§Ù„Ø£Ø¨Ø¹Ø§Ø¯ Ø·Ù†Ø¬Ø©, Ø¹Ø§Ø¦Ø¯ Ø§Ù„Ø§Ø³ØªØ«Ù…Ø§Ø± Ø¬ÙˆÙ„Ø© Ø§ÙØªØ±Ø§Ø¶ÙŠØ©',
    },
    {
        'page_identifier': 'sitemap',
        'meta_title_fr': 'Plan du site & architecture de navigation',
        'meta_title_en': 'HTML Sitemap & Navigation Index',
        'meta_title_ar': 'Ø®Ø±ÙŠØ·Ø© Ø§Ù„Ù…ÙˆÙ‚Ø¹ ÙˆÙ‡ÙŠÙƒÙ„ Ø§Ù„ØªØµÙØ­',
        'meta_description_fr': 'Consultez le plan du site VR Creation Ã  Tanger : accÃ¨s direct Ã  tous nos services 3D, visites virtuelles, projets et articles.',
        'meta_description_en': 'Explore the VR Creation sitemap in Tanger: direct access to all our 3D services, virtual tours, portfolio and articles.',
        'meta_description_ar': 'ØªØµÙØ­ Ø®Ø±ÙŠØ·Ø© Ù…ÙˆÙ‚Ø¹ ÙÙŠ Ø¢Ø± ÙƒØ±ÙŠÙŠØ´Ù† Ø¨Ø·Ù†Ø¬Ø©: ÙˆØµÙˆÙ„ Ù…Ø¨Ø§Ø´Ø± Ù„Ø¬Ù…ÙŠØ¹ Ø®Ø¯Ù…Ø§ØªÙ†Ø§ Ø«Ù„Ø§Ø«ÙŠØ© Ø§Ù„Ø£Ø¨Ø¹Ø§Ø¯ ÙˆØ¬ÙˆÙ„Ø§ØªÙ†Ø§ ÙˆÙ…Ø´Ø§Ø±ÙŠØ¹Ù†Ø§ ÙˆÙ…Ù‚Ø§Ù„Ø§ØªÙ†Ø§.',
        'keywords_fr': 'plan du site VR Creation, architecture site 3D Tanger',
        'keywords_en': 'sitemap VR Creation, navigation index Tanger',
        'keywords_ar': 'Ø®Ø±ÙŠØ·Ø© Ø§Ù„Ù…ÙˆÙ‚Ø¹ ÙÙŠ Ø¢Ø± ÙƒØ±ÙŠÙŠØ´Ù† Ø·Ù†Ø¬Ø©',
    },
]


class Command(BaseCommand):
    help = 'Seed SEO data with strict character limits (title â‰¤ 60, desc â‰¤ 155) for all major pages.'

    def handle(self, *args, **options):
        created_count = 0
        updated_count = 0

        for item in SEO_DATA:
            page_id = item['page_identifier']
            defaults = {k: v for k, v in item.items() if k != 'page_identifier'}
            obj, created = PageSEO.objects.update_or_create(
                page_identifier=page_id,
                defaults=defaults,
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

