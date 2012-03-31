#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gevent import monkey; 
monkey.patch_all()

import os

from hydra import settings as settings

import django.core.handlers.wsgi
from socketio import SocketIOServer

from django.core.management import setup_environ
setup_environ(settings)


os.environ['DJANGO_SETTINGS_MODULE'] = 'hydra.settings'
application = django.core.handlers.wsgi.WSGIHandler()