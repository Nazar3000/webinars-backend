from django.conf.urls import url

from . import consumers
from django.urls import path
from . import views

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
    url(r'^ws/chat/(?P<room_name>[^/]+)/get_online/$', consumers.GetOnlineConsumer),
    url(r'^ws/user-list/$', consumers.GetUsersConsumer),
]


urlpatterns = [
    path('', views.index, name='index'),
    path('<room_name>/', views.room, name='room'),
]
