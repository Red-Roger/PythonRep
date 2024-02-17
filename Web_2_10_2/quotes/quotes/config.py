import psycopg2
import json
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes.settings')
import django
from django.conf import settings

if not settings.configured:
    django.setup()
