#!/usr/bin/python
from gevent import monkey; monkey.patch_all()
from gevent.wsgi import WSGIServer

import sys
import os
import traceback

from django.core.handlers.wsgi import WSGIHandler
from django.core.management import call_command
from django.core.signals import got_request_exception

sys.path.append('/vagrant/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'hydra.settings_production'

def exception_printer(sender, **kwargs):
    traceback.print_exc()

got_request_exception.connect(exception_printer)

print 'Serving on 8000...'
WSGIServer(('', 8000), WSGIHandler()).serve_forever()