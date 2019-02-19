from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, PasswordResetSerializer, PasswordResetConfirm, UserUpdateSerializer, \
    CreditCardProfile, CreditCardProfileSerializer, UserProfile, UserProfileSerializer, PasswordChangeSerializer
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

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
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()


class CreditCardProfileView(ListCreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    model = CreditCardProfile
    serializer_class = CreditCardProfileSerializer

    def get_queryset(self):
        queryset = CreditCardProfile.objects.all()
        user = self.kwargs.get('user_id')
        if user:
            queryset = queryset.filter(user=user)
        return queryset


class CreditCardProfileUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = CreditCardProfileSerializer
    queryset = CreditCardProfile.objects.all()


@api_view()
def activate_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None:
        user.is_active = True
        user.save()
        return Response('Thank you for your email confirmation. Now you can login your account.',
                        status=status.HTTP_200_OK)
    else:
        return Response('User does not exist!', status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(ListCreateAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (permissions.AllowAny,)
    model = UserProfile
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        queryset = UserProfile.objects.all()
        user = self.kwargs.get('user_id')
        if user:
            queryset = queryset.filter(user=user)
        return queryset


class UserProfileRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    # authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class PasswordChangeView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = PasswordChangeSerializer

    def get_object(self):
        return User.objects.get(pk=self.kwargs.get('user_id'))

    def put(self, request, user_id):
        self.object = self.get_object()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"old_password": ["Wrong password."]},
                                status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response('Password for {} has been succesfully changed'.format(self.object),
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
