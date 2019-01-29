from rest_framework.permissions import AllowAny
from projects.serializers import UserCountSerializer, WebinarChatActivateSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class WebinarMixin(object):
    serializer_active_chats = None

    @action(detail=True, methods=['get'], serializer_class=UserCountSerializer)
    def user_fake_count(self, request, pk):
        webinar = self.get_object()
        serializer = self.serializer_class(data={'counter': webinar.fake_user_count})
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

    @action(detail=True, methods=['put'], serializer_class=WebinarChatActivateSerializer)
    def activate_chats(self, request, pk):
        webinar = self.get_object()
        serializer = self.serializer_active_chats(webinar, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({'status', 'Update was successful!'}, status.HTTP_200_OK)
        else:
            return Response({'status': 'Invalid data!'}, status.HTTP_400_BAD_REQUEST)
