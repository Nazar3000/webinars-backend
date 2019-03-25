from rest_framework import serializers
from .models import BotBase


class TelegramBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotBase
        fields = (
            'name',
            'api_key',
            'active',
            'user',
            'bot_type',
        )
