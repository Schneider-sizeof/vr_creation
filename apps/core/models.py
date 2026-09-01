"""
Core models for VR Creation Company.
Site settings, team, values, strengths, and process steps.
"""
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class SingletonModel(models.Model):
    """Abstract base model that ensures only one instance exists."""

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass  # Prevent deletion

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class SiteSettings(SingletonModel):
    """Global site configuration — singleton, editable in admin."""
    site_name = models.CharField(
        _('Nom du site'), max_length=200, default='VR Creation Company'
    )
    tagline = models.CharField(
        _('Slogan'), max_length=300, default="L'innovation en action"
    )
    logo = models.ImageField(
        _('Logo'), upload_to='site/', blank=True, null=True
    )
    favicon = models.ImageField(
        _('Favicon'), upload_to='site/', blank=True, null=True
    )
    email = models.EmailField(
        _('Email de contact'), default='contact@vrcreation.com'
    )
    phone = models.CharField(
        _('Téléphone'), max_length=30, blank=True, default='+33 1 23 45 67 89'
    )
    address = models.TextField(
        _('Adresse'), blank=True, default='Paris, France'
    )
    google_analytics_id = models.CharField(
        _('Google Analytics ID'), max_length=30, blank=True,
        help_text=_('Ex: G-XXXXXXXXXX. Chargé uniquement après consentement cookies.')
    )
    google_search_console_id = models.CharField(
        _('Google Search Console'), max_length=100, blank=True,
        help_text=_('Code de vérification Google Search Console (contenu de la balise meta)')
    )
    google_maps_embed_url = models.CharField(
        _('URL Google Maps (embed)'), max_length=500, blank=True,
        help_text=_('URL iframe Google Maps pour la page contact')
    )
    hero_image = models.ImageField(
        _('Image hero accueil'), upload_to='site/', blank=True, null=True,
        help_text=_('Image de fond du hero de la page d\'accueil')
    )
    hero_video = models.FileField(
        _('Vidéo / 3D hero (toutes les pages)'), upload_to='site/hero/',
        blank=True, null=True,
        help_text=_('Vidéo de fond (MP4, WebM) ou fichier 3D affichée derrière les titres de toutes les pages. Recommandé : MP4, max 15 Mo, 1920x1080.')
    )
    hero_video_poster = models.ImageField(
        _('Image poster vidéo hero'), upload_to='site/hero/',
        blank=True, null=True,
        help_text=_('Image affichée pendant le chargement de la vidéo hero (1920x600 recommandé)')
    )
    hero_headline = models.CharField(
        _('Titre hero accueil'), max_length=300, blank=True,
        default="DONNEZ VIE À VOTRE PROJET IMMOBILIER, AVANT MÊME SA CONSTRUCTION.",
        help_text=_('Titre principal affiché sur le hero de la page d\'accueil')
    )
    hero_subheadline = models.TextField(
        _('Sous-titre hero accueil'), blank=True,
        default="De la conception 3D à la commercialisation digitale, nous transformons vos projets immobiliers en expériences visuelles capables de séduire, convaincre et générer des prospects.",
        help_text=_('Texte affiché sous le titre du hero')
    )
    hero_cta1_label = models.CharField(
        _('Bouton hero 1 — libellé'), max_length=100, blank=True,
        default='Découvrir nos solutions'
    )
    hero_cta1_link = models.CharField(
        _('Bouton hero 1 — lien'), max_length=300, blank=True,
        default='#services',
        help_text=_('URL ou ancre (ex: #services, /contact/)')
    )
    hero_cta2_label = models.CharField(
        _('Bouton hero 2 — libellé'), max_length=100, blank=True,
        default='Nous contacter'
    )
    hero_cta2_link = models.CharField(
        _('Bouton hero 2 — lien'), max_length=300, blank=True,
        default='/contact/',
        help_text=_('URL ou ancre (ex: /contact/)')
    )
    about_image = models.ImageField(
        _('Image page À propos'), upload_to='site/', blank=True, null=True
    )
    default_og_image = models.ImageField(
        _('Image OG par défaut'), upload_to='site/', blank=True, null=True,
        help_text=_('Image par défaut pour le partage social (1200x630px recommandé)')
    )
    footer_text = models.TextField(
        _('Texte du pied de page'), blank=True,
        default="Nous allions esthétique et technologie de pointe pour transformer vos projets en expériences visuelles immersives et inoubliables."
    )
    copyright_text = models.CharField(
        _('Texte copyright'), max_length=300, blank=True,
        default='© 2026 VR Creation Company'
    )

    # Social media
    social_facebook = models.URLField(_('Facebook'), blank=True)
    social_instagram = models.URLField(_('Instagram'), blank=True)
    social_linkedin = models.URLField(_('LinkedIn'), blank=True)
    social_youtube = models.URLField(_('YouTube'), blank=True)
    social_twitter = models.URLField(_('Twitter / X'), blank=True)
    social_tiktok = models.URLField(_('TikTok'), blank=True)
    social_behance = models.URLField(_('Behance'), blank=True)
    social_whatsapp = models.CharField(
        _('WhatsApp'), max_length=30, blank=True,
        help_text=_('Numéro WhatsApp au format international (ex: +33612345678)')
    )

    class Meta:
        verbose_name = _('Paramètres du site')
        verbose_name_plural = _('Paramètres du site')

    def __str__(self):
        return self.site_name


