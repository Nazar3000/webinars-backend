from projects import views
from rest_framework import routers

app_name = 'projects'

router = routers.DefaultRouter()

router.register('', views.ProjectViewSet, base_name='Project')
router.register('webinars', views.WebinarViewSet)
router.register('webinars/fake_messages', views.FakeChatMessageViewSet, base_name='Project')

urlpatterns = router.urls
