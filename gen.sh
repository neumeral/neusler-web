#!/bin/sh

# Generate static site using django-distill

echo 'Running collect static ... '
rm -rf staticfiles
python  manage.py collectstatic --noinput
echo 'DONE!'

echo 'Generating static site files in _site folder ... '
rm -rf _site
DEVELOPMENT_MODE=True python manage.py distill-local _site --force
echo 'DONE!'

