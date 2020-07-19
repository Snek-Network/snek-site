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

    display_name = models.CharField(
        max_length=32,
        help_text='The display name of a user.'
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

    avatar_url = models.URLField(
        help_text="The URL of a user's avatar."
    )

    roles = models.ManyToManyField(Role)
    guilds = models.ManyToManyField(Guild)

    def __str__(self):
        return f"{self.name}#{self.discriminator}"

    def top_role(self, guild_id) -> Role:
        """Returns the ID of a user's top role."""
        roles = self.roles.filter(guild__id=guild_id)

        if not roles:
            return guild_id

        return max(roles).id
