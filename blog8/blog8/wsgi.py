"""
WSGI config for blog8 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# cambio agregado: production

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog8.blog8.settings.production')

application = get_wsgi_application()
