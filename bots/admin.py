from django.contrib import admin
from .models import TelegramBot, FacebookBot

admin.site.register(TelegramBot)
admin.site.register(FacebookBot)
