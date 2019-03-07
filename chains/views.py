from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import MessagesChain
from .serializers import MessageChainSerializer


class MessageChainListCreateView(ListCreateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    queryset = MessagesChain.objects.all()
    serializer_class = MessageChainSerializer


