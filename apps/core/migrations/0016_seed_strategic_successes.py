from django.db import migrations


def seed_strategic_successes(apps, schema_editor):
    StrategicSuccess = apps.get_model('core', 'StrategicSuccess')

    STRATEGIC_DATA = [
        {
            'title': 'Projet immobilier',
            'title_fr': 'Projet immobilier',
            'title_en': 'Real estate project',
            'title_ar': 'مشروع عقاري',
            'importance': "Les acheteurs veulent se projeter avant d'investir.",
            'importance_fr': "Les acheteurs veulent se projeter avant d'investir.",
            'importance_en': 'Buyers want to envision before investing.',
            'importance_ar': 'يريد المشترون التصور قبل الاستثمار.',
            'icon': 'fas fa-building',
            'order': 1,
            'image': 'services/projet-immobilier.jpg',
        },
        {
            'title': 'Villa en construction',
            'title_fr': 'Villa en construction',
            'title_en': 'Villa under construction',
            'title_ar': 'فيلا قيد الإنشاء',
            'importance': "Le client veut visualiser le résultat final pour s'engager.",
            'importance_fr': "Le client veut visualiser le résultat final pour s'engager.",
            'importance_en': 'The client wants to visualize the final result before committing.',
            'importance_ar': 'يرغب العميل في معاينة النتيجة النهائية بكل ثقة قبل الالتزام.',
            'icon': 'fas fa-home',
            'order': 2,
            'image': 'services/villa-en-construction.jpg',
        },
        {
            'title': 'Magasin ou concept-store',
            'title_fr': 'Magasin ou concept-store',
            'title_en': 'Store or concept store',
            'title_ar': 'متجر أو مساحة تجارية',
            'importance': 'Attirer les clients dès la phase de pré-lancement.',
            'importance_fr': 'Attirer les clients dès la phase de pré-lancement.',
            'importance_en': 'Attract customers from the pre-launch phase.',
            'importance_ar': 'جذب الزوار وبناء الترقب منذ مرحلة ما قبل الافتتاح.',
            'icon': 'fas fa-store',
            'order': 3,
            'image': 'services/magasin-concept-store.jpg',
        },
        {
            'title': 'Événementiel & Salons',
            'title_fr': 'Événementiel & Salons',
            'title_en': 'Events & Exhibitions',
            'title_ar': 'فعاليات ومعارض',
            'importance': 'Séduire et engager un public exigeant.',
            'importance_fr': 'Séduire et engager un public exigeant.',
            'importance_en': 'Captivate and engage a demanding audience.',
            'importance_ar': 'إبهار الجمهور واستقطاب اهتمام الشركاء بتجارب ثلاثية الأبعاد تفاعلية.',
            'icon': 'fas fa-calendar-star',
            'order': 4,
            'image': 'services/evenementiel.jpg',
        },
    ]

    for item in STRATEGIC_DATA:
        obj = StrategicSuccess.objects.filter(order=item['order']).first()
        if not obj:
            obj = StrategicSuccess.objects.filter(title_fr=item['title_fr']).first()
        if not obj:
            obj = StrategicSuccess(order=item['order'])

        for field, value in item.items():
            if hasattr(obj, field):
                setattr(obj, field, value)
        obj.is_active = True
        obj.save()


def unseed_strategic_successes(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_sitesettings_address_and_more'),
    ]

    operations = [
        migrations.RunPython(seed_strategic_successes, unseed_strategic_successes),
    ]
