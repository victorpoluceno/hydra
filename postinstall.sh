#!/bin/sh
sudo mkdir -p /srv/hydra/media /srv/hydra/static
cd hydra; sudo python manage.py collectstatic --noinput --settings=settings_production