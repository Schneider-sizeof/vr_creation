import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
import django
django.setup()

from apps.services.models import City

def tokenize(text):
    if not text:
        return set()
    # Simple word tokenization lowercase
    import re
    words = re.findall(r'\b\w+\b', text.lower(), re.UNICODE)
    # Filter short stop-like words (len <= 2)
    return set(w for w in words if len(w) > 2)

def jaccard_similarity(set1, set2):
    if not set1 or not set2:
        return 0.0
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return (intersection / union) * 100.0 if union > 0 else 0.0

cities = list(City.objects.all().order_by('order'))
print(f"Loaded {len(cities)} cities.\n")

langs = [('fr', 'French'), ('en', 'English'), ('ar', 'Arabic')]

for lang_code, lang_name in langs:
    print(f"=== Checking {lang_name} ({lang_code}) ===")
    city_texts = {}
    for c in cities:
        intro = getattr(c, f'intro_text_{lang_code}') or ''
        market = getattr(c, f'market_description_{lang_code}') or ''
        landmarks = getattr(c, f'landmarks_{lang_code}') or ''
        combined = f"{intro} {market} {landmarks}"
        city_texts[c.name] = combined
        word_count = len(combined.split())
        print(f"  {c.name}: {word_count} words")

    max_sim = 0.0
    highest_pair = None
    all_below_25 = True

    pairs_checked = 0
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            c1 = cities[i]
            c2 = cities[j]
            t1 = city_texts[c1.name]
            t2 = city_texts[c2.name]
            tok1 = tokenize(t1)
            tok2 = tokenize(t2)
            sim = jaccard_similarity(tok1, tok2)
            pairs_checked += 1
            if sim > max_sim:
                max_sim = sim
                highest_pair = (c1.name, c2.name, sim)
            if sim >= 25.0:
                print(f"  [WARNING] High similarity between {c1.name} and {c2.name}: {sim:.2f}%")
                all_below_25 = False

    print(f"  Checked {pairs_checked} pairs.")
    print(f"  Highest similarity pair: {highest_pair[0]} & {highest_pair[1]} at {highest_pair[2]:.2f}%")
    if all_below_25:
        print(f"  ✓ PASSED: All pairwise Jaccard similarities strictly < 25% for {lang_name}!\n")
    else:
        print(f"  ✗ FAILED: Some pairs exceeded 25% for {lang_name}!\n")
