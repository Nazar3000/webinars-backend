from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView, ListCreateAPIView, UpdateAPIView
from projects.models import Project, Webinar, AutoWebinar
from rest_framework.permissions import AllowAny
from projects.serializers import ProjectSerializer, UpdateActivationProjectSerializer, WebinarSerializer, \
    AutoWebinarSerializer, UserCountSerializer
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class ListCreateProjectView(ListCreateAPIView):
    model = Project
    # TODO: change permissions
    permission_classes = (AllowAny,)
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return self.model.objects.all()


class RetrieveUpdateProjectView(RetrieveUpdateAPIView):
    model = Project
    permission_classes = (AllowAny, )
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class UpdateProjectActivation(UpdateAPIView):
    model = Project
    serializer_class = UpdateActivationProjectSerializer
    # TODO: change permissions
    permission_classes = (AllowAny, )
    queryset = Project.objects.all()


# class ListCreateWebinar(ListCreateAPIView):
#     model = Webinar
#     serializer_class = WebinarSerializer
#     # TODO: change permissions
#     permission_classes = (AllowAny, )
#     queryset = Webinar.objects.all()
#
#
# class ListCreateAutoWebinar(ListCreateAPIView):
#     model = AutoWebinar
#     serializer_class = AutoWebinarSerializer
#     # TODO: change permissions
#     permission_classes = (AllowAny, )
#     queryset = AutoWebinar.objects.all()

class WebinarViewSet(ModelViewSet):
    queryset = Webinar.objects.all()
    serializer_class = WebinarSerializer
    # TODO: change permissions
    permission_classes = (AllowAny, )
    http_method_names = ['get', 'post', 'put', 'delete']

    @action(detail=True, methods=['GET'])
    def user_fake_count(self, request, pk):
        webinar = self.get_object()
        print(webinar.fake_user_count)
        serializer = UserCountSerializer(data={'counter': webinar.fake_user_count})
        if serializer.is_valid():
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(
                {
                    'status':
                        'Problem with calculating "counter". '
                        'Please, check the webinar values "min_fake_user_count" and "max_fake_user_count". '
                        'It must be not None.'
                },
                status.HTTP_204_NO_CONTENT
            )
