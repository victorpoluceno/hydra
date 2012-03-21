hydra
========


Install
-------

::
    sudo apt-get install python-dev python-virtualenv libevent-1.4-2 libevent1-dev nodejs nodejs-dev curl

::
    sudo curl http://npmjs.org/install.sh | sh 
     
::
    npm install socket.io

::
    virtualenv --no-site-packages env

::
    source env/bin/activate

::
    pip install -r requiremets.txt

Run
---

::
    node app_socketio.js &
    cd hydra; python manage.py runserver 0.0.0.0:8000