hydra
========


Install with vagrant (only once)
--------------------------------

::

    vagrant up
    vagrant ssh

::
    cd vagrant

::
    sudo apt-get install build-essential python-dev python-virtualenv nodejs nodejs-dev curl

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
    python hydra/manage.py syncdb


Run (every time)
----------------

::
    vagrant up
    vagrant ssh

::
    cd vagrant

::
    node app_socketio.js &

::
	source env/bin/activate
    python hydra/manage.py runserver 0.0.0.0:8000
