import threading

from django.contrib.auth import get_user_model
from djangorestframework_camel_case.parser import CamelCaseJSONParser
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
import requests

from projects.models import Project, Webinar, WebinarFakeChatMessage, WebinarOnlineWatchersCount
from rest_framework.permissions import AllowAny
from projects.serializers import ProjectSerializer, WebinarSerializer, \
    UserCountSerializer, WebinarFakeMessageSerializer, WebinarFakeChatMessageSerializer, \
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
        if self.action in ['check_publish_stream_permission', 'check_play_stream_permission', 'check_stream_status']:
            return WebinarPermissionSerializer
        return ProjectSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, user=request.user)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['post'])
    def check_publish_stream_permission(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        data = serializer.validated_data
        try:
            project = Project.objects.get(user_id=data['user_id'], is_active=True)
            webinar = Webinar.objects.get(project=project, slug=data['slug'])

            WebinarOnlineWatchersCount.objects.get_or_create(webinar=webinar)
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

    @action(detail=False, methods=['post'])
    def check_stream_status(self, request, *args, **kwargs):
        data_to_response = {}
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        data = serializer.validated_data
        webinar = get_object_or_404(Webinar, slug=data['slug'])
        r = requests.get(url='http://django:8000/' + webinar.slug + '.m3u8')
        # r = requests.get(url='https://foxery.io/test.m3u8')
        user = User.objects.get(pk=data['user_id'])
        if r.status_code != 200:
            if webinar.stream_datetime > timezone.localtime(timezone=user.timezone):
                data_to_response['time_left_to_start_streaming'] = (webinar.stream_datetime - timezone.localtime(timezone=user.timezone)).seconds
            else:
                data_to_response['time_left_to_start_streaming'] = 0

            if webinar.image_cover:
                data_to_response['image_cover'] = webinar.image_cover.url
            else:
                data_to_response['image_cover'] = None

            if webinar.video_cover:
                data_to_response['video_cover'] = webinar.video_cover.url
            else:
                data_to_response['video_cover'] = None
            return Response(
                status=status.HTTP_206_PARTIAL_CONTENT,
                data=data_to_response
            )
        else:
            return Response(status=status.HTTP_200_OK)


class WebinarViewSet(WebinarMixin, ModelViewSet):
    # TODO: change permissions
    permission_classes = (AllowAny,)
    serializer_class = WebinarSerializer
    parser_classes = (MultiPartParser, CamelCaseJSONParser,)

    def get_queryset(self):
        return Webinar.objects.filter(project__pk=self.kwargs.get('project_pk'))

    def get_serializer_class(self):
        if self.action == 'user_fake_count':
            return UserCountSerializer
        else:
            return self.serializer_class

    def perform_create(self, serializer):
        if Project.objects.filter(pk=self.kwargs.get('project_pk')).exists():
            serializer.save(project_id=self.kwargs.get('project_pk'))
        else:
            raise ValidationError({
                'project': 'Project with id={} does not exist'.format(self.kwargs.get('project_pk'))})

    def perform_update(self, serializer):
        if Project.objects.filter(pk=self.kwargs.get('project_pk')).exists():
            serializer.save(project_id=self.kwargs.get('project_pk'))
        else:
            raise ValidationError({
                'project': 'Project with id={} does not exist'.format(self.kwargs.get('project_pk'))})


class FakeChatMessageViewSet(ModelViewSet):
    def get_queryset(self):
        return WebinarFakeChatMessage.objects.filter(webinar__pk=self.kwargs.get('webinar_pk'))

    def get_serializer_class(self):
        if self.action in ['list', 'destroy']:
            return WebinarFakeChatMessageSerializer
        else:
            return WebinarFakeMessageSerializer
