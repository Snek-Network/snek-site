from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from api.models.guild import Guild
from api.models.utils import ModelReprMixin


class Role(ModelReprMixin, models.Model):
    """A Discord role."""
    id = models.PositiveIntegerField(
        primary_key=True,
        validators=(
            MinValueValidator(
                limit_value=0,
                message='Guild IDs cannot be negative.'
            ),
        ),
        help_text='The ID of a Discord role.'
    )

    name = models.CharField(
        max_length=100,
        help_text='The name of a Discord role.'
    )

    color = models.IntegerField(
        validators=(
            MinValueValidator(
                limit_value=0,
                message='Color hex cannot be negative.'
            ),
        ),
        help_text='The integer value of the color of a role.'
    )

    permissions = models.IntegerField(
        validators=(
            MinValueValidator(
                limit_value=0,
                message="Role permissions cannot be negative."
            ),
            MaxValueValidator(
                limit_value=2 << 32,
                message="Role permission bitset exceeds value of having all permissions"
            )
        ),
        help_text="The integer value of the permission bitset of a role."
    )
    position = models.IntegerField(
        help_text="The position of a role in the role hierarchy of a guild."
    )

    guild = models.ForeignKey(Guild, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.position < other.position
    
    def __le__(self, other):
        return self.position <= other.position
