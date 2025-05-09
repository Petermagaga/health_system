import os
import sys

# Ensure the project directory is in the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'health_system'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'health_system.settings')

application = get_wsgi_application()
