from django.core.validators import MinValueValidator
from django.db import models

from api.models.utils import ModelReprMixin


class Guild(ModelReprMixin, models.Model):
    """A Discord guild."""
    id = models.BigIntegerField(
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
