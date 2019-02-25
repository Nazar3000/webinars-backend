from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from projects.models import Project, Webinar
from rest_framework.permissions import AllowAny
from projects.serializers import ProjectSerializer, UpdateActivationProjectSerializer, WebinarSerializer, \
    UserCountSerializer, WebinarChatActivateSerializer, WebinarFakeMessageSerializer, WebinarFakeChatMessageSerializer
from rest_framework.viewsets import ModelViewSet
from projects.mixins import WebinarMixin


class ProjectViewSet(ModelViewSet):
    # TODO: change permissions
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action:
            return UpdateActivationProjectSerializer
        return ProjectSerializer

    @action(detail=True, methods=['patch'])
    def activate(self, request, *args, **kwargs):
        serializer = self.get_serializer(instance=self.get_object(), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class FakeChatMessageViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action in ['list', 'destroy']:
            return WebinarFakeChatMessageSerializer
        else:
            return WebinarFakeMessageSerializer


class WebinarViewSet(WebinarMixin, ModelViewSet):
    # TODO: change permissions
    permission_classes = (AllowAny,)
    serializer_class = WebinarSerializer
    queryset = Webinar.objects.all()

    def get_serializer_class(self):
        if self.action == 'activate_chats':
            return WebinarChatActivateSerializer
        elif self.action == 'user_fake_count':
            return UserCountSerializer
        else:
            return self.serializer_class
