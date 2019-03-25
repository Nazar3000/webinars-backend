from django.urls import path
from rest_framework_nested import routers

from projects.views import ProjectViewSet
from . import views

router = routers.SimpleRouter()
router.register(r'', ProjectViewSet, base_name='Project')

projects_router = routers.NestedSimpleRouter(router, r'', lookup='project')
projects_router.register(r'chains', views.MessagesChainViewSet, base_name='MessagesChain')

urlpatterns = projects_router.urls
urlpatterns += [
    path('<int:chain_id>/messages/', views.MessageListCreateView.as_view(), name='list_create_message'),
    path(
        'messages/<int:pk>',
        views.MessageRetrieveUpdateDestroyView.as_view(),
        name='retrieve_update_destroy_message'
    ),
    path(
        'messages/user_templates/',
        views.UserTemplateMessageListView.as_view(),
        name='list_user_templates',
    ),
    path(
        'messages/service_templates/',
        views.ServiceTemplateMessageListView.as_view(),
        name='list_service_templates',
    ),
]
