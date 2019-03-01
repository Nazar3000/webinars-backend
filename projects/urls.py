from projects import views
from rest_framework_nested import routers

app_name = 'projects'

router = routers.SimpleRouter()
router.register(r'', views.ProjectViewSet, base_name='Project')

projects_router = routers.NestedSimpleRouter(router, r'', lookup='project')
projects_router.register(r'webinars', views.WebinarViewSet, base_name='Webinar')

webinars_router = routers.NestedSimpleRouter(projects_router, r'webinars', lookup='webinar')
webinars_router.register(r'fake_messages', views.FakeChatMessageViewSet, base_name='WebinarFakeChatMessage')

urlpatterns = router.urls + projects_router.urls + webinars_router.urls
