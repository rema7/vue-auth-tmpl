#!/bin/bash

mkdir -p logs

pip install --pre -U -r /app/src/.meta/packages.dev

invoke init-config --db-connection="$DB_CONNECTION" --silent
invoke db.apply-migrations

gunicorn app:app -c gunicorn.conf.py --reload
