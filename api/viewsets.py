from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models import Guild, GuildConfig, Infraction, Role, User
from api.serializers import (
    GuildSerializer,
    GuildConfigSerializer,
    InfractionSerializer,
    RoleSerializer,
    UserSerializer
)


class GuildViewSet(ModelViewSet):
    """View providing CRUD access to the guilds stored."""
    queryset = Guild.objects.all()
    serializer_class = GuildSerializer


class GuildConfigViewSet(ModelViewSet):
    """View providing CRUD access to the guild configs stored."""
    queryset = GuildConfig.objects.all()
    serializer_class = GuildConfigSerializer


class InfractionViewSet(ModelViewSet):
    """View providing CRUD access to the infractions stored."""
    queryset = Infraction.objects.all()
    serializer_class = InfractionSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    search_fields = ('$reason',)
    filter_fields = ('guild__id', 'user__id', 'actor__id', 'active', 'hidden', 'type')
    frozen_fields = ('id', 'created_at', 'type', 'user', 'guild', 'actor', 'hidden')

    def partial_update(self, request, *args, **kwargs):
        for field in request.data:
            if field in self.frozen_fields:
                raise ValidationError({field: ['This field cannot be updated.']})

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class RoleViewSet(ModelViewSet):
    """View providing CRUD access to the roles stored."""
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class UserViewSet(ModelViewSet):
    """View providing CRUD access to the users stored."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = (DjangoFilterBackend,)

    filter_fields = ('name', 'discriminator')
