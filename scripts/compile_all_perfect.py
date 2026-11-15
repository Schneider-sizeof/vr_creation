import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
import django
django.setup()

import re
from django.template.loader import get_template
from django.templatetags.i18n import BlockTranslateNode
import rebuild_translations as r
import compile_messages

BLOCKTRANS_EXACT_EN = {
    'Expertise visuelle 3D et captation immersive à %(city_name)s': '3D Visual Expertise & Immersive Media in %(city_name)s',
    'Bonjour, je souhaite un devis pour un projet à %(city_name)s.': 'Hello, I would like a quote for a project in %(city_name)s.',
    'Nos solutions visuelles déployées à %(city_name)s': 'Our Visual Solutions Deployed in %(city_name)s',
    'Projets types réalisés à %(city_name)s': 'Typical Projects Executed in %(city_name)s',
    "Logistique d'intervention à %(city_name)s": 'Field Intervention Logistics in %(city_name)s',
    'Questions fréquentes sur nos services à %(city_name)s': 'Frequently Asked Questions about our services in %(city_name)s',
    'Villes voisines de %(city_name)s également couvertes': 'Nearby Cities around %(city_name)s also covered',
    'Prêt à valoriser votre projet à %(city_name)s ?': 'Ready to showcase your project in %(city_name)s?',
    'Contactez notre équipe basée à Tanger pour organiser un repérage sur site à %(city_name)s et obtenir une proposition technique chiffrée sous 24h.': 'Contact our Tangier team to schedule an on-site visit in %(city_name)s and receive a detailed quote within 24h.',
    'Bonjour, je souhaite démarrer un projet de production visuelle à %(city_name)s. Pouvez-vous me transmettre une offre ?': 'Hello, I would like to start a visual production project in %(city_name)s. Could you send me an offer?',
    'Découvrir nos services à %(city_name)s': 'Explore our services in %(city_name)s',
    'Depuis nos bureaux à Tanger, nos équipes interviennent sur l\'ensemble du littoral et de l\'arrière-pays du Nord marocain : Tétouan, Asilah, Larache, Chefchaouen, Al Hoceima, M\'diq, Martil et Fnideq. <a href="%(hub_url)s" class="text-primary font-semibold hover:underline">Découvrez le détail de nos zones d\'intervention &rarr;</a>': 'From our Tangier headquarters, our crews operate across the entire Northern coastline and interior: Tetouan, Asilah, Larache, Chefchaouen, Al Hoceima, M\'diq, Martil, and Fnideq. <a href="%(hub_url)s" class="text-primary font-semibold hover:underline">Explore our full service areas &rarr;</a>',
}

