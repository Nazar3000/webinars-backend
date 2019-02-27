import base64

from projects.serializers import UserCountSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
import django.contrib.auth.password_validation as validators
from django.core import exceptions
from rest_framework import serializers


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


class UserSerializerMixin:
    def validate(self, data):
        password = data.get('password')
        if password:
            errors = dict()
            try:
                validators.validate_password(password=password)
            except exceptions.ValidationError as e:
                errors['password'] = list(e.messages)
            if errors:
                raise serializers.ValidationError(errors)
            if data.get('password') != data.get('confirm_password'):
                errors['password'] = "The two password fields didn't match."
                raise serializers.ValidationError(errors)
        return super().validate(data)


class RequireTogetherFields:
    REQUIRED_TOGETHER = tuple()

    def validate(self, data):
        for field in self.REQUIRED_TOGETHER:
            if field not in self.fields.keys():
                raise serializers.ValidationError('Field {} is not specified.'.format(field))

        data_values = [data.get(key) for key in self.REQUIRED_TOGETHER]
        if not all(data_values) and any(data_values):
            raise serializers.ValidationError('Fields ' + ', '.join(self.REQUIRED_TOGETHER) + ' are required together.')
        return super().validate(data)
