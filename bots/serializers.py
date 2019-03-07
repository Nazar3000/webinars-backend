from rest_framework import serializers
from .models import TelegramBot, FacebookBot, WhatsAppBot, ViberBot


class TelegramBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramBot
        fields = '__all__'


class FacebookBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookBot
        fields = '__all__'


class ViberBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViberBot
        fields = '__all__'


class WhatsAppBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatsAppBot
        fields = '__all__'
