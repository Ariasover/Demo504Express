# Generated by Django 3.1.3 on 2020-11-28 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messagesconf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagesconfiguration',
            name='is_active',
            field=models.IntegerField(blank=True, db_column='IsActive', null=True),
        ),
    ]
