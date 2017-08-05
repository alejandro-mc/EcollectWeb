"""
WSGI config for EcollectWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EcollectWeb.settings")


from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise



application = get_wsgi_application()
application = DjangoWhiteNoise(application)

