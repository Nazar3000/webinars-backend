from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class ViberHandlerView(GenericAPIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        return Response(status=status.HTTP_200_OK)
