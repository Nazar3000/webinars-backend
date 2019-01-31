from django.urls import path, include
from bots.facebook import FacebookBotView

app_name = 'bots'

urlpatterns = [
    path('facebook_bot/66d2b8f4a09cd35cb23076a1da5d51529136a3373fd570b122/',
         FacebookBotView.as_view(),
         name='facebook_bot'),
]