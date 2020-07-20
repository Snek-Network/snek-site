from django.db import models
from django.utils import timezone

from api.models.guild import Guild
from api.models.user import User
from api.models.utils import ModelReprMixin


class Infraction(ModelReprMixin, models.Model):
    """An infraction for a Discord user."""
    INFRACTION_TYPES = (
        ('note', 'Note'),
        ('warning', 'Warning'),
        ('force_nick', 'Forced Nickname'),
        ('watch', 'Watch'),
        ('mute', 'Mute'),
        ('kick', 'Kick'),
        ('ban', 'Ban')
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        help_text='The date and time of the creation of an infraction.'
    )

    expires_at = models.DateTimeField(
        null=True,
        help_text=(
            'The date and time of the expiration of an infraction. '
            'This is null if the infraction is permanent.'
        )
    )

    active = models.BooleanField(
        help_text='Whether or not an infraction is active.'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='infractions_received',
        help_text='The target user of an infraction.'
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.CASCADE,
        help_text='The guild an infraction was given in.'
    )

    actor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='infractions_given',
        help_text='The user who gave an infraction.'
    )

    type = models.CharField(
        choices=INFRACTION_TYPES,
        help_text='The type of infraction.'
    )

    reason = models.TextField(
        null=True,
        help_text='The reason for an infraction.'
    )

    hidden = models.BooleanField(
        default=False,
        help_text='Whether or not an infraction is a shadow infraction.'
    )

    class Meta:
        ordering = ['-inserted_at']
        constraints = (
            models.UniqueConstraint(
                fields=['guild', 'user', 'type'],
                condition=models.Q(active=True),
                name='unique_active_infraction_per_type_per_user_per_guild'
            ),
        )
