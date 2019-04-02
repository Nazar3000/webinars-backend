from django.urls import path

from . import views

app_name = 'bots'

urlpatterns = [
    path(
        'viber-start/',
        views.ViberHandlerView.as_view(),
        name='viber_handler',
    ),
]
