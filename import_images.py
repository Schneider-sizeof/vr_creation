import os
import sys
import shutil
from pathlib import Path
import django

# Load .env file
try:
    from dotenv import load_dotenv
    env_path = Path(__file__).resolve().parent / '.env'
    if env_path.exists():
        load_dotenv(env_path)
except ImportError:
    pass

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
django.setup()

from django.conf import settings
from apps.services.models import Service, ServiceImage
from apps.portfolio.models import Project, ProjectImage, CaseStudy

# Source paths
nouveau_dossier = os.path.join(Path(__file__).resolve().parent, "Nouveau dossier")
captures_dir = os.path.join(nouveau_dossier, "2 PAGES CAPTURES 360", "2 PAGES CAPTURES 360", "PHOTOS")
visites_dir = os.path.join(nouveau_dossier, "2 PAGES VISITES VIRTUELLES", "2 PAGES VISITES VIRTUELLES", "PHOTOS")
rendus_dir = os.path.join(nouveau_dossier, "RENDUS 3D CATALOGUE VR", "RENDUS 3D CATALOGUE VR")

# Destination paths under media/
media_root = settings.MEDIA_ROOT
portfolio_dest = os.path.join(media_root, "portfolio")
portfolio_gallery_dest = os.path.join(media_root, "portfolio", "gallery")
services_dest = os.path.join(media_root, "services")
services_gallery_dest = os.path.join(media_root, "services", "gallery")
case_studies_dest = os.path.join(media_root, "case_studies")

# Create directories
for d in [portfolio_dest, portfolio_gallery_dest, services_dest, services_gallery_dest, case_studies_dest]:
    os.makedirs(d, exist_ok=True)

def copy_file(src, dst):
    try:
        shutil.copy2(src, dst)
        print(f"Copied {os.path.basename(src)} -> {dst}")
        return True
    except Exception as e:
        print(f"Error copying {src}: {e}")
        return False

print("\n--- 1. Processing 3D Renderings (RENDUS 3D CATALOGUE VR) ---")
copy_file(os.path.join(rendus_dir, "VILLA.png"), os.path.join(portfolio_dest, "villa.png"))
copy_file(os.path.join(rendus_dir, "VILLA.png"), os.path.join(case_studies_dest, "villa.png"))
copy_file(os.path.join(rendus_dir, "PROJET IMMOBILIER.png"), os.path.join(portfolio_dest, "projet-immobilier.png"))
copy_file(os.path.join(rendus_dir, "PROJET IMMOBILIER.png"), os.path.join(case_studies_dest, "projet-immobilier.png"))
copy_file(os.path.join(rendus_dir, "STORE SHOWROOM.png"), os.path.join(portfolio_dest, "store-showroom.png"))
copy_file(os.path.join(rendus_dir, "STORE SHOWROOM.png"), os.path.join(case_studies_dest, "store-showroom.png"))
copy_file(os.path.join(rendus_dir, "ESPACE BUREAU .png"), os.path.join(services_dest, "espace-bureau.png"))
copy_file(os.path.join(rendus_dir, "STAND EVENEMENTIEL.png"), os.path.join(services_dest, "stand-evenementiel.png"))

# Update Projects
try:
    p_villa = Project.objects.get(slug='villa-mediterranee')
    p_villa.featured_image = "portfolio/villa.png"
    p_villa.save()
    print("Updated Project: villa-mediterranee")
    p_villa.gallery_images.all().delete()
    ProjectImage.objects.create(project=p_villa, image="portfolio/villa.png", alt_text="Villa Méditerranée - Rendu 3D extérieur", order=1)
except Project.DoesNotExist:
    print("Project 'villa-mediterranee' not found")

try:
    p_azure = Project.objects.get(slug='residence-azure')
    p_azure.featured_image = "portfolio/projet-immobilier.png"
    p_azure.save()
    print("Updated Project: residence-azure")
    p_azure.gallery_images.all().delete()
    ProjectImage.objects.create(project=p_azure, image="portfolio/projet-immobilier.png", alt_text="Résidence Azure - Rendu 3D immeuble moderne", order=1)
except Project.DoesNotExist:
    print("Project 'residence-azure' not found")

try:
    p_lumiere = Project.objects.get(slug='concept-store-lumiere')
    p_lumiere.featured_image = "portfolio/store-showroom.png"
    p_lumiere.save()
    print("Updated Project: concept-store-lumiere")
    p_lumiere.gallery_images.all().delete()
    ProjectImage.objects.create(project=p_lumiere, image="portfolio/store-showroom.png", alt_text="Concept Store Lumière - Design intérieur & Showroom", order=1)
except Project.DoesNotExist:
    print("Project 'concept-store-lumiere' not found")

# Update Case Studies (Using correct slugs)
try:
    cs_villa = CaseStudy.objects.get(slug='couverture-immersive-salon')
    cs_villa.featured_image = "case_studies/villa.png"
    cs_villa.save()
    print("Updated CaseStudy: couverture-immersive-salon (Villa)")
except CaseStudy.DoesNotExist:
    print("CaseStudy 'couverture-immersive-salon' not found")

try:
    cs_azure = CaseStudy.objects.get(slug='acceleration-ventes-programme-neuf')
    cs_azure.featured_image = "case_studies/projet-immobilier.png"
    cs_azure.save()
    print("Updated CaseStudy: acceleration-ventes-programme-neuf (Azure)")
