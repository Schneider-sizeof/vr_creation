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
        call_command('seed_seo')

        # 2. Update Services
        self.stdout.write("2. Updating Services (lead-generation, differentiation & titles)...")
        # Lead Generation (Unblock 404)
        lead, _ = Service.objects.get_or_create(slug='lead-generation')
        lead.is_active = True
        lead.title = "Marketing digital & lead generation"
        lead.title_fr = "Marketing digital & lead generation"
        lead.title_en = "Digital Marketing & Lead Generation"
        lead.title_ar = "التسويق الرقمي وجلب العملاء"
        lead.short_description = "Campagnes publicitaires ciblées, tunnels de conversion et qualification des prospects pour maximiser vos ventes immobilières à Tanger."
        lead.short_description_fr = "Campagnes publicitaires ciblées, tunnels de conversion et qualification des prospects pour maximiser vos ventes immobilières à Tanger."
        lead.short_description_en = "Targeted ad campaigns, conversion funnels and prospect qualification to maximize your real estate sales in Tangier."
        lead.short_description_ar = "حملات إعلانية مستهدفة ومسارات تحويل وتأهيل العملاء المحتملين لزيادة مبيعاتكم العقارية في طنجة."
        lead.full_description = """<p class="mb-4">VR Creation accompagne les promoteurs immobiliers et entreprises dans la mise en place de dispositifs d'acquisition de leads hautement qualifiés. Grâce à une synergie entre nos visuels 3D d'exception et des stratégies média ciblées, nous transformons l'intérêt des visiteurs en rendez-vous commerciaux concrets.</p>
<h3 class="text-xl font-bold text-dark mt-6 mb-3">Ce que comprend ce service :</h3>
<ul class="list-disc list-inside space-y-2 mb-6 text-gray-600">
    <li><strong>Création de landing pages immersives :</strong> Pages de conversion optimisées intégrant visuels 3D, visites virtuelles et formulaires interactifs.</li>
    <li><strong>Campagnes publicitaires ciblées :</strong> Diffusion sponsorisée sur Meta (Instagram, Facebook), Google Ads et LinkedIn ciblant les acheteurs nationaux et MRE.</li>
    <li><strong>Qualification et suivi des prospects :</strong> Filtrage en amont des demandes et synchronisation directe avec votre équipe commerciale ou votre CRM.</li>
    <li><strong>Reporting et optimisation continue :</strong> Tableaux de bord en temps réel pour mesurer le coût par lead et maximiser le retour sur investissement.</li>
</ul>"""
        lead.full_description_fr = lead.full_description
        lead.meta_title = "Marketing digital & lead generation Tanger | VR Creation"
        lead.meta_title_fr = "Marketing digital & lead generation Tanger | VR Creation"
        lead.meta_description = "Génération de prospects qualifiés et campagnes digitales ciblées pour accélérer les ventes de vos programmes immobiliers à Tanger."
        lead.meta_description_fr = "Génération de prospects qualifiés et campagnes digitales ciblées pour accélérer les ventes de vos programmes immobiliers à Tanger."
        lead.icon = "fas fa-bullseye"
        lead.save()
        self.stdout.write(self.style.SUCCESS("  + Activated & updated lead-generation"))

        # Modélisation 3D
        try:
            s3d = Service.objects.get(slug='modelisation-3d')
            s3d.title = "Modélisation 3D & rendu architectural"
            s3d.title_fr = "Modélisation 3D & rendu architectural"
            s3d.meta_title = "Modélisation 3D & rendu architectural Tanger | VR Creation"
            s3d.meta_title_fr = "Modélisation 3D & rendu architectural Tanger | VR Creation"
            s3d.meta_description = "Rendus 3D photoréalistes pour l'architecture et l'immobilier à Tanger et dans le Nord du Maroc. Perspectives intérieures et extérieures de prestige."
            s3d.meta_description_fr = "Rendus 3D photoréalistes pour l'architecture et l'immobilier à Tanger et dans le Nord du Maroc. Perspectives intérieures et extérieures de prestige."
            s3d.save()
            self.stdout.write(self.style.SUCCESS("  ~ Updated modelisation-3d"))
        except Service.DoesNotExist:
            pass

        # Visites virtuelles (3D architectural unbuilt)
        try:
            vv = Service.objects.get(slug='visites-virtuelles')
            vv.title = "Visite virtuelle 3D & maquette orbitale"
            vv.title_fr = "Visite virtuelle 3D & maquette orbitale"
            vv.short_description = "Visites virtuelles 3D immersives et interactives pour projets immobiliers sur plan (VEFA), maquettes 3D orbitales et configurateurs d'espaces."
            vv.short_description_fr = "Visites virtuelles 3D immersives et interactives pour projets immobiliers sur plan (VEFA), maquettes 3D orbitales et configurateurs d'espaces."
            vv.meta_title = "Visite virtuelle 360° à Tanger | VR Creation"
            vv.meta_title_fr = "Visite virtuelle 360° à Tanger | VR Creation"
            vv.meta_description = "Visites virtuelles 3D immersives et maquettes orbitales interactives pour la vente de biens immobiliers sur plan à Tanger et au Maroc."
            vv.meta_description_fr = "Visites virtuelles 3D immersives et maquettes orbitales interactives pour la vente de biens immobiliers sur plan à Tanger et au Maroc."
            vv.save()
            self.stdout.write(self.style.SUCCESS("  ~ Updated visites-virtuelles"))
        except Service.DoesNotExist:
            pass

        # Captures 360 (Real built spaces)
        try:
            c360 = Service.objects.get(slug='captures-360')
            c360.title = "Capture 360° d'espaces réels"
            c360.title_fr = "Capture 360° d'espaces réels"
            c360.short_description = "Numérisation 360° et visites virtuelles d'espaces construits réels : showrooms, boutiques, hôtels, villas et suivi photographique de chantiers à Tanger."
            c360.short_description_fr = "Numérisation 360° et visites virtuelles d'espaces construits réels : showrooms, boutiques, hôtels, villas et suivi photographique de chantiers à Tanger."
            c360.meta_title = "Capture 360° & scan d'espace à Tanger | VR Creation"
            c360.meta_title_fr = "Capture 360° & scan d'espace à Tanger | VR Creation"
            c360.meta_description = "Captures 360° haute résolution et scans immersifs pour valoriser vos espaces réels, commerces et établissements touristiques à Tanger."
            c360.meta_description_fr = "Captures 360° haute résolution et scans immersifs pour valoriser vos espaces réels, commerces et établissements touristiques à Tanger."
            c360.save()
            self.stdout.write(self.style.SUCCESS("  ~ Updated captures-360"))
        except Service.DoesNotExist:
            pass

        # Branding visuel
        try:
            bv = Service.objects.get(slug='branding-visuel')
            bv.title = "Branding & communication visuelle"
            bv.title_fr = "Branding & communication visuelle"
            bv.meta_title = "Branding & communication visuelle à Tanger | VR Creation"
            bv.meta_title_fr = "Branding & communication visuelle à Tanger | VR Creation"
            bv.meta_description = "Création d'identités visuelles percutantes, chartes graphiques, brochures et supports de vente pour marques et promoteurs immobiliers à Tanger."
            bv.meta_description_fr = "Création d'identités visuelles percutantes, chartes graphiques, brochures et supports de vente pour marques et promoteurs immobiliers à Tanger."
            bv.save()
            self.stdout.write(self.style.SUCCESS("  ~ Updated branding-visuel"))
        except Service.DoesNotExist:
            pass

        # Photographie
        try:
            photo = Service.objects.get(slug='photographie')
            photo.title = "Photographie professionnelle & drone"
            photo.title_fr = "Photographie professionnelle & drone"
            photo.meta_title = "Photographie professionnelle & drone à Tanger | VR Creation"
            photo.meta_title_fr = "Photographie professionnelle & drone à Tanger | VR Creation"
            photo.meta_description = "Reportages photographiques d'architecture intérieure et prises de vues aériennes par drone certifié pour l'immobilier et l'hôtellerie à Tanger."
            photo.meta_description_fr = "Reportages photographiques d'architecture intérieure et prises de vues aériennes par drone certifié pour l'immobilier et l'hôtellerie à Tanger."
            photo.save()
            self.stdout.write(self.style.SUCCESS("  ~ Updated photographie"))
        except Service.DoesNotExist:
            pass

        # Animation motion design
        try:
            anim = Service.objects.get(slug='animation-motion-design')
            anim.title = "Animation 3D & motion design"
            anim.title_fr = "Animation 3D & motion design"
            anim.meta_title = "Animation 3D & motion design à Tanger | VR Creation"
            anim.meta_title_fr = "Animation 3D & motion design à Tanger | VR Creation"
            anim.meta_description = "Films d'animation 3D cinématographiques, teasers vidéo et habillages motion design pour valoriser vos projets immobiliers et publicitaires à Tanger."
            anim.meta_description_fr = "Films d'animation 3D cinématographiques, teasers vidéo et habillages motion design pour valoriser vos projets immobiliers et publicitaires à Tanger."
            anim.save()
            self.stdout.write(self.style.SUCCESS("  ~ Updated animation-motion-design"))
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
            settings_obj.save()
            self.stdout.write(self.style.SUCCESS("  ~ Updated SiteSettings headline & CTA link"))

        self.stdout.write(self.style.SUCCESS("\n[SUCCESS] All SEO audit synchronization steps completed!"))
