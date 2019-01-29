from django.urls import path, include
from projects.views import ListCreateProjectView, UpdateProjectActivation, RetrieveUpdateProjectView, \
    WebinarViewSet, AutoWebinarViewSet, WebinarFakeChatMessageListCreateView, AutoWebinarFakeChatMessageListCreateView, \
    WebinarFakeChatMessageUpdateRetrieveDestroyView, AutoWebinarFakeChatMessageUpdateRetrieveDestroyView
from rest_framework import routers

app_name = 'projects'

webinar_router = routers.DefaultRouter()
webinar_router.register('webinar', WebinarViewSet)
webinar_router.register('autowebinar', AutoWebinarViewSet)

urlpatterns = [
    path('', ListCreateProjectView.as_view(), name='list_create_project'),
    path('<int:pk>/', RetrieveUpdateProjectView.as_view()),
    path('activate/<int:pk>/update/', UpdateProjectActivation.as_view(), name='project_activate'),
    path('', include(webinar_router.urls)),
    path('webinar/<int:webinar_id>/fake_messages/',
         WebinarFakeChatMessageListCreateView.as_view(),
         name='list_create_webinar_fake_message'),
    path('webinar/fake_messages/<int:pk>/',
         WebinarFakeChatMessageUpdateRetrieveDestroyView.as_view(),
         name='update_retrieve_destroy_webinar_fake_message'),
    path('autowebinar/<int:autowebinar_id>/fake_messages/',
         AutoWebinarFakeChatMessageListCreateView.as_view(),
         name='list_create_autowebinar_fake_message'),
    path('webinar/fake_messages/<int:pk>/',
         AutoWebinarFakeChatMessageUpdateRetrieveDestroyView.as_view(),
         name='update_retrieve_destroy_autowebinar_fake_message'),
]
