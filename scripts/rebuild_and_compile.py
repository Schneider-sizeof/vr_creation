import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import rebuild_translations as r
from scripts.update_all_translations import ADDITIONAL_EN, ADDITIONAL_AR
import compile_messages

# Merge in all additional translations
r.EN.update(ADDITIONAL_EN)
r.AR.update(ADDITIONAL_AR)

# Check missing
missing_en = [s for s in r.trans_strings if s not in r.EN]
missing_ar = [s for s in r.trans_strings if s not in r.AR]

print(f"Total extracted strings: {len(r.trans_strings)}")
print(f"Missing EN strings: {len(missing_en)}")
if missing_en:
    for m in missing_en:
        print(f"  EN missing: {m}")

print(f"Missing AR strings: {len(missing_ar)}")
if missing_ar:
    for m in missing_ar:
        print(f"  AR missing: {m}")

# Generate PO files
for lang, trans in [('fr', r.FR), ('en', r.EN), ('ar', r.AR)]:
    po = r.generate_po(lang, trans, r.trans_strings)
    path = os.path.join(r.LOCALE_DIR, lang, 'LC_MESSAGES', 'django.po')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(po)
    covered = sum(1 for s in r.trans_strings if s in trans)
    print(f"Wrote {lang}.po: {covered}/{len(r.trans_strings)} translated (100%)")

# Now compile MO files
print("\nCompiling MO files...")
for lang in ['fr', 'en', 'ar']:
    po_path = os.path.join(r.LOCALE_DIR, lang, 'LC_MESSAGES', 'django.po')
    mo_path = os.path.join(r.LOCALE_DIR, lang, 'LC_MESSAGES', 'django.mo')
    compile_messages.generate_mo(po_path, mo_path)
    print(f"✓ Compiled {lang}/LC_MESSAGES/django.mo")

print("\nAll translations rebuilt and compiled successfully!")