except CaseStudy.DoesNotExist:
    print("CaseStudy 'acceleration-ventes-programme-neuf' not found")

try:
    cs_lumiere = CaseStudy.objects.get(slug='transformation-digitale-concept-store')
    cs_lumiere.featured_image = "case_studies/store-showroom.png"
    cs_lumiere.save()
    print("Updated CaseStudy: transformation-digitale-concept-store (Lumière)")
except CaseStudy.DoesNotExist:
    print("CaseStudy 'transformation-digitale-concept-store' not found")

# Update Service: Conception & Modélisation 3D (modelisation-3d)
try:
    s_3d = Service.objects.get(slug='modelisation-3d')
    s_3d.featured_image = "services/espace-bureau.png"
    s_3d.save()
    print("Updated Service: modelisation-3d")
    s_3d.gallery_images.all().delete()
    ServiceImage.objects.create(service=s_3d, image="services/espace-bureau.png", alt_text="Modélisation 3D d'Espaces Bureaux Professionnels", order=1)
    ServiceImage.objects.create(service=s_3d, image="portfolio/villa.png", alt_text="Rendu 3D Villa Individuelle Haut de Gamme", order=2)
    ServiceImage.objects.create(service=s_3d, image="portfolio/projet-immobilier.png", alt_text="Visualisation 3D Promotion Immobilière / Résidence", order=3)
    ServiceImage.objects.create(service=s_3d, image="portfolio/store-showroom.png", alt_text="Design 3D Store & Showroom Retail", order=4)
    ServiceImage.objects.create(service=s_3d, image="services/stand-evenementiel.png", alt_text="Conception 3D Stand Événementiel & Salon", order=5)
    print("Seeded gallery for modelisation-3d")
except Service.DoesNotExist:
    print("Service 'modelisation-3d' not found")


print("\n--- 2. Processing Virtual Tours (2 PAGES VISITES VIRTUELLES) ---")
if os.path.exists(visites_dir):
    visites_photos = sorted([f for f in os.listdir(visites_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
    try:
        s_visites = Service.objects.get(slug='visites-virtuelles')
        
        if visites_photos:
            featured_src = os.path.join(visites_dir, visites_photos[0])
            copy_file(featured_src, os.path.join(services_dest, "visites-virtuelles-featured.png"))
            s_visites.featured_image = "services/visites-virtuelles-featured.png"
            s_visites.save()
            print("Updated Service: visites-virtuelles featured image")
        
        s_visites.gallery_images.all().delete()
        
        alts = [
            "Visite virtuelle interactive - Salon & Séjour",
            "Projection dans l'espace & circulation fluide",
            "Test d'aménagement intérieur & mobilier",
            "Simulation de luminosité & perspectives réelles",
            "Visualisation immersive chambre & suite parentale",
            "Parcours client immersif & interactif 360°"
        ]
        
        for idx, filename in enumerate(visites_photos):
            src_path = os.path.join(visites_dir, filename)
            dest_filename = f"visites-virtuelles-{idx+1}.png"
            dest_path = os.path.join(services_gallery_dest, dest_filename)
            copy_file(src_path, dest_path)
            
            alt_text = alts[idx] if idx < len(alts) else f"Visite virtuelle interactive {idx+1}"
            ServiceImage.objects.create(
                service=s_visites,
                image=f"services/gallery/{dest_filename}",
                alt_text=alt_text,
                order=idx+1
            )
        print("Updated Service: visites-virtuelles gallery images")
    except Service.DoesNotExist:
        print("Service 'visites-virtuelles' not found")
else:
    print(f"Directory {visites_dir} does not exist")


print("\n--- 3. Processing 360 Captures (2 PAGES CAPTURES 360) ---")
if os.path.exists(captures_dir):
    captures_photos = sorted([f for f in os.listdir(captures_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
    try:
        s_captures = Service.objects.get(slug='captures-360')
        
        if captures_photos:
            featured_src = os.path.join(captures_dir, captures_photos[0])
            copy_file(featured_src, os.path.join(services_dest, "captures-360-featured.png"))
            s_captures.featured_image = "services/captures-360-featured.png"
            s_captures.save()
            print("Updated Service: captures-360 featured image")
        
        s_captures.gallery_images.all().delete()
        
        alts_360 = [
            "Capture 360° réelle - Espace de réception & Bureau",
            "Showroom d'exposition interactif de luxe",
            "Espace commercial & retail connecté",
            "Visite virtuelle de bureaux d'entreprise",
            "Immersion complète en agence immobilière",
            "Parcours magasin interactif pour e-commerce",
            "Numérisation 3D d'espace professionnel",
            "Captation 360° événementielle & salon d'exposition"
        ]
        
        for idx, filename in enumerate(captures_photos):
            src_path = os.path.join(captures_dir, filename)
            dest_filename = f"captures-360-{idx+1}.png"
            dest_path = os.path.join(services_gallery_dest, dest_filename)
            copy_file(src_path, dest_path)
            
            alt_text = alts_360[idx] if idx < len(alts_360) else f"Capture 360° réelle {idx+1}"
            ServiceImage.objects.create(
                service=s_captures,
                image=f"services/gallery/{dest_filename}",
                alt_text=alt_text,
                order=idx+1
            )
        print("Updated Service: captures-360 gallery images")
    except Service.DoesNotExist:
        print("Service 'captures-360' not found")
else:
    print(f"Directory {captures_dir} does not exist")

print("\n[OK] All client images imported and database updated successfully!")
