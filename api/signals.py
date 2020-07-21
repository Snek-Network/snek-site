from django.db.models.signals import post_save
from django.dispatch import receiver

from api.models.guild import Guild
from api.models.guild_config import GuildConfig


@receiver(post_save, sender=Guild)
def create_guild_config(sender, instance, created, **kwargs):
    if created:
        GuildConfig.objects.create(guild=instance)


@receiver(post_save, sender=Guild)
def save_guild_config(sender, instance, **kwargs):
    instance.config.save()
