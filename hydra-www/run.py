from gevent import monkey; monkey.patch_all()

import os
import sys

import django.core.handlers.wsgi
from socketio import SocketIOServer


PORT = 8000
PROJECT_ROOT = os.path.dirname(__file__)


os.environ['DJANGO_SETTINGS_MODULE'] = 'hydra.settings_production'
sys.path.insert(0, os.path.join(PROJECT_ROOT, "hydra/"))


if __name__ == '__main__':
    print 'Listening on port %s and on port 843 (flash policy server)' % PORT
    application = django.core.handlers.wsgi.WSGIHandler()
    SocketIOServer(('0.0.0.0', PORT), application, namespace="socket.io").serve_forever()