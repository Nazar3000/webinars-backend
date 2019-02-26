from django.urls import path, re_path
from bots import views
from bots.facebook import FacebookBotView

app_name = 'bots'

urlpatterns = [
    # # telegram
    # path('telegram_bot/', views.TelegramBotListCreateView.as_view(), name='list_create_telegram_bot'),
    # path('telegram_bot/<int:pk>/', views.TelegramBotRetrieveUpdateView.as_view(), name='retrieve_update_telegram_bot'),
    #
    # # facebook
    # path('facebook_bot/', views.FacebookBotListCreateView.as_view(), name='list_create_facebook_bot'),
    # path('facebook_bot/<int:pk>/', views.FacebookRetrieveUpdateView.as_view(), name='retrieve_update_facebook_bot'),
    #
    # # viber
    # path('viber_bot/', views.ViberBotListCreateView.as_view(), name='list_create_viber_bot'),
    # path('viber_bot/<int:pk>/', views.ViberBotRetrieveUpdate.as_view(), name='retrieve_update_viber_bot'),
    #
    # # whatsapp
    # path('whatsapp_bot/', views.WhatsAppListCreateBotView.as_view(), name='list_create_whatsapp_bot'),
    # path('whatsapp_bot/<int:pk>/', views.WhatsAppRetrieveUpdateView.as_view(), name='retrieve_update_whatsapp_bot'),
    #
    # # chains
    # path('message_chain_create/', views.MessagesChainView.as_view(), name='list_create_message_chain'),
    # path('message_chain/<int:pk>/retrieve/', views.MessagesChainRetrieveUpdateDeleteView.as_view()),
    # path('message_chain/<int:pk>/update/', views.MessagesChainRetrieveUpdateDeleteView.as_view()),
    # path('message_chain/<int:pk>/delete/', views.MessagesChainRetrieveUpdateDeleteView.as_view()),
    # path('bot_message_create/', views.BotMessageView.as_view(), name='list_create_bot_message'),
    # path('bot_message/<int:pk>/retrieve/', views.BotMessageRetrieveUpdateDeleteView.as_view()),
    # path('bot_message/<int:pk>/update/', views.BotMessageRetrieveUpdateDeleteView.as_view()),
    # path('bot_message/<int:pk>/delete/', views.BotMessageRetrieveUpdateDeleteView.as_view()),


]

