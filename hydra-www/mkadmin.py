#!/usr/bin/env python
import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'hydra.settings_production'
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "hydra/"))


from django.contrib.auth.models import User
u, created = User.objects.get_or_create(username='admin')
if created:
    u.set_password('zxcv')
    u.is_superuser = True
    u.is_staff = True
    u.save()