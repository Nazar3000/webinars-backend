"""Project_W URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from channels.auth import AuthMiddlewareStack
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema
from drf_yasg.views import get_schema_view
from rest_framework.permissions import IsAdminUser
from django.conf import settings
from django.conf.urls.static import static
from channels.routing import ProtocolTypeRouter, URLRouter
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AnonymousUser

from chat.urls import websocket_urlpatterns


class CategorizedAutoSchema(SwaggerAutoSchema):
    def get_tags(self, operation_keys):
        if len(operation_keys) >= 1:
            operation_keys = operation_keys[1:]
        return super().get_tags(operation_keys)


schema_view = get_schema_view(
    openapi.Info(
      title="Webinars API",
      default_version='v1',
    ),
    permission_classes=(IsAdminUser,),
)


class TokenAuthMiddleware:
    """
    Token authorization middleware for Django Channels 2
    """

    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        headers = dict(scope['headers'])
        if b'sec-websocket-protocol' in headers:
            try:
                token_name, token_key = headers[b'sec-websocket-protocol'].decode().split(', ')
                self.get_user(token_key)
                if token_name == 'Token':
                    print(Token)
                    print(Token.objects.all())
                    token = Token.objects.get(key=token_key)
                    scope['user'] = token.user
            except Exception as e:
                print(e)
                scope['user'] = AnonymousUser()
        return self.inner(scope)


TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(AuthMiddlewareStack(inner))


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui(), name='docs'),
    path('chat/', include('chat.urls')),

    path('api/<version>/', include('users.urls')),
    path('api/<version>/projects/', include('projects.urls')),
    path('api/<version>/projects/', include('chains.urls'))
] \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
