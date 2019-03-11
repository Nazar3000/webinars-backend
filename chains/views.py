from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import MessagesChain, Message
from .serializers import MessageChainSerializer, MessageSerializer



class MessageChainListCreateView(ListCreateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (permissions.AllowAny, )
    queryset = MessagesChain.objects.all()
    serializer_class = MessageChainSerializer


class MessageListCreateView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    
