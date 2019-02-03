#!/usr/bin/env bash
if [ -z $VIRTUAL_ENV ];
    then
        sudo pip install --upgrade pip
        sudo pip install -r requirements.txt
    else
        pip install --upgrade pip
        pip install -r requirements.txt
fi;
python manage.py migrate
echo "yes" | python manage.py collectstatic
python manage.py createsuperuser