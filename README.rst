hydra
========


Install with vagrant (only once)
--------------------------------

Run vagrant and get into vm::

    vagrant up
    vagrant ssh

Create upload dir::

    mkdir -p /srv/hydra/media/player/
    chown -R vagrant:vagrant /srv

Install system packages::

    sudo apt-get update && sudo apt-get upgrade
    sudo apt-get install build-essential python-dev python-virtualenv libevent1-dev 

Create a python virtual env::

    virtualenv --no-site-packages env

Activate and install required python packages::

    source env/bin/activate
    pip install -r /vagrant/hydra-www/requirements.txt

Go to apps dir and create database::

    cd /vagrant/hydra-www/
    python hydra/manage.py syncdb


Run (every time)
----------------

Run vagrant and get into vm::

    vagrant up
    vagrant ssh

Activate python virtual env::

    source env/bin/activate

Go to apps dir and run the devel server::

    cd /vagrant/hydra-www/
	python run_server.py runserver