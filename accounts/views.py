from rest_framework import permissions, viewsets, mixins
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import GenericViewSet

from accounts.models import CustomUser
from accounts.serializers import CreateUserSerializer, RetrieveUpdateUserSerializer


class UserViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                   GenericViewSet):

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateUserSerializer
        return RetrieveUpdateUserSerializer


