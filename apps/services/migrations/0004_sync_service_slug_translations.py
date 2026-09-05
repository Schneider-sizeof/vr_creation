from django.db import migrations


def sync_service_slugs(apps, schema_editor):
    Service = apps.get_model('services', 'Service')
    for svc in Service.objects.all():
        changed = False
        if not getattr(svc, 'slug_fr', None):
            svc.slug_fr = svc.slug
            changed = True
        if not getattr(svc, 'slug_en', None):
            svc.slug_en = svc.slug_fr or svc.slug
            changed = True
        if not getattr(svc, 'slug_ar', None):
            svc.slug_ar = svc.slug_fr or svc.slug
            changed = True
        if changed:
            svc.save(update_fields=['slug_fr', 'slug_en', 'slug_ar'])


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_update_service_icons'),
    ]

    operations = [
        migrations.RunPython(sync_service_slugs, reverse_func),
    ]
