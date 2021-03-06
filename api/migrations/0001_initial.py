# Generated by Django 3.0.8 on 2020-07-19 06:19

import api.models.utils
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guild',
            fields=[
                ('id', models.PositiveIntegerField(help_text='The ID of a Discord guild.', primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(limit_value=0, message='Guild IDs cannot be negative.')])),
                ('name', models.CharField(help_text='The name of a Discord guild.', max_length=100)),
                ('icon_url', models.URLField(help_text="The URL of a guild's icon.")),
            ],
            bases=(api.models.utils.ModelReprMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.PositiveIntegerField(help_text='The ID of a Discord role.', primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(limit_value=0, message='Guild IDs cannot be negative.')])),
                ('name', models.CharField(help_text='The name of a Discord role.', max_length=100)),
                ('color', models.IntegerField(help_text='The integer value of the color of a role.', validators=[django.core.validators.MinValueValidator(limit_value=0, message='Color hex cannot be negative.')])),
                ('permissions', models.IntegerField(help_text='The integer value of the permission bitset of a role.', validators=[django.core.validators.MinValueValidator(limit_value=0, message='Role permissions cannot be negative.'), django.core.validators.MaxValueValidator(limit_value=8589934592, message='Role permission bitset exceeds value of having all permissions')])),
                ('position', models.IntegerField(help_text='The position of a role in the role hierarchy of a guild.')),
                ('guild', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Guild')),
            ],
            bases=(api.models.utils.ModelReprMixin, models.Model),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigIntegerField(help_text='The ID of a Discord user.', primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(limit_value=0, message='User IDs cannot be negative.')])),
                ('name', models.CharField(help_text='The username of a user.', max_length=32)),
                ('display_name', models.CharField(help_text='The display name of a user.', max_length=32)),
                ('discriminator', models.PositiveSmallIntegerField(help_text='The discriminator of a user.', validators=[django.core.validators.MaxValueValidator(limit_value=9999, message='Discriminators may not exceed 9999.')])),
                ('avatar_url', models.URLField(help_text="The URL of a user's avatar.")),
                ('guilds', models.ManyToManyField(to='api.Guild')),
                ('roles', models.ManyToManyField(to='api.Role')),
            ],
            bases=(api.models.utils.ModelReprMixin, models.Model),
        ),
    ]
