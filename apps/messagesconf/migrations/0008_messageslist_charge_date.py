# Generated by Django 3.1.4 on 2021-01-13 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messagesconf', '0007_auto_20201201_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='messageslist',
            name='charge_date',
            field=models.DateField(blank=True, db_column='ChargeDate', null=True),
        ),
    ]