BLOCKTRANS_EXACT_AR = {
    'Expertise visuelle 3D et captation immersive à %(city_name)s': 'الخبرة البصرية 3D والتصوير التفاعلي الغامر في %(city_name)s',
    'Bonjour, je souhaite un devis pour un projet à %(city_name)s.': 'مرحباً، أود الحصول على عرض أسعار لمشروع في %(city_name)s.',
    'Nos solutions visuelles déployées à %(city_name)s': 'حلولنا البصرية المتوفرة في %(city_name)s',
    'Projets types réalisés à %(city_name)s': 'نماذج المشاريع المنجزة في %(city_name)s',
    "Logistique d'intervention à %(city_name)s": 'الترتيبات اللوجستية للتدخل في %(city_name)s',
    'Questions fréquentes sur nos services à %(city_name)s': 'الأسئلة الشائعة حول خدماتنا في %(city_name)s',
    'Villes voisines de %(city_name)s également couvertes': 'المدن المجاورة لـ %(city_name)s المشمولة بالتغطية أيضاً',
    'Prêt à valoriser votre projet à %(city_name)s ?': 'هل أنتم مستعدون لتثمين مشروعكم في %(city_name)s؟',
    'Contactez notre équipe basée à Tanger pour organiser un repérage sur site à %(city_name)s et obtenir une proposition technique chiffrée sous 24h.': 'تواصلوا مع فريقنا بطنجة لبرمجة معاينة ميدانية في %(city_name)s والحصول على عرض تقني مفصل خلال 24 ساعة.',
    'Bonjour, je souhaite démarrer un projet de production visuelle à %(city_name)s. Pouvez-vous me transmettre une offre ?': 'مرحباً، أرغب في بدء مشروع إنتاج بصري في %(city_name)s. هل يمكنكم تزويدي بعرض؟',
    'Découvrir nos services à %(city_name)s': 'اكتشف خدماتنا في %(city_name)s',
    'Depuis nos bureaux à Tanger, nos équipes interviennent sur l\'ensemble du littoral et de l\'arrière-pays du Nord marocain : Tétouan, Asilah, Larache, Chefchaouen, Al Hoceima, M\'diq, Martil et Fnideq. <a href="%(hub_url)s" class="text-primary font-semibold hover:underline">Découvrez le détail de nos zones d\'intervention &rarr;</a>': 'انطلاقاً من مكاتبنا في طنجة، تتدخل فرقنا في كامل الساحل والظهير الشمالي للمغرب: تطوان، أصيلة، العرائش، شفشاون، الحسيمة، المضيق، مرتيل والفنيدق. <a href="%(hub_url)s" class="text-primary font-semibold hover:underline">اكتشفوا تفاصيل مناطق تدخلنا &rarr;</a>',
}

# Collect all strings:
all_strings = set(r.trans_strings)

# Add exact blocktrans tokens
for template_path in [
    'services/city_detail.html', 'services/city_hub.html', 'core/about.html',
    'core/privacy_policy.html', 'portfolio/virtual_tours.html', 'services/service_list.html'
]:
    t = get_template(template_path)
    nodes = t.template.nodelist.get_nodes_by_type(BlockTranslateNode)
    for n in nodes:
        tok = n.render_token_list(n.singular)[0]
        all_strings.add(tok)

from scripts.update_all_translations import ADDITIONAL_EN, ADDITIONAL_AR

from scripts.rebuild_and_compile import BLOCKTRANS_EN, BLOCKTRANS_AR

EN = dict(r.EN)
EN.update(ADDITIONAL_EN)
EN.update(BLOCKTRANS_EN)
EN.update(BLOCKTRANS_EXACT_EN)

AR = dict(r.AR)
AR.update(ADDITIONAL_AR)
AR.update(BLOCKTRANS_AR)
AR.update(BLOCKTRANS_EXACT_AR)

# Check missing
missing_en = [s for s in all_strings if s not in EN]
missing_ar = [s for s in all_strings if s not in AR]

print(f"Total strings: {len(all_strings)}")
print(f"Missing EN: {len(missing_en)}")
print(f"Missing AR: {len(missing_ar)}")

if missing_en:
    for m in missing_en:
        print(f"  Missing EN: {repr(m)}")
if missing_ar:
    for m in missing_ar:
        print(f"  Missing AR: {repr(m)}")

assert len(missing_en) == 0, f"{len(missing_en)} strings missing in EN!"
assert len(missing_ar) == 0, f"{len(missing_ar)} strings missing in AR!"

FR = {s: s for s in all_strings}

LOCALE_DIR = r.LOCALE_DIR
for lang, trans in [('fr', FR), ('en', EN), ('ar', AR)]:
    po = r.generate_po(lang, trans, all_strings)
    path = os.path.join(LOCALE_DIR, lang, 'LC_MESSAGES', 'django.po')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(po)
    mo_path = os.path.join(LOCALE_DIR, lang, 'LC_MESSAGES', 'django.mo')
    compile_messages.generate_mo(path, mo_path)
    print(f"✓ Generated & compiled {lang}: {len(all_strings)} entries in django.mo")

print("\nSUCCESS: All templates and blocktrans strings verified and compiled!")
