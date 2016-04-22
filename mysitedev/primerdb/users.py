from django.contrib.auth import authenticate
import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
django.setup()
from django.contrib.auth.models import User

print User.objects.filter(is_superuser=True)