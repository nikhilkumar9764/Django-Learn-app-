# Generated by Django 4.0.3 on 2022-03-24 20:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_alter_room_options_message_participants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='participants',
        ),
        migrations.AddField(
            model_name='room',
            name='participants',
            field=models.ManyToManyField(related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]
