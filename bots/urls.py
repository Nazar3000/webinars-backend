from django.urls import path, re_path
from bots import views
from bots.facebook import FacebookBotView

app_name = 'bots'

urlpatterns = [
    path('telegram_bot_create/', views.TelegramBotView.as_view(), name='list_create_telegram_bot'),
    path('facebook_bot_create/', views.FacebookBotView.as_view(), name='list_create_facebook_bot'),

    # hardcoded tokens
    path('facebook_bot/66d2b8f4a09cd35cb23076a1da5d51529136a3373fd570b122/',
         FacebookBotView.as_view(),
         name='facebook_bot_token'),
]

