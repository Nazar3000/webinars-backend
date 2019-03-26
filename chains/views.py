from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet

from .models import MessagesChain, Message
from .serializers import MessageChainSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework import status


class MessagesChainViewSet(ModelViewSet):
    serializer_class = MessageChainSerializer

    def get_queryset(self):
        return MessagesChain.objects.filter(project__pk=self.kwargs.get('project_pk'))

    def perform_create(self, serializer):
        serializer.save(project_pk=self.kwargs.get('project_pk'))


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(chain_id=self.kwargs.get('chain_pk'))

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, chain=self.kwargs.get('chain_pk'))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    
class UserTemplateMessageListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.user_templates.filter(chain__project_id=self.kwargs.get('project_id'))


class ServiceTemplateMessageListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Message.service_templates.all()
    serializer_class = MessageSerializer
