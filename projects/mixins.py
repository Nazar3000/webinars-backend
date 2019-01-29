from projects.serializers import UserCountSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class WebinarMixin(object):

    @action(detail=True, methods=['get'])
    def user_fake_count(self, request, pk):
        serializer_class = UserCountSerializer
        webinar = self.get_object()
        serializer = serializer_class(data={'counter': webinar.fake_user_count})
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

    @action(detail=True, methods=['put'])
    def activate_chats(self, request, pk):
        serializer_class = self.get_serializer_class()
        webinar = self.get_object()
        serializer = serializer_class(webinar, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({'status': 'Update was successful!'}, status.HTTP_200_OK)
        else:
            return Response({'status': 'Invalid data!'}, status.HTTP_400_BAD_REQUEST)