class TeamMember(models.Model):
    """Team members displayed on the About page."""
    name = models.CharField(_('Nom'), max_length=200)
    role = models.CharField(_('Rôle'), max_length=200)
    bio = models.TextField(_('Biographie'), blank=True)
    photo = models.ImageField(
        _('Photo'), upload_to='team/', blank=True, null=True
    )
    order = models.PositiveIntegerField(_('Ordre'), default=0)

    class Meta:
        verbose_name = _('Membre de l\'équipe')
        verbose_name_plural = _('Membres de l\'équipe')
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} — {self.role}"


class Value(models.Model):
    """Company values (Créativité, Précision, etc.)."""
    title = models.CharField(_('Titre'), max_length=200)
    description = models.TextField(_('Description'))
    icon = models.CharField(
        _('Icône CSS'), max_length=100, blank=True,
        help_text=_('Classe d\'icône (ex: fas fa-lightbulb) ou emoji')
    )
    order = models.PositiveIntegerField(_('Ordre'), default=0)

    class Meta:
        verbose_name = _('Valeur')
        verbose_name_plural = _('Valeurs')
        ordering = ['order']

    def __str__(self):
        return self.title


class Strength(models.Model):
    """Key figures and strengths for the home page."""
    title = models.CharField(_('Titre'), max_length=200)
    description = models.TextField(_('Description'), blank=True)
    icon = models.CharField(_('Icône CSS'), max_length=100, blank=True)
    stat_number = models.CharField(
        _('Chiffre clé'), max_length=50, blank=True,
        help_text=_('Ex: 150+, 98%, 10 ans')
    )
    stat_label = models.CharField(
        _('Label du chiffre'), max_length=200, blank=True
    )
    background_image = models.ImageField(
        _('Image de fond'), upload_to='strengths/', blank=True, null=True
    )
    order = models.PositiveIntegerField(_('Ordre'), default=0)

    class Meta:
        verbose_name = _('Point fort')
        verbose_name_plural = _('Points forts')
        ordering = ['order']

    def __str__(self):
        return self.title


class ProcessStep(models.Model):
    """Methodology timeline steps."""
    title = models.CharField(_('Titre'), max_length=200)
    description = models.TextField(_('Description'))
    icon = models.CharField(_('Icône CSS'), max_length=100, blank=True)
    order = models.PositiveIntegerField(_('Ordre'), default=0)

    class Meta:
        verbose_name = _('Étape du processus')
        verbose_name_plural = _('Étapes du processus')
        ordering = ['order']

    def __str__(self):
        return f"{self.order}. {self.title}"


class HeroSlide(models.Model):
    """Slides for the homepage hero carousel."""
    title = models.CharField(_('Titre'), max_length=200, blank=True)
    image = models.ImageField(_('Image'), upload_to='hero/')
    order = models.PositiveIntegerField(_('Ordre'), default=0)
    active = models.BooleanField(_('Actif'), default=True)

    class Meta:
        verbose_name = _('Diapositive Hero')
        verbose_name_plural = _('Diapositives Hero')
        ordering = ['order']

    def __str__(self):
        return self.title or f"Slide {self.id}"


