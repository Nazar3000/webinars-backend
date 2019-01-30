from rest_framework.generics import ListCreateAPIView, UpdateAPIView, \
    RetrieveUpdateDestroyAPIView
from projects.models import Project, Webinar, AutoWebinar, WebinarFakeChatMessage, AutoWebinarFakeChatMessage
from rest_framework.permissions import AllowAny
from projects.serializers import ProjectSerializer, UpdateActivationProjectSerializer, WebinarSerializer, \
    AutoWebinarSerializer, UserCountSerializer, WebinarChatActivateSerializer, AutoWebinarChatActivateSerializer, \
    WebinarFakeChatMessageSerializer, AutoWebinarFakeChatMessageSerializer, WebinarFakeMessageSerializer, \
    AutoWebinarFakeMessageSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from projects.mixins import WebinarMixin


class ListCreateProjectView(ListCreateAPIView):
    model = Project
    # TODO: change permissions
    permission_classes = (AllowAny,)
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class RetrieveUpdateDestroyProjectView(RetrieveUpdateDestroyAPIView):
    model = Project
    # TODO: change permissions
    permission_classes = (AllowAny, )
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class UpdateProjectActivation(UpdateAPIView):
    model = Project
    serializer_class = UpdateActivationProjectSerializer
    # TODO: change permissions
    permission_classes = (AllowAny, )
    queryset = Project.objects.all()
    http_method_names = ['put']


class WebinarViewSet(WebinarMixin, ModelViewSet):
    # TODO: change permissions
    permission_classes = (AllowAny,)
    http_method_names = ['get', 'post', 'put', 'delete', 'patch']
    serializer_class = WebinarSerializer
    queryset = Webinar.objects.all()

    def get_serializer_class(self):
        if self.action == 'activate_chats':
            return WebinarChatActivateSerializer
        elif self.action == 'user_fake_count':
            return UserCountSerializer
        else:
            return self.serializer_class


class AutoWebinarViewSet(WebinarMixin, ModelViewSet):
    # TODO: change permissions
    permission_classes = (AllowAny,)
    http_method_names = ['get', 'post', 'put', 'delete', 'patch']
    queryset = AutoWebinar.objects.all()
    serializer_class = AutoWebinarSerializer

    def get_serializer_class(self):
        if self.action == 'activate_chats':
            return AutoWebinarChatActivateSerializer
        else:
            return self.serializer_class


class ListCreateWebinarFakeChatMessageView(ListCreateAPIView):
    # TODO: change permissions
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WebinarFakeMessageSerializer
        else:
            return WebinarFakeChatMessageSerializer

    def get_queryset(self):
        webinar = self.kwargs['webinar_id']
        return WebinarFakeChatMessage.objects.filter(webinar_id=webinar)


class UpdateRetrieveDestroyWebinarFakeChatMessageView(RetrieveUpdateDestroyAPIView):
    # TODO: change permissions
    permission_classes = (AllowAny,)
    queryset = WebinarFakeChatMessage.objects.all()
    serializer_class = WebinarFakeChatMessageSerializer

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return WebinarFakeMessageSerializer
        else:
            return WebinarFakeChatMessageSerializer


class ListCreateAutoWebinarFakeChatMessageView(ListCreateAPIView):
    # TODO: change permissions
    permission_classes = (AllowAny,)
    queryset = AutoWebinarFakeChatMessage.objects.all()
    serializer_class = AutoWebinarFakeChatMessageSerializer

    def get_queryset(self):
        webinar = self.kwargs['autowebinar_id']
        return WebinarFakeChatMessage.objects.filter(webinar_id=webinar)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AutoWebinarFakeMessageSerializer
        else:
            return AutoWebinarFakeChatMessageSerializer


class UpdateRetrieveDestroyAutoWebinarFakeChatMessageView(RetrieveUpdateDestroyAPIView):
    # TODO: change permissions
    permission_classes = (AllowAny,)
    queryset = AutoWebinarFakeChatMessage.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return AutoWebinarFakeMessageSerializer
        else:
            return AutoWebinarFakeChatMessageSerializer
