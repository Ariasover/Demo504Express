# Generated by Django 3.1.4 on 2021-01-21 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messagesconf', '0010_errornumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChromeDriverVerification',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('id_chrome_driver_verification', models.AutoField(db_column='IdChromeDriverVerification', primary_key=True, serialize=False)),
                ('version', models.CharField(blank=True, db_column='Version', max_length=100, null=True)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]