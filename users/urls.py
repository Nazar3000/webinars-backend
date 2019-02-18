from django.urls import path, re_path, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from users import views as user_views, serializers as user_serializers
from rest_framework_simplejwt import views as jwt_views


app_name = 'users'

urlpatterns = [
    path('register/', user_views.CreateUserView.as_view()),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            user_serializers.activate, name='activate'),
    path('activate_user/<int:user_id>/', user_views.activate_user),
    path('password_reset/', user_views.PasswordResetView.as_view()),
    path('password_reset_confirm/', user_views.PasswordResetConfirmView.as_view()),
    path('user/<int:pk>/retrieve/', user_views.UserProfileRetrieveUpdateDeleteView.as_view()),
    path('user/<int:pk>/update/', user_views.UserProfileRetrieveUpdateDeleteView.as_view()),
    path('user/<int:pk>/delete/', user_views.UserProfileRetrieveUpdateDeleteView.as_view()),

    path('credit_card_profile/create/', user_views.CreditCardProfileView.as_view()),
    path('credit_card_profiles/<int:pk>/', user_views.CreditCardProfileView.as_view()),

    path('credit_card_profile/<int:pk>/update/', user_views.CreditCardProfileUpdateDeleteView.as_view()),
    path('credit_card_profile/<int:pk>/delete/', user_views.CreditCardProfileUpdateDeleteView.as_view()),

    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

