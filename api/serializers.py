from rest_framework import serializers

from api.models import Guild, GuildConfig, Role, User


class GuildSerializer(serializers.ModelSerializer):
    """(De-)Serialization of `Guild` instances."""

    class Meta:
        model = Guild
        fields = ('id', 'name', 'icon_url')


class GuildConfigSerializer(serializers.ModelSerializer):
    """(De-)Serialization of `GuildConfig` instances."""

    class Meta:
        model = GuildConfig
        fields = ('guild', 'mod_role', 'admin_role')


class RoleSerializer(serializers.ModelSerializer):
    """(De-)Serialization of `Role` instances."""

    class Meta:
        model = Role
        fields = ('id', 'name', 'color', 'permissions', 'position', 'guild')


class UserSerializer(serializers.ModelSerializer):
    """(De-)Serialization of `User` instances."""

    class Meta:
        model = User
        fields = ('id', 'name', 'display_name', 'discriminator', 'avatar_url', 'roles', 'guilds')
