from django.urls import path, re_path
from bots import views

app_name = 'bots'

urlpatterns = [
    path('telegram_bot_create/', views.TelegramBotView.as_view()),
]

