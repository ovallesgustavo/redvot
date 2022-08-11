from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response

from redvot.login.serializers import LoginSerializers, LogoutSerializers

User = get_user_model()


class LoginViewSet(viewsets.ViewSet):
    serializer_class = LoginSerializers
    permission_classes = [permissions.AllowAny]

    def list(self, request, **kwargs):
        service = self.serializer_class(context={'request': request})
        return Response(data=service.get_all())

    def retrieve(self, request, pk=None):
        service = self.serializer_class(pk, context={'request': request})
        return Response(data=service.get_one(pk))

    def create(self, request, format=None, *args, **kwargs):
        service = self.serializer_class(data=request.data, context={'request': request})
        service.is_valid(raise_exception=True)
        service.save()
        return Response(data=service.instance)


class LogoutViewSet(viewsets.ViewSet):

    serializer_class = LogoutSerializers
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, format=None, *args, **kwargs):
        service = self.serializer_class(data=request.data, context={'request': request})
        service.is_valid(raise_exception=True)
        service.save()
        return Response(data=service.instance)
