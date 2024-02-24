from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from app.consumers import ChatConsumer
from app.models import ChatMessage
websocket_urlpatterns = [
    path('ws/chat/', ChatConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})