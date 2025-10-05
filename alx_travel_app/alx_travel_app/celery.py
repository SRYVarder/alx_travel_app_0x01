import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

app = Celery('alx_travel_app')

app.config_from_object('django.config:settings', namespace='CELERY')

app.autodiscover_tasks()