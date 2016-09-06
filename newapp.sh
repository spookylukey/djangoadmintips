#!/bin/zsh

NAME=$1

VENV=~/.virtualenvs/djangoadmintips_$NAME
virtualenv $VENV --python=`which python3.5` || exit 1
. $VENV/bin/activate
pip install Django ipython || exit 1
PATH=$PATH
mkdir $NAME
django-admin startproject $NAME $NAME || exit 1
cd $NAME
./manage.py migrate || exit 1
./manage.py createsuperuser --username=admin --email=admin@example.com --noinput || exit 1
./manage.py shell -c "from django.contrib.auth.models import *; u = User.objects.get(); u.set_password('adminadmin'); u.save()" || exit 1

cp ~/devel/.template-python.dir-locals.el .dir-locals.el
echo "Remember to edit .dir-locals"
