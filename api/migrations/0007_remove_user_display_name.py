# Generated by Django 3.0.8 on 2020-07-22 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200722_0558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='display_name',
        ),
    ]