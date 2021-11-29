#!/bin/bash
flask db upgrade

if [ "$FLASK_ENV" == "development" ]; then
    flask run --host=0.0.0.0
else
    gunicorn --bind 0.0.0.0:5000 app:app
fi