class StrategicSuccess(models.Model):
    """Examples of strategic success displayed on the home page."""
    title = models.CharField(_('Titre'), max_length=200)
    importance = models.CharField(
        _('Importance du service'), max_length=300,
        help_text=_('Ex: Les acheteurs veulent se projeter avant d\'investir.')
    )
    image = models.ImageField(
        _('Image'), upload_to='services/', blank=True, null=True,
        help_text=_('Image affichée sur la carte. Stockée dans le dossier media/services/')
    )
    icon = models.CharField(
        _('Icône'), max_length=100, blank=True, default='fas fa-cube',
        help_text=_('Classe d\'icône CSS (ex: fas fa-store)')
    )
    order = models.PositiveIntegerField(_('Ordre'), default=0)
    is_active = models.BooleanField(_('Actif'), default=True)

    class Meta:
        verbose_name = _('Succès stratégique')
        verbose_name_plural = _('Succès stratégiques')
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class Promotion(models.Model):
    """Dynamic promotions/offers page models."""
    title = models.CharField(_('Titre'), max_length=200)
    slug = models.SlugField(_('Slug'), max_length=200, unique=True)
    badge_text = models.CharField(_('Texte du Badge'), max_length=100, default='Offre de Lancement')
    headline = models.CharField(_('Grande phrase d’accroche'), max_length=300)
    sub_headline = models.TextField(_('Sous-titre / Explication courte'))
    featured_image = models.ImageField(_('Image principale'), upload_to='promotions/', blank=True, null=True)
    short_description = models.TextField(
        _('Description courte'), max_length=300,
        help_text=_('Résumé affiché dans la grille des promotions')
    )
    
    # Problem section
    problem_title = models.CharField(_('Titre Problème'), max_length=200, default='LE PROBLÈME QUE VOUS CONNAISSEZ DÉJÀ')
    problem_text = models.TextField(_('Texte introduction Problème'), blank=True)
    
    # Solution section
    solution_title = models.CharField(_('Titre Solution'), max_length=200, default='LA SOLUTION')
    solution_text = models.TextField(_('Texte Solution'), blank=True)
    solution_quote = models.TextField(_('Citation de la Solution'), blank=True)
    
    # CTA section
    cta_title = models.CharField(_('Titre CTA'), max_length=200, default='PRÊT À ACCÉLÉRER VOS VENTES ?')
    cta_text = models.TextField(_('Texte CTA'), blank=True)
    offer_price = models.CharField(_('Tarif / Condition de l\'offre'), max_length=100, default='Sur devis')
    
    is_active = models.BooleanField(_('Actif'), default=True)
    is_featured = models.BooleanField(
        _('Mise en avant'), default=False,
        help_text=_('Cocher pour afficher ce pack en section vedette sur la page d\'accueil et d\'autres pages.')
    )
    is_customizable = models.BooleanField(
        _('Personnalisable'), default=True,
        help_text=_('Si coché, le client peut personnaliser les services inclus. Décocher pour les offres sur commission où VR Creation décide de la stratégie.')
    )
    included_services = models.ManyToManyField(
        'services.Service', blank=True,
        related_name='promotions',
        verbose_name=_('Services inclus'),
        help_text=_('Services inclus dans ce pack. Pour les packs personnalisables, ces services sont pré-cochés.')
    )
    commission_rate = models.CharField(
        _('Taux de commission'), max_length=50, blank=True,
        help_text=_('Ex: 10%, 15%, ou "Sur négociation". Affiché uniquement pour les offres sur commission.')
    )
    video = models.FileField(
        _('Vidéo explicative du pack'), upload_to='promotions/videos/', blank=True, null=True,
        help_text=_('Vidéo MP4 expliquant le pack (max 50 Mo). Affichée sur la page du pack si présente.')
    )
    order = models.PositiveIntegerField(_('Ordre'), default=0)
    created_at = models.DateTimeField(_('Créé le'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Modifié le'), auto_now=True)

    class Meta:
        verbose_name = _('Promotion')
        verbose_name_plural = _('Promotions')
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:promotion_detail', kwargs={'slug': self.slug})


class PromotionDeliverable(models.Model):
    """Deliverable items included in a promotion package."""
    promotion = models.ForeignKey(
        Promotion, on_delete=models.CASCADE, related_name='deliverables',
        verbose_name=_('Promotion')
    )
    title = models.CharField(_('Titre de la prestation'), max_length=200)
    description = models.TextField(_('Description'))
    icon = models.CharField(_('Icône CSS'), max_length=100, default='fas fa-check')
    image = models.ImageField(
        _('Image / Illustration'), upload_to='promotions/deliverables/', blank=True, null=True,
        help_text=_('Image optionnelle affichée sur la carte de cette prestation (400x300px recommandé)')
    )
    order = models.PositiveIntegerField(_('Ordre'), default=0)

    class Meta:
        verbose_name = _('Prestation incluse')
        verbose_name_plural = _('Prestations incluses')
        ordering = ['order']

    def __str__(self):
        return self.title


class PromotionComparison(models.Model):
    """Comparison table items for a promotion."""
    promotion = models.ForeignKey(
        Promotion, on_delete=models.CASCADE, related_name='comparisons',
        verbose_name=_('Promotion')
    )
    feature = models.CharField(_('Fonctionnalité / Critère'), max_length=200)
    without_vr = models.CharField(_('Sans VR Creation'), max_length=200)
    with_vr = models.CharField(_('Avec VR Creation'), max_length=200)
    order = models.PositiveIntegerField(_('Ordre'), default=0)

    class Meta:
        verbose_name = _('Point de comparaison')
        verbose_name_plural = _('Points de comparaison')
        ordering = ['order']

    def __str__(self):
        return self.feature


class PromotionStep(models.Model):
    """Workflow steps for a promotion."""
    promotion = models.ForeignKey(
        Promotion, on_delete=models.CASCADE, related_name='steps',
        verbose_name=_('Promotion')
    )
    title = models.CharField(_('Titre de l’étape'), max_length=200)
    description = models.TextField(_('Description'))
    order = models.PositiveIntegerField(_('Ordre'), default=0)

    class Meta:
        verbose_name = _('Étape de l’offre')
        verbose_name_plural = _('Étapes de l’offre')
        ordering = ['order']

    def __str__(self):
        return f"{self.order}. {self.title}"

