import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'hydra.settings_production'
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "hydra/"))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()