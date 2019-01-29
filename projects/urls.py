from django.urls import path, include
from projects.views import ListCreateProjectView, UpdateProjectActivation, RetrieveUpdateProjectView, \
    WebinarViewSet
from rest_framework import routers

app_name = 'projects'

webinar_router = routers.DefaultRouter()
webinar_router.register('webinar', WebinarViewSet)

urlpatterns = [
    path('', ListCreateProjectView.as_view(), name='list_create_project'),
    path('<int:pk>/', RetrieveUpdateProjectView.as_view()),
    path('activate/<int:pk>/update/', UpdateProjectActivation.as_view(), name='project_activate'),
    path('', include(webinar_router.urls)),
]
