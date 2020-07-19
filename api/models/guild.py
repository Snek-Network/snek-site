from django.core.validators import MinValueValidator
from django.db import models

from api.models.role import Role
from api.models.utils import ModelReprMixin


class Guild(ModelReprMixin, models.Model):
    """A Discord guild."""
    id = models.PositiveIntegerField(
        primary_key=True,
        validators=(
            MinValueValidator(
                limit_value=0,
                message='Guild IDs cannot be negative.'
            ),
        ),
        help_text='The ID of a Discord guild.'
    )

    name = models.CharField(
        max_length=100,
        help_text='The name of a Discord guild.'
    )

    icon_url = models.URLField(
        help_text="The URL of a guild's icon."
    )

    config = models.OneToOneField(
        GuildConfig,
        on_delete=models.SET_DEFAULT,
        default=GuildConfig,
        help_text='The config for a guild.'
    )


class GuildConfig(ModelReprMixin, models.Model):
    """A config for a Discord guild."""
    mod_role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        help_text='The moderator role of a guild.'
    )

    admin_role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        help_text='The administrator role of a guild.'
    )
