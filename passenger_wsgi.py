"""
Passenger WSGI entry point for Namecheap cPanel hosting.
This file is used by Phusion Passenger to serve the Django application.
"""
import os
import sys
from pathlib import Path

# Add project to Python path
project_path = Path(__file__).resolve().parent
if str(project_path) not in sys.path:
    sys.path.insert(0, str(project_path))

# Load .env
try:
    from dotenv import load_dotenv
    env_path = project_path / '.env'
    if env_path.exists():
        load_dotenv(str(env_path))
except ImportError:
    pass

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings.prod'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
