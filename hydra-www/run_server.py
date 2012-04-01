#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gevent import monkey
monkey.patch_all()

import os
import sys

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "hydra/"))

os.environ['DJANGO_SETTINGS_MODULE'] = 'hydra.settings'

import django.core.handlers.wsgi
from django.core.management import setup_environ

from socketio import SocketIOServer

from hydra import settings
setup_environ(settings)


PORT = 8000
HOSTNAME = '0.0.0.0'


if __name__ == '__main__':
    print 'Listening on port %s and on port 843 (flash policy server)' % PORT
    application = django.core.handlers.wsgi.WSGIHandler()
    SocketIOServer((HOSTNAME, PORT), application, namespace="socket.io").serve_forever()