#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gevent import monkey
monkey.patch_all()

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'hydra.settings'

import django.core.handlers.wsgi
from django.core.management import setup_environ
setup_environ(settings)

from socketio import SocketIOServer

from hydra import settings


PORT = 8000
HOSTNAME = '0.0.0.0'


if __name__ == '__main__':
    print 'Listening on port %s and on port 843 (flash policy server)' % PORT
    application = django.core.handlers.wsgi.WSGIHandler()
    SocketIOServer((HOSTNAME, PORT), application, namespace="api").serve_forever()