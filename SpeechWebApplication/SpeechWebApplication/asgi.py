"""
ASGI config for SpeechWebApplication project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import Speech.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SpeechWebApplication.settings')

#application = get_asgi_application()
application=ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket': URLRouter(
        Speech.routing.websocket_urlpatterns
    )
})
