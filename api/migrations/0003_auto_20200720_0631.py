# Generated by Django 3.0.8 on 2020-07-20 06:31

import api.models.utils
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_guildconfig'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time of the creation of an infraction.')),
                ('expires_at', models.DateTimeField(help_text='The date and time of the expiration of an infraction. This is null if the infraction is permanent.', null=True)),
                ('active', models.BooleanField(help_text='Whether or not an infraction is active.')),
                ('type', models.CharField(choices=[('note', 'Note'), ('warning', 'Warning'), ('force_nick', 'Forced Nickname'), ('watch', 'Watch'), ('mute', 'Mute'), ('kick', 'Kick'), ('ban', 'Ban')], help_text='The type of infraction.', max_length=10)),
                ('reason', models.TextField(help_text='The reason for an infraction.', null=True)),
                ('hidden', models.BooleanField(default=False, help_text='Whether or not an infraction is a shadow infraction.')),
                ('actor', models.ForeignKey(help_text='The user who gave an infraction.', on_delete=django.db.models.deletion.CASCADE, related_name='infractions_given', to='api.User')),
                ('guild', models.ForeignKey(help_text='The guild an infraction was given in.', on_delete=django.db.models.deletion.CASCADE, to='api.Guild')),
                ('user', models.ForeignKey(help_text='The target user of an infraction.', on_delete=django.db.models.deletion.CASCADE, related_name='infractions_received', to='api.User')),
            ],
            options={
                'ordering': ['-created_at'],
            },
            bases=(api.models.utils.ModelReprMixin, models.Model),
        ),
        migrations.AddConstraint(
            model_name='infraction',
            constraint=models.UniqueConstraint(condition=models.Q(active=True), fields=('guild', 'user', 'type'), name='unique_active_infraction_per_type_per_user_per_guild'),
        ),
    ]
