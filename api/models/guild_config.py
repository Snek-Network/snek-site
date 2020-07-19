from django.db import models

from api.models.guild import Guild
from api.models.role import Role
from api.models.utils import ModelReprMixin


class GuildConfig(ModelReprMixin, models.Model):
    """A config for a Discord guild."""
    guild = models.OneToOneField(
        Guild,
        on_delete=models.CASCADE,
        primary_key=True
    )

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
