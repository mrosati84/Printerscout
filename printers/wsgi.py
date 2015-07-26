"""
WSGI config for printers project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

env = os.environ.get('DJANGO_ENV') or 'local'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", '.'.join(['settings', env]))

application = get_wsgi_application()
