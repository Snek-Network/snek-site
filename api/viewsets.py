from rest_framework.viewsets import ModelViewSet

from api.models import Guild, GuildConfig, Role, User
from api.serializers import (
    GuildSerializer,
    GuildConfigSerializer,
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


class RoleViewSet(ModelViewSet):
    """View providing CRUD access to the roles stored."""
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class UserViewSet(ModelViewSet):
    """View providing CRUD access to the users stored."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
