from rest_framework.generics import UpdateAPIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, PasswordResetSerializer, PasswordResetConfirm
from rest_framework.generics import CreateAPIView
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

User = get_user_model()


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer


class PasswordResetView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = PasswordResetSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = PasswordResetConfirm

    def put(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            uid = serializer.data['uid']
            uid = force_text(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uid)
            return Response('Password for {} has been succesfully changed'.format(user), status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
