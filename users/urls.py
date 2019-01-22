from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from users import views as user_views, serializers as user_serializers


app_name = 'users'

urlpatterns = [
    path('register/', user_views.CreateUserView.as_view()),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            user_serializers.activate, name='activate'),
    path('login/', obtain_jwt_token, name='login'),
    path('token-refresh/', refresh_jwt_token, name='refresh_token'),
    path('password_reset/', user_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/', user_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
