from django.urls import path
import chains.views as chain_views


urlpatterns = [
    path('', chain_views.MessageChainListCreateView.as_view(), name='list_create_chain'),
    path(
        '<int:pk>',
        chain_views.MessageChainRetrieveUpdateDestroyView.as_view(), 
        name='retrieve_update_destroy_chain'
    ),
    path('<int:chain_id>/messages/', chain_views.MessageListCreateView.as_view(), name='list_create_message'),
    path(
        'messages/<int:pk>',
        chain_views.MessageRetrieveUpdateDestroyView.as_view(),
        name='retrieve_update_destroy_message'
    ),
    path(
        'messages/user_templates/',
        chain_views.UserTemplateMessageListView.as_view(),
        name='list_user_templates',
    ),
    path(
        'messages/service_templates/',
        chain_views.ServiceTemplateMessageListView.as_view(),
        name='list_service_templates',
    ),
]
