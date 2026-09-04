from django.db import migrations


def update_service_icons(apps, schema_editor):
    Service = apps.get_model('services', 'Service')
    slug_map = {
        'modelisation-3d': 'fas fa-cube',
        'conception-modelisation-3d': 'fas fa-cube',
        'visites-virtuelles': 'fas fa-vr-cardboard',
        'visites-virtuelles-interactives': 'fas fa-vr-cardboard',
        'captures-360': 'fas fa-camera-retro',
        'captures-360-reelles': 'fas fa-camera-retro',
        'branding-visuel': 'fas fa-palette',
        'branding-communication-visuelle': 'fas fa-palette',
        'site-web-digital': 'fas fa-laptop-code',
        'site-web-experience-digitale': 'fas fa-laptop-code',
        'lead-generation': 'fas fa-bullseye',
        'lead-generation-suivi': 'fas fa-bullseye',
        'photographie': 'fas fa-camera',
        'photographie-professionnelle': 'fas fa-camera',
        'animation-motion-design': 'fas fa-film',
    }
    emoji_map = {
        '🏗️': 'fas fa-cube',
        '🏗': 'fas fa-cube',
        '🥽': 'fas fa-vr-cardboard',
        '📸': 'fas fa-camera-retro',
        '📷': 'fas fa-camera',
        '🎨': 'fas fa-palette',
        '💻': 'fas fa-laptop-code',
        '🎯': 'fas fa-bullseye',
        '🎬': 'fas fa-film',
        '📊': 'fas fa-chart-line',
        '🚀': 'fas fa-rocket',
    }

    for svc in Service.objects.all():
        raw = (svc.icon or '').strip()
        new_icon = None
        
        if svc.slug in slug_map:
            new_icon = slug_map[svc.slug]
        elif raw in emoji_map:
            new_icon = emoji_map[raw]
        elif not raw or not ('fa-' in raw):
            new_icon = 'fas fa-cube'

        if new_icon and svc.icon != new_icon:
            svc.icon = new_icon
            svc.save(update_fields=['icon'])


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_service_meta_description_service_meta_description_ar_and_more'),
    ]

    operations = [
        migrations.RunPython(update_service_icons, reverse_func),
    ]
