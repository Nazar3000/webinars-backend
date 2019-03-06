from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from projects.models import Project, Webinar, WebinarFakeChatMessage
from rest_framework.permissions import AllowAny
from projects.serializers import ProjectSerializer, UpdateActivationProjectSerializer, WebinarSerializer, \
    UserCountSerializer, WebinarChatActivateSerializer, WebinarFakeMessageSerializer, WebinarFakeChatMessageSerializer, \
    WebinarPermissionSerializer
from rest_framework.viewsets import ModelViewSet
from projects.mixins import WebinarMixin

User = get_user_model()


class ProjectViewSet(ModelViewSet):
    # TODO: change permissions
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'activate':
            return UpdateActivationProjectSerializer
        elif self.action in ['check_publish_stream_permission', 'check_play_stream_permission']:
            return WebinarPermissionSerializer
        return ProjectSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, user=request.user)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['patch'])
    def activate(self, request, *args, **kwargs):
        serializer = self.get_serializer(instance=self.get_object(), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def check_publish_stream_permission(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        data = serializer.validated_data
        try:
            project = Project.objects.get(user_id=data['user_id'], is_active=True)
            Webinar.objects.get(project=project, slug=data['slug'])
        except (Project.DoesNotExist, Webinar.DoesNotExist):
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def check_play_stream_permission(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        data = serializer.validated_data
        webinar = get_object_or_404(Webinar, slug=data['slug'])
        user = User.objects.get(pk=data['user_id'])
        if user not in webinar.viewers.all():
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_200_OK)


class WebinarViewSet(WebinarMixin, ModelViewSet):
    # TODO: change permissions
    permission_classes = (AllowAny,)
    serializer_class = WebinarSerializer

    def get_queryset(self):
        return Webinar.objects.filter(project=self.kwargs['project_pk'])

    def get_serializer_class(self):
        if self.action == 'activate_chats':
            return WebinarChatActivateSerializer
        elif self.action == 'user_fake_count':
            return UserCountSerializer
        else:
            return self.serializer_class

    # TODO: pass project
    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()


class FakeChatMessageViewSet(ModelViewSet):
    def get_queryset(self):
        return get_object_or_404(WebinarFakeChatMessage, webinar__pk=self.kwargs.get('webinar_pk'))

    def get_serializer_class(self):
        if self.action in ['list', 'destroy']:
            return WebinarFakeChatMessageSerializer
        else:
            return WebinarFakeMessageSerializer
