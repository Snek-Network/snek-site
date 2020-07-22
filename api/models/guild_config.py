from django.db import models

from api.models.guild import Guild
from api.models.role import Role
from api.models.utils import ModelReprMixin


class GuildConfig(ModelReprMixin, models.Model):
    """A config for a Discord guild."""
    guild = models.OneToOneField(
        Guild,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='config'
    )

    mod_role = models.OneToOneField(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        related_name='mod_in_guild_config',
        help_text='The moderator role of a guild.'
    )

    admin_role = models.OneToOneField(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        related_name='admin_in_guild_config',
        help_text='The administrator role of a guild.'
    )
