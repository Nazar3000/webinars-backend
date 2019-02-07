from django.contrib import admin
from .models import TelegramBot, FacebookBot, MessagesChain, BotMessage

admin.site.register(TelegramBot)
admin.site.register(FacebookBot)
admin.site.register(MessagesChain)
admin.site.register(BotMessage)
