from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import TelegramBotSerializer, FacebookBotSerializer, MessagesChainSerializer, BotMessageSerializer
from .models import TelegramBot, FacebookBot, MessagesChain, BotMessage
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import permissions


class TelegramBotView(ListCreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = TelegramBot.objects.all()
    serializer_class = TelegramBotSerializer
    pagination_class = None


class TelegramBotRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = TelegramBotSerializer
    queryset = TelegramBot.objects.all()


class FacebookBotView(ListCreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = FacebookBot.objects.all()
    serializer_class = FacebookBotSerializer
    pagination_class = None


class FacebookBotRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = FacebookBotSerializer
    queryset = FacebookBot.objects.all()


class MessagesChainView(ListCreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = MessagesChain.objects.all()
    serializer_class = MessagesChainSerializer
    pagination_class = None


class MessagesChainRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = MessagesChainSerializer
    queryset = MessagesChain.objects.all()


class BotMessageView(ListCreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = BotMessage.objects.all()
    serializer_class = BotMessageSerializer
    pagination_class = None


class BotMessageRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = BotMessageSerializer
    queryset = BotMessage.objects.all()

