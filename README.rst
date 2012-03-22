hydra
========


Install
-------

::
    sudo apt-get install build-essential python-dev python-virtualenv libevent-1.4-2 libevent1-dev nodejs nodejs-dev curl

::
    curl http://npmjs.org/install.sh | sudo sh
     
::
    npm install socket.io sqlite3

::
    virtualenv --no-site-packages env

::
    source env/bin/activate

::
    pip install -r requiremets.txt

::

    cd hydra; python manage.py syncdb

Run
---

::
    node app_socketio.js &

::
    cd hydra; python manage.py runserver 0.0.0.0:8000
