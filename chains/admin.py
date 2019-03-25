from django.contrib import admin
from .models import MessagesChain, Message

admin.site.register(MessagesChain)
admin.site.register(Message)
