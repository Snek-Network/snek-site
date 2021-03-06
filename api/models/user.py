from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from api.models.guild import Guild
from api.models.role import Role
from api.models.utils import ModelReprMixin


class User(ModelReprMixin, models.Model):
    """A Discord user."""
    id = models.BigIntegerField(
        primary_key=True,
        validators=(
            MinValueValidator(
                limit_value=0,
                message='User IDs cannot be negative.'
            ),
        ),
        help_text='The ID of a Discord user.'
    )

    name = models.CharField(
        max_length=32,
        help_text='The username of a user.'
    )

    discriminator = models.PositiveSmallIntegerField(
        validators=(
            MaxValueValidator(
                limit_value=9999,
                message='Discriminators may not exceed 9999.'
            ),
        ),
        help_text='The discriminator of a user.'
    )

    created_at = models.DateTimeField(
        help_text='The datetime when a user was created.'
    )

    avatar_url = models.URLField(
        help_text="The URL of a user's avatar."
    )

    roles = models.ManyToManyField(Role, blank=True)
    guilds = models.ManyToManyField(Guild, blank=True)

    def __str__(self):
        return f"{self.name}#{self.discriminator}"

    def top_role(self, guild) -> Role:
        """Returns the ID of a user's top role."""
        roles = self.roles.filter(guild__id=guild.id)

        if not roles:
            # The ID of @everyone is the guild's ID
            return Role.objects.get(id=guild.id)

        return max(roles)
