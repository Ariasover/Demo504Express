# Generated by Django 3.1.3 on 2020-12-01 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messagesconf', '0005_auto_20201201_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='messageslist',
            name='weight_greather',
            field=models.CharField(blank=True, db_column='WeightGreather', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='messageslist',
            name='weight_type',
            field=models.CharField(blank=True, db_column='WeightType', max_length=20, null=True),
        ),
    ]
