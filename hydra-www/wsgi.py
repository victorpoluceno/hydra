#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gevent import monkey; 
monkey.patch_all()

import os
import sys

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "hydra/"))

from hydra import settings_production as settings

import django.core.handlers.wsgi
from django.core.management import setup_environ
setup_environ(settings)


os.environ['DJANGO_SETTINGS_MODULE'] = 'hydra.settings_production'
application = django.core.handlers.wsgi.WSGIHandler()