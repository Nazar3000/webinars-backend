from django.urls import path
import chains.views as chain_views


urlpatterns = [
    path('messages/', chain_views.MessageListCreateView.as_view(), name='list_create_message'),
    path(
        'messages/<int:pk>',
        chain_views.MessageRetrieveUpdateDestroyView.as_view(),
        name='retrieve_update_destroy_message'
    ),
]
