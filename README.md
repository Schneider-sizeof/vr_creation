# VR Creation Company — Site Web Django

> **L'innovation en action** — Agence spécialisée en création visuelle 3D, visites virtuelles et captures 360°.

Site web professionnel multilingue (FR/EN/AR avec support RTL), SEO-optimisé, RGPD-compliant, prêt pour le déploiement en production.

---

## Stack technique

| Composant | Technologie |
|-----------|-------------|
| Backend | Django 5.1+ / Python 3.12+ |
| Base de données | SQLite (fichier local) |
| Frontend | Django Templates + Tailwind CSS (CDN) + JS vanilla |
| Fichiers statiques | WhiteNoise |
| Serveur WSGI | Gunicorn |
| Multilingue | django-modeltranslation + i18n_patterns |
| Images | Pillow |
| Compression | django-compressor |

---

## Installation locale (développement)

### 1. Prérequis

- Python 3.12+
- pip

### 2. Cloner le projet

```bash
git clone <url-du-repo> vr_creation
cd vr_creation
```

### 3. Environnement virtuel

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 4. Installation des dépendances

```bash
pip install -r requirements.txt
```

### 5. Configuration de l'environnement

```bash
cp .env.example .env
# Éditez .env selon vos besoins (les valeurs par défaut fonctionnent en dev)
```

### 6. Base de données

```bash
python manage.py migrate
```

### 7. Charger les données de démonstration

```bash
python manage.py load_demo_data
```

### 8. Créer un superutilisateur

```bash
python manage.py createsuperuser
```

### 9. Lancer le serveur de développement

```bash
python manage.py runserver
```

Le site est accessible sur **http://localhost:8000/fr/**

L'administration est accessible sur **http://localhost:8000/fr/admin/**

---

## Structure du projet

```
vr_creation/
├── config/                 # Configuration Django
│   └── settings/           # base.py / dev.py / prod.py
├── apps/
│   ├── core/               # Accueil, À propos, pages légales
│   ├── services/           # Services (6 types)
│   ├── portfolio/          # Projets, études de cas, visites 360°
│   ├── blog/               # Articles & catégories
│   ├── contact/            # Formulaire de contact
│   └── seo/                # SEO meta, JSON-LD, sitemap, robots
├── templates/              # Templates Django
├── static/                 # CSS, JS, images statiques
├── locale/                 # Fichiers de traduction .po/.mo
├── media/                  # Uploads utilisateur (gitignored)
├── data/                   # Base SQLite (gitignored)
└── manage.py
```

---

## Multilingue

Le site supporte 3 langues :
- 🇫🇷 **Français** (défaut) — `/fr/`
- 🇬🇧 **English** — `/en/`
- 🇸🇦 **العربية** (RTL) — `/ar/`

Les contenus dynamiques sont traduits via l'admin Django (onglets par langue).

Les textes statiques utilisent `{% trans %}` et les fichiers `.po` dans `locale/`.

### Compiler les traductions

```bash
python manage.py compilemessages
```

---

## Administration

Accessible à `/fr/admin/`. Le client peut gérer :

- **Paramètres du site** : nom, logo, coordonnées, réseaux sociaux
- **Services** : titre, description, galerie, icône (6 services)
- **Projets portfolio** : détails, galerie, visite virtuelle 360°
- **Études de cas** : format problème/importance/résultat/efficacité
- **Articles de blog** : avec catégories
- **Messages de contact** : lecture des soumissions du formulaire
- **SEO** : meta title/description par page et par objet

Tout est traduisible dans les 3 langues directement depuis l'admin.

---

## Déploiement en production

### 1. Configuration serveur

```bash
# Sur votre VPS / serveur
pip install -r requirements.txt

# Copier et configurer l'environnement
cp .env.example .env
# Modifier .env :
#   DJANGO_SETTINGS_MODULE=config.settings.prod
#   DJANGO_SECRET_KEY=<clé-secrète-longue>
#   DJANGO_DEBUG=False
#   DJANGO_ALLOWED_HOSTS=votre-domaine.com,www.votre-domaine.com
#   SITE_DOMAIN=votre-domaine.com
#   SITE_PROTOCOL=https
```

