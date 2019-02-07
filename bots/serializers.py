from rest_framework import serializers
from .models import TelegramBot, FacebookBot, MessagesChain, BotMessage, WhatsAppBot, ViberBot


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


class MessagesChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessagesChain
        fields = '__all__'


class BotMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessagesChain
        fields = '__all__'
