# Generated by Django 3.1.4 on 2021-02-08 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messagesconf', '0003_auto_20210203_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messagesconfiguration',
            name='configuration_type',
        ),
        migrations.RemoveField(
            model_name='messagesconfiguration',
            name='creation_user',
        ),
        migrations.RemoveField(
            model_name='messagesconfiguration',
            name='modification_user',
        ),
        migrations.DeleteModel(
            name='ConfigurationType',
        ),
        migrations.DeleteModel(
            name='MessagesConfiguration',
        ),
    ]
