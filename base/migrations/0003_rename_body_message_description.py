# Generated by Django 4.0.2 on 2022-02-20 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='body',
            new_name='Description',
        ),
    ]