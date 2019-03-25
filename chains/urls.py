from django.urls import path
from rest_framework_nested import routers

from projects.views import ProjectViewSet
from . import views

router = routers.SimpleRouter()
router.register(r'', ProjectViewSet, base_name='Project')

projects_router = routers.NestedSimpleRouter(router, r'', lookup='project')
projects_router.register(r'chains', views.MessagesChainViewSet, base_name='MessagesChain')

chains_router = routers.NestedSimpleRouter(projects_router, r'chains', lookup='chain')
chains_router.register(r'messages', views.MessageViewSet, base_name='Message')

urlpatterns = projects_router.urls + chains_router.urls
urlpatterns += [
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
