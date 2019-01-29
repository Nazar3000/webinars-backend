from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from projects.models import Project, Webinar, AutoWebinar, WebinarFakeChatMessage, AutoWebinarFakeChatMessage
from rest_framework.permissions import AllowAny
from projects.serializers import ProjectSerializer, UpdateActivationProjectSerializer, WebinarSerializer, \
    AutoWebinarSerializer, UserCountSerializer, WebinarChatActivateSerializer, AutoWebinarChatActivateSerializer, \
    WebinarFakeChatMessageSerializer, AutoWebinarFakeChatMessageSerializer
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


class RetrieveUpdateProjectView(RetrieveUpdateAPIView):
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


class WebinarViewSet(WebinarMixin, ModelViewSet):
    # TODO: change permissions
    permission_classes = (AllowAny,)
    http_method_names = ['get', 'post', 'put', 'delete', 'patch']
    queryset = Webinar.objects.all()
    serializer_class = WebinarSerializer

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
    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = AutoWebinar.objects.all()
    serializer_class = AutoWebinarSerializer

    def get_serializer_class(self):
        if self.action == 'activate_chats':
            return AutoWebinarChatActivateSerializer
        else:
            return self.serializer_class


class WebinarFakeChatMessageListCreateView(ListCreateAPIView):
    # TODO: change permissions
    permission_classes = (AllowAny,)
    serializer_class = WebinarFakeChatMessageSerializer

    def get_queryset(self):
        webinar = self.kwargs['webinar_id']
        print(webinar)
        return WebinarFakeChatMessage.objects.filter(webinar_id=webinar)


class WebinarFakeChatMessageUpdateRetrieveDestroyView(RetrieveUpdateDestroyAPIView):
    # TODO: change permissions
    permission_classes = (AllowAny,)
    queryset = WebinarFakeChatMessage.objects.all()
    serializer_class = WebinarFakeChatMessageSerializer


class AutoWebinarFakeChatMessageListCreateView(ListCreateAPIView):
    # TODO: change permissions
    permission_classes = (AllowAny,)
    queryset = AutoWebinarFakeChatMessage.objects.all()
    serializer_class = AutoWebinarFakeChatMessageSerializer

    def get_queryset(self):
        webinar = self.kwargs['autowebinar_id']
        print(webinar)
        return WebinarFakeChatMessage.objects.filter(webinar_id=webinar)


class AutoWebinarFakeChatMessageUpdateRetrieveDestroyView(RetrieveUpdateDestroyAPIView):
    # TODO: change permissions
    permission_classes = (AllowAny,)
    queryset = AutoWebinarFakeChatMessage.objects.all()
    serializer_class = AutoWebinarFakeChatMessageSerializer


