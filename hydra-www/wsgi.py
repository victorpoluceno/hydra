import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'hydra.settings_production'
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "hydra/"))

import django.core.handlers.wsgi
application_django = django.core.handlers.wsgi.WSGIHandler()
application = WebSocketHandler('0.0.0.0', 80, application_django, 'socket.io')