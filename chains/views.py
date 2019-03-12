from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import MessagesChain, Message
from .serializers import MessageChainSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework import status


class MessageChainListCreateView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = MessageChainSerializer

    def get_queryset(self):
        return MessagesChain.objects.filter(project_id=self.kwargs.get('project_id'))

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, project_id=self.kwargs.get('project_id'))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    
class MessageChainRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = MessagesChain.objects.all()

    def get_queryset(self):
        return MessagesChain.objects.filter(project_id=self.kwargs.get('project_id'))


class MessageListCreateView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(chain_id=self.kwargs.get('chain_id'))
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, chain=self.kwargs.get('chain_id'))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MessageRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    
class UserTemplateMessageListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.user_templates.filter(chain__project_id=self.kwargs.get('project_id'))


class ServiceTemplateMessageListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Message.service_templates.all()
    serializer_class = MessageSerializer


