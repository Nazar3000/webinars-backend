from django.urls import path, re_path
from bots import views
from bots.facebook import FacebookBotView

app_name = 'bots'

urlpatterns = [
    path('telegram_bot_create/', views.TelegramBotView.as_view(), name='list_create_telegram_bot'),
    path('telegram_bot/<int:pk>/retrieve/', views.TelegramBotRetrieveUpdateDeleteView.as_view()),
    path('telegram_bot/<int:pk>/update/', views.TelegramBotRetrieveUpdateDeleteView.as_view()),
    path('telegram_bot/<int:pk>/delete/', views.TelegramBotRetrieveUpdateDeleteView.as_view()),
    path('facebook_bot_create/', views.FacebookBotView.as_view(), name='list_create_facebook_bot'),
    path('facebook_bot/<int:pk>/retrieve/', views.FacebookBotRetrieveUpdateDeleteView.as_view()),
    path('facebook_bot/<int:pk>/update/', views.FacebookBotRetrieveUpdateDeleteView.as_view()),
    path('facebook_bot/<int:pk>/delete/', views.FacebookBotRetrieveUpdateDeleteView.as_view()),
    path('message_chain_create/', views.MessagesChainView.as_view(), name='list_create_message_chain'),
    path('message_chain/<int:pk>/retrieve/', views.MessagesChainRetrieveUpdateDeleteView.as_view()),
    path('message_chain/<int:pk>/update/', views.MessagesChainRetrieveUpdateDeleteView.as_view()),
    path('message_chain/<int:pk>/delete/', views.MessagesChainRetrieveUpdateDeleteView.as_view()),
    path('bot_message_create/', views.BotMessageView.as_view(), name='list_create_bot_message'),
    path('bot_message/<int:pk>/retrieve/', views.BotMessageRetrieveUpdateDeleteView.as_view()),
    path('bot_message/<int:pk>/update/', views.BotMessageRetrieveUpdateDeleteView.as_view()),
    path('bot_message/<int:pk>/delete/', views.BotMessageRetrieveUpdateDeleteView.as_view()),

    # hardcoded tokens
    path('facebook_bot/66d2b8f4a09cd35cb23076a1da5d51529136a3373fd570b122/',
         FacebookBotView.as_view(),
         name='facebook_bot_token'),
]

