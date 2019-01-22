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
from django.contrib import admin
from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from users import views as user_views, serializers as user_serializers


urlpatterns = [
    path('register/', user_views.CreateUserView.as_view()),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        user_serializers.activate, name='activate'),
    path('login/', obtain_jwt_token),
    path('token-refresh/', refresh_jwt_token),

    path('password_reset/', user_views.PasswordResetView.as_view()),
    path('password_reset_confirm/', user_views.PasswordResetConfirmView.as_view()),

    path('admin/', admin.site.urls),
]
