from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .serializers import TelegramBotSerializer, FacebookBotSerializer, ViberBotSerializer, WhatsAppBotSerializer
from .models import TelegramBot, FacebookBot, ViberBot, WhatsAppBot
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import TelegramBotSerializer, FacebookBotSerializer
from .models import TelegramBot, FacebookBot


# Telegram

class TelegramBotListCreateView(ListCreateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    queryset = TelegramBot.objects.all()
    serializer_class = TelegramBotSerializer
    pagination_class = None


class TelegramBotRetrieveUpdateView(RetrieveUpdateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    queryset = TelegramBot.objects.all()
    serializer_class = TelegramBotSerializer


# Facebook

class FacebookBotListCreateView(ListCreateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    queryset = FacebookBot.objects.all()
    serializer_class = FacebookBotSerializer
    pagination_class = None


class FacebookRetrieveUpdateView(RetrieveUpdateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = FacebookBotSerializer
    queryset = FacebookBot.objects.all()


class TelegramBotRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = TelegramBotSerializer
    queryset = TelegramBot.objects.all()


class FacebookBotView(ListCreateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    queryset = FacebookBot.objects.all()
    serializer_class = FacebookBotSerializer


# Viber

class ViberBotListCreateView(ListCreateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    queryset = ViberBot.objects.all()
    serializer_class = ViberBotSerializer
    pagination_class = None


class ViberBotRetrieveUpdate(RetrieveUpdateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    queryset = ViberBot.objects.all()
    serializer_class = ViberBotSerializer


# WhatsApp

class WhatsAppListCreateBotView(ListCreateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    queryset = WhatsAppBot.objects.all()
    serializer_class = WhatsAppBotSerializer
    pagination_class = None


class WhatsAppRetrieveUpdateView(RetrieveUpdateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    queryset = WhatsAppBot.objects.all()
    serializer_class = WhatsAppBotSerializer


# Chains

class FacebookBotRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = FacebookBotSerializer
    queryset = FacebookBot.objects.all()


class MessagesChainView(ListCreateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    queryset = MessagesChain.objects.all()
    serializer_class = MessagesChainSerializer
    pagination_class = None


class MessagesChainRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = MessagesChainSerializer
    queryset = MessagesChain.objects.all()


class BotMessageView(ListCreateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    queryset = BotMessage.objects.all()
    serializer_class = BotMessageSerializer
    pagination_class = None


class BotMessageRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = BotMessageSerializer
    queryset = BotMessage.objects.all()

