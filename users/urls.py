from django.urls import path, re_path
from rest_framework import routers

from users import views
from rest_framework_simplejwt import views as jwt_views


app_name = 'users'


class ProfileRouter(routers.SimpleRouter):
    routes = [
        routers.Route(
            url=r'^{prefix}/$',
            mapping={'get': 'retrieve', 'put': 'update', 'patch': 'update', 'delete': 'destroy'},
            name='{basename}-profile',
            detail=True,
            initkwargs={}
        ),
    ]


router = ProfileRouter()
router.register('profile', views.UserProfileViewSet, base_name='User')

urlpatterns = router.urls

urlpatterns += [
    path('register/', views.CreateUserView.as_view()),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate, name='activate'),
    path('password_reset/', views.PasswordResetView.as_view()),
    path('password_reset_confirm/', views.PasswordResetConfirmView.as_view()),

    path('password_change/<user_id>/', views.PasswordChangeView.as_view()),

    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token_refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # path('credit_card_profile/create/', views.CreditCardProfileView.as_view()),
    # path('credit_card_profile/<user_id>/', views.CreditCardProfileView.as_view()),
    # path('credit_card_profile/<int:pk>/update/', views.CreditCardProfileUpdateDeleteView.as_view()),
    # path('credit_card_profile/<int:pk>/delete/', views.CreditCardProfileUpdateDeleteView.as_view()),
]


