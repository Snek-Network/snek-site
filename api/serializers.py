from rest_framework.serializers import ModelSerializer, ValidationError
from rest_framework.validators import UniqueTogetherValidator

from api.models import Guild, GuildConfig, Infraction, Role, User


class GuildSerializer(ModelSerializer):
    """(De-)Serialization of `Guild` instances."""

    class Meta:
        model = Guild
        fields = ('id', 'name', 'icon_url')


class GuildConfigSerializer(ModelSerializer):
    """(De-)Serialization of `GuildConfig` instances."""

    class Meta:
        model = GuildConfig
        fields = ('guild', 'mod_role', 'admin_role')


class InfractionSerializer(ModelSerializer):
    """(De-)Serialization of `Infraction` instances."""

    class Meta:
        model = Infraction
        fields = (
            'id', 'created_at', 'expires_at', 'active', 'user',
            'guild', 'actor', 'type', 'reason', 'hidden'
        )
        validators = [
            UniqueTogetherValidator(
                queryset=Infraction.objects.filter(active=True),
                fields=['guild', 'user', 'type', 'active'],
                message='This user already has an active infraction of this type.'
            )
        ]

    def validate(self, attrs):
        """Validate data constraints for the given data."""
        infr_type = attrs['type']

        active = attrs['active']
        if active and infr_type in ('note', 'warning', 'kick'):
            raise ValidationError({'active': [f'{infr_type} infractions cannot be active.']})

        expires_at = attrs.get('expires_at')
        if expires_at and infr_type in ('kick', 'warning'):
            raise ValidationError({'expires_at': [f'{infr_type} infractions cannot expire.']})

        hidden = attrs.get('hidden')
        if hidden and infr_type in ('force_nick', 'warning'):
            raise ValidationError({'hidden': [f'{infr_type} infractions cannot be hidden.']})

        if not hidden and infr_type in ('note',):
            raise ValidationError({'hidden': [f'{infr_type} infractions must be hidden.']})

        return attrs


class RoleSerializer(ModelSerializer):
    """(De-)Serialization of `Role` instances."""

    class Meta:
        model = Role
        fields = ('id', 'name', 'color', 'permissions', 'position', 'guild')


class UserSerializer(ModelSerializer):
    """(De-)Serialization of `User` instances."""

    class Meta:
        model = User
        fields = ('id', 'name', 'display_name', 'discriminator', 'avatar_url', 'roles', 'guilds')
