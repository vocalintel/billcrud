"""
WSGI config for xboards project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xboards.settings')

# application = get_wsgi_application()

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xboards.settings')

try:
    application = get_wsgi_application()
except Exception as e:
    import sys
    print(f"WSGI application failed to load: {e}", file=sys.stderr)
    raise

