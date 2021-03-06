# Generated by Django 3.0.8 on 2020-07-26 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_user_display_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='guild',
            name='created_at',
            field=models.DateTimeField(help_text='The datetime when a guild was created.', null=True),
        ),
        migrations.AddField(
            model_name='role',
            name='created_at',
            field=models.DateTimeField(help_text='The datetime when a role was created.', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(help_text='The datetime when a user was created.', null=True),
        ),
    ]
