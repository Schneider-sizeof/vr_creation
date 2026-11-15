import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import rebuild_translations as r
from scripts.update_all_translations import ADDITIONAL_EN, ADDITIONAL_AR
import compile_messages

BLOCKTRANS_EN = {
    'Prêt à valoriser votre projet à {{ city_name }} ?': 'Ready to showcase your project in {{ city_name }}?',
    'Contactez notre équipe basée à Tanger pour organiser un repérage sur site à {{ city_name }} et obtenir une proposition technique chiffrée sous 24h.': 'Contact our Tangier team to schedule an on-site visit in {{ city_name }} and receive a detailed quote within 24h.',
    "Logistique d'intervention à {{ city_name }}": 'Field Intervention Logistics in {{ city_name }}',
    'Expertise visuelle 3D et captation immersive à {{ city_name }}': '3D Visual Expertise & Immersive Media in {{ city_name }}',
    'Nos solutions visuelles déployées à {{ city_name }}': 'Our Visual Solutions Deployed in {{ city_name }}',
    'Projets types réalisés à {{ city_name }}': 'Typical Projects Executed in {{ city_name }}',
    'Questions fréquentes sur nos services à {{ city_name }}': 'Frequently Asked Questions about our services in {{ city_name }}',
    'Villes voisines de {{ city_name }} également couvertes': 'Nearby Cities around {{ city_name }} also covered',
    'Découvrir nos services à {{ city_name }}': 'Explore our services in {{ city_name }}',
    'Bonjour, je souhaite un devis pour un projet à {{ city_name }}.': 'Hello, I would like a quote for a project in {{ city_name }}.',
    'Bonjour, je souhaite démarrer un projet de production visuelle à {{ city_name }}. Pouvez-vous me transmettre une offre ?': 'Hello, I would like to start a visual production project in {{ city_name }}. Could you send me an offer?',
    'Depuis nos bureaux à Tanger, nos équipes interviennent sur l\'ensemble du littoral et de l\'arrière-pays du Nord marocain : Tétouan, Asilah, Larache, Chefchaouen, Al Hoceima, M\'diq, Martil et Fnideq. <a href="{{ hub_url }}" class="text-primary font-semibold hover:underline">Découvrez le détail de nos zones d\'intervention &rarr;</a>': 'From our Tangier headquarters, our crews operate across the entire Northern coastline and interior: Tetouan, Asilah, Larache, Chefchaouen, Al Hoceima, M\'diq, Martil, and Fnideq. <a href="{{ hub_url }}" class="text-primary font-semibold hover:underline">Explore our full service areas &rarr;</a>'
}

BLOCKTRANS_AR = {
    'Prêt à valoriser votre projet à {{ city_name }} ?': 'هل أنتم مستعدون لتثمين مشروعكم في {{ city_name }}؟',
    'Contactez notre équipe basée à Tanger pour organiser un repérage sur site à {{ city_name }} et obtenir une proposition technique chiffrée sous 24h.': 'تواصلوا مع فريقنا بطنجة لبرمجة معاينة ميدانية في {{ city_name }} والحصول على عرض تقني مفصل خلال 24 ساعة.',
    "Logistique d'intervention à {{ city_name }}": 'الترتيبات اللوجستية للتدخل في {{ city_name }}',
    'Expertise visuelle 3D et captation immersive à {{ city_name }}': 'الخبرة البصرية 3D والتصوير التفاعلي الغامر في {{ city_name }}',
    'Nos solutions visuelles déployées à {{ city_name }}': 'حلولنا البصرية المتوفرة في {{ city_name }}',
    'Projets types réalisés à {{ city_name }}': 'نماذج المشاريع المنجزة في {{ city_name }}',
    'Questions fréquentes sur nos services à {{ city_name }}': 'الأسئلة الشائعة حول خدماتنا في {{ city_name }}',
    'Villes voisines de {{ city_name }} également couvertes': 'المدن المجاورة لـ {{ city_name }} المشمولة بالتغطية أيضاً',
    'Découvrir nos services à {{ city_name }}': 'اكتشف خدماتنا في {{ city_name }}',
    'Bonjour, je souhaite un devis pour un projet à {{ city_name }}.': 'مرحباً، أود الحصول على عرض أسعار لمشروع في {{ city_name }}.',
    'Bonjour, je souhaite démarrer un projet de production visuelle à {{ city_name }}. Pouvez-vous me transmettre une offre ?': 'مرحباً، أرغب في بدء مشروع إنتاج بصري في {{ city_name }}. هل يمكنكم تزويدي بعرض؟',
    'Depuis nos bureaux à Tanger, nos équipes interviennent sur l\'ensemble du littoral et de l\'arrière-pays du Nord marocain : Tétouan, Asilah, Larache, Chefchaouen, Al Hoceima, M\'diq, Martil et Fnideq. <a href="{{ hub_url }}" class="text-primary font-semibold hover:underline">Découvrez le détail de nos zones d\'intervention &rarr;</a>': 'انطلاقاً من مكاتبنا في طنجة، تتدخل فرقنا في كامل الساحل والظهير الشمالي للمغرب: تطوان، أصيلة، العرائش، شفشاون، الحسيمة، المضيق، مرتيل والفنيدق. <a href="{{ hub_url }}" class="text-primary font-semibold hover:underline">اكتشفوا تفاصيل مناطق تدخلنا &rarr;</a>'
}

# Merge all into r.EN and r.AR
r.EN.update(ADDITIONAL_EN)
r.EN.update(BLOCKTRANS_EN)

r.AR.update(ADDITIONAL_AR)
r.AR.update(BLOCKTRANS_AR)

# Check missing
missing_en = [s for s in r.trans_strings if s not in r.EN]
missing_ar = [s for s in r.trans_strings if s not in r.AR]

print(f"Total extracted strings: {len(r.trans_strings)}")
print(f"Missing EN strings: {len(missing_en)}")
if missing_en:
    for m in missing_en:
        print(f"  EN missing: {repr(m)}")

print(f"Missing AR strings: {len(missing_ar)}")
if missing_ar:
    for m in missing_ar:
        print(f"  AR missing: {repr(m)}")

assert len(missing_en) == 0, "There are still missing EN strings!"
assert len(missing_ar) == 0, "There are still missing AR strings!"

# Update FR mapping
r.FR = {s: s for s in r.trans_strings}

# Generate PO files
for lang, trans in [('fr', r.FR), ('en', r.EN), ('ar', r.AR)]:
    po = r.generate_po(lang, trans, r.trans_strings)
    path = os.path.join(r.LOCALE_DIR, lang, 'LC_MESSAGES', 'django.po')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(po)
    covered = sum(1 for s in r.trans_strings if s in trans)
    print(f"Wrote {lang}.po: {covered}/{len(r.trans_strings)} translated (100%)")

# Compile MO files
print("\nCompiling MO files...")
for lang in ['fr', 'en', 'ar']:
    po_path = os.path.join(r.LOCALE_DIR, lang, 'LC_MESSAGES', 'django.po')
    mo_path = os.path.join(r.LOCALE_DIR, lang, 'LC_MESSAGES', 'django.mo')
    compile_messages.generate_mo(po_path, mo_path)
    print(f"✓ Compiled {lang}/LC_MESSAGES/django.mo")

print("\nSUCCESS: All translations 100% complete and compiled in all 3 languages!")
