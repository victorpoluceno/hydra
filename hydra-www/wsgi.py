from gevent import monkey; monkey.patch_all()

import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'hydra.settings_production'
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "hydra/"))

import django.core.handlers.wsgi
from socketio.handler import SocketIOHandler

application_django = django.core.handlers.wsgi.WSGIHandler()
application = SocketIOHandler('0.0.0.0', 80, application_django, 'socket.io')

"""
from geventwebsocket.handler import WebSocketHandler
from gunicorn.workers.ggevent import GeventPyWSGIWorker


class GeventWebSocketWorker(GeventPyWSGIWorker):
    wsgi_handler = WebSocketHandler"""