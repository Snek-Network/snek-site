# Generated by Django 3.0.8 on 2020-07-21 22:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200720_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='id',
            field=models.BigIntegerField(help_text='The ID of a Discord guild.', primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(limit_value=0, message='Guild IDs cannot be negative.')]),
        ),
        migrations.AlterField(
            model_name='role',
            name='id',
            field=models.BigIntegerField(help_text='The ID of a Discord role.', primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(limit_value=0, message='Guild IDs cannot be negative.')]),
        ),
    ]