from socketio.handler import SocketIOHandler
from gunicorn.workers.ggevent import GeventPyWSGIWorker


class GeventSocketIOWorker(GeventPyWSGIWorker):
    wsgi_handler = SocketIOHandler