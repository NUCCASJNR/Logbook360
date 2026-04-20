#!/bin/bash

# Stop on errors
set -e


echo "Make database migrations..."
python3 manage.py makemigrations --noinput

echo "🚀 Applying database migrations..."
python3 manage.py migrate --noinput


echo "🌍 Starting Gunicorn web server..."
# Start Gunicorn in the background
gunicorn sabirent.wsgi:application --bind 0.0.0.0:$PORT &

# Wait a few seconds to let Gunicorn boot up
sleep 5

echo "⚙️ Starting Celery worker..."
# Start Celery in the foreground (Render will keep this alive)
celery -A sabirent worker --loglevel=info --pool=solo
