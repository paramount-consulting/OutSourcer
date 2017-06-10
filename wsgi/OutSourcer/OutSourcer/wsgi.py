"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# GETTING-STARTED: change 'OutSourcer' to your project name:
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OutSourcer.settings")

application = get_wsgi_application()
