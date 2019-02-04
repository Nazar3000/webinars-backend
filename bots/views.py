from rest_framework.generics import ListCreateAPIView
from .serializers import TelegramBotSerializer, FacebookBotSerializer
from .models import TelegramBot, FacebookBot
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import permissions


class TelegramBotView(ListCreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = TelegramBot.objects.all()
    serializer_class = TelegramBotSerializer
    pagination_class = None


class FacebookBotView(ListCreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication, )
    queryset = FacebookBot.objects.all()
    serializer_class = FacebookBotSerializer
    pagination_class = None
