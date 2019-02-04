from rest_framework import serializers
from .models import TelegramBot, FacebookBot


class TelegramBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramBot
        fields = '__all__'


class FacebookBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookBot
        fields = '__all__'
