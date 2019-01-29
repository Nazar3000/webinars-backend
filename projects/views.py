from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView, ListCreateAPIView, UpdateAPIView
from projects.models import Project, Webinar, AutoWebinar
from rest_framework.permissions import AllowAny
from projects.serializers import ProjectSerializer, UpdateActivationProjectSerializer, WebinarSerializer, \
    AutoWebinarSerializer, UserCountSerializer, WebinarChatActivateSerializer
from rest_framework.viewsets import ViewSet, ModelViewSet, GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from projects.mixins import WebinarMixin
from rest_framework import mixins


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
    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = Webinar.objects.all()
    serializer_class = WebinarSerializer
    serializer_active_chats = WebinarChatActivateSerializer