### 2. Migrations et fichiers statiques

```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py compilemessages
python manage.py load_demo_data  # Optionnel
python manage.py createsuperuser
```

### 3. Lancer avec Gunicorn

```bash
gunicorn config.wsgi:application -c gunicorn.conf.py
```

### 4. Reverse proxy (optionnel, recommandé)

Nginx en reverse proxy devant Gunicorn :

```nginx
server {
    listen 80;
    server_name votre-domaine.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name votre-domaine.com;

    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    location /media/ {
        alias /path/to/vr_creation/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

> **Note** : Sans Nginx, WhiteNoise sert les fichiers statiques directement. Nginx n'est requis que pour servir les fichiers media et offrir des performances optimales.

---

## Sauvegarde de la base de données

La base SQLite est stockée dans `data/db.sqlite3`. Pour sauvegarder :

```bash
# Copie manuelle
cp data/db.sqlite3 data/db.sqlite3.backup.$(date +%Y%m%d)

# Script cron recommandé (quotidien)
0 3 * * * cp /path/to/vr_creation/data/db.sqlite3 /path/to/backups/db.sqlite3.$(date +\%Y\%m\%d)
```

⚠️ **Important** : SQLite n'a pas de réplication. Effectuez des copies régulières, idéalement quotidiennes, vers un stockage externe.

---

## Variables d'environnement

| Variable | Description | Défaut |
|----------|-------------|--------|
| `DJANGO_SECRET_KEY` | Clé secrète Django | clé dev (à changer !) |
| `DJANGO_DEBUG` | Mode debug | `True` |
| `DJANGO_ALLOWED_HOSTS` | Hosts autorisés (séparés par ,) | `*` |
| `DJANGO_SETTINGS_MODULE` | Module settings | `config.settings.dev` |
| `SITE_DOMAIN` | Domaine du site | `vrcreation.com` |
| `SITE_PROTOCOL` | Protocole (http/https) | `https` |
| `DATABASE_PATH` | Chemin vers le fichier SQLite | `data/db.sqlite3` |
| `EMAIL_HOST` | Serveur SMTP | `smtp.gmail.com` |
| `EMAIL_PORT` | Port SMTP | `587` |
| `EMAIL_HOST_USER` | Utilisateur SMTP | _(vide)_ |
| `EMAIL_HOST_PASSWORD` | Mot de passe SMTP | _(vide)_ |
| `CONTACT_EMAIL` | Email destinataire du formulaire | `contact@vrcreation.com` |

---

## Checklist SEO

- [x] `<title>` et `<meta description>` uniques par page
- [x] Open Graph complet (`og:title`, `og:description`, `og:image`, `og:locale`)
- [x] Twitter Cards (`summary_large_image`)
- [x] JSON-LD : `Organization`, `LocalBusiness`, `BreadcrumbList`, `Service`, `Article`
- [x] `sitemap.xml` dynamique (toutes les URLs)
- [x] `robots.txt` dynamique
- [x] `<link rel="canonical">` sur chaque page
- [x] `hreflang` pour FR/EN/AR + `x-default`
- [x] HTML sémantique (`<header>`, `<main>`, `<nav>`, `<article>`, `<footer>`)
- [x] H1 unique par page
- [x] `loading="lazy"` sur les images
- [x] Attributs `alt` descriptifs sur toutes les images
- [x] `aria-label` sur les éléments interactifs
- [x] Responsive mobile-first
- [x] WhiteNoise compression (Gzip/Brotli)
- [x] Cache Django (file-based)
- [x] Polices Google préconnectées (`preconnect`)

---

## Licence

© 2026 VR Creation Company. Tous droits réservés.
