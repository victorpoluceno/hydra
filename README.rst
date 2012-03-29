hydra
========


Install with vagrant (only once)
--------------------------------

::

    vagrant up
    vagrant ssh

::
    sudo apt-get install build-essential python-dev python-virtualenv libevent1-dev 

::
    curl http://npmjs.org/install.sh | sudo sh
     
::
    npm install socket.io sqlite3

::
    virtualenv --no-site-packages env

::
    source env/bin/activate

::
    pip install -r /vagrant/hydra-www/requiremets.txt

::
    cd /vagrant/
    python hydra/manage.py syncdb


Run (every time)
----------------

::
    vagrant up
    vagrant ssh

::
    source env/bin/activate

::
    cd vagrant

::
    node app_socketio.js &

::
	python hydra/manage.py runserver 0.0.0.0:8000
