import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'hydra.settings_production'
sys.path.insert(0, "player/")

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()