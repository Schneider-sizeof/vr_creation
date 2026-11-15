import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
import django
django.setup()

from apps.seo.models import PageSEO

legal_data = {
    'legal': {
        'fr': {
            'title': "Mentions légales & statut juridique | VR Creation",
            'desc': "Consultez les mentions légales de VR Creation Company à Tanger : statut de l'entreprise, hébergement, droits d'auteur et conditions d'utilisation du site."
        },
        'en': {
            'title': "Legal Notices & Company Terms | VR Creation",
            'desc': "Read the legal notices of VR Creation Company in Tangier: company details, website hosting, copyright, and general terms of service in Northern Morocco."
        },
        'ar': {
            'title': "الإشعار القانوني وشروط الاستخدام | VR Creation",
            'desc': "اطلع على الإشعارات القانونية لشركة VR Creation Company بطنجة: البيانات القانونية، الاستضافة، حقوق الملكية الفكرية وشروط استخدام الموقع الإلكتروني."
        }
    },
    'privacy': {
        'fr': {
            'title': "Politique de confidentialité (Loi 09-08) | VR Creation",
            'desc': "Protection de vos données personnelles et conformité à la loi marocaine 09-08 : découvrez la politique de confidentialité et de traitement de VR Creation."
        },
        'en': {
            'title': "Privacy Policy & Data Protection | VR Creation",
            'desc': "Our privacy policy outlines personal data handling, user rights, and full compliance with Moroccan law 09-08 for all clients of VR Creation Company."
        },
        'ar': {
            'title': "سياسة الخصوصية وحماية البيانات | VR Creation",
            'desc': "تعرف على سياسة حماية المعطيات ذات الطابع الشخصي والامتثال للقانون المغربي 09-08 لدى استوديو VR Creation Company لإنتاج المحتوى البصري بطنجة."
        }
    },
    'cookies': {
        'fr': {
            'title': "Gestion des cookies & traceurs web | VR Creation",
            'desc': "Politique relative aux cookies et traceurs de navigation sur vrcreationcompany.com : finalités, consentement utilisateur et paramétrage de vos préférences."
        },
        'en': {
            'title': "Cookie Policy & Tracking Preferences | VR Creation",
            'desc': "Understand how cookies and local storage are utilized on vrcreationcompany.com to enhance browsing performance, analytics, and interactive 3D media."
        },
        'ar': {
            'title': "سياسة ملفات تعريف الارتباط (الكوكيز) | VR Creation",
            'desc': "تعرف على سياسة ملفات تعريف الارتباط (الكوكيز) وأدوات التتبع المستخدمة في موقع vrcreationcompany.com وكيفية إدارة تفضيلات التصفح الخاصة بك بكل أمان."
        }
    }
}

for page_id, translations in legal_data.items():
    obj, created = PageSEO.objects.get_or_create(page_identifier=page_id)
    obj.meta_title_fr = translations['fr']['title']
    obj.meta_description_fr = translations['fr']['desc']
    obj.meta_title_en = translations['en']['title']
    obj.meta_description_en = translations['en']['desc']
    obj.meta_title_ar = translations['ar']['title']
    obj.meta_description_ar = translations['ar']['desc']
    obj.meta_title = translations['fr']['title']
    obj.meta_description = translations['fr']['desc']
    obj.save()
    print(f"Updated PageSEO for '{page_id}' (fr={len(obj.meta_description_fr)}, en={len(obj.meta_description_en)}, ar={len(obj.meta_description_ar)} chars)")
