# Generated by Django 3.1.4 on 2021-01-27 01:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='ConfigurationType',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('id_configuration_type', models.AutoField(db_column='IdConfigurationType', primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, db_column='Title', max_length=50, null=True)),
                ('creation_user', models.ForeignKey(db_column='CreationUser', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ct_creation_user', to=settings.AUTH_USER_MODEL)),
                ('modification_user', models.ForeignKey(db_column='ModificationUser', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ct_modification_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MessageListStatus',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('id_message_list_status', models.AutoField(db_column='IdMessageListStatus', primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=20, null=True)),
                ('creation_user', models.ForeignKey(db_column='CreationUser', on_delete=django.db.models.deletion.DO_NOTHING, related_name='mls_creation_user', to=settings.AUTH_USER_MODEL)),
                ('modification_user', models.ForeignKey(db_column='ModificationUser', on_delete=django.db.models.deletion.DO_NOTHING, related_name='mls_modification_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MessagesList',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('id_message_list', models.AutoField(db_column='IdMessageList', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('phone', models.CharField(blank=True, db_column='Phone', max_length=20, null=True)),
                ('message', models.TextField(blank=True, db_column='Message', null=True)),
                ('amount', models.FloatField(blank=True, db_column='Amount', max_length=20, null=True)),
                ('departure_date', models.DateField(db_column='DepartureDate')),
                ('weight_greather', models.CharField(blank=True, db_column='WeightGreather', max_length=20, null=True)),
                ('weight_type', models.CharField(blank=True, db_column='WeightType', max_length=20, null=True)),
                ('creation_user', models.ForeignKey(db_column='CreationUser', on_delete=django.db.models.deletion.DO_NOTHING, related_name='creation_user', to=settings.AUTH_USER_MODEL)),
                ('modification_user', models.ForeignKey(db_column='ModificationUser', on_delete=django.db.models.deletion.DO_NOTHING, related_name='modification_user', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(db_column='MessagesListStatus', on_delete=django.db.models.deletion.DO_NOTHING, related_name='message_list_status', to='messagesconf.messageliststatus')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MessagesConfiguration',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('id_message_configuration', models.AutoField(db_column='IdMessageConfiguration', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=50, null=True)),
                ('text', models.TextField(blank=True, db_column='Text', null=True)),
                ('value', models.IntegerField(blank=True, db_column='Value', null=True)),
                ('is_active', models.BooleanField(blank=True, db_column='IsActive', default=0, null=True)),
                ('configuration_type', models.ForeignKey(db_column='ConfigurationType', on_delete=django.db.models.deletion.DO_NOTHING, to='messagesconf.configurationtype')),
                ('creation_user', models.ForeignKey(db_column='CreationUser', on_delete=django.db.models.deletion.DO_NOTHING, related_name='mc_creation_user', to=settings.AUTH_USER_MODEL)),
                ('modification_user', models.ForeignKey(db_column='ModificationUser', on_delete=django.db.models.deletion.DO_NOTHING, related_name='mc_modification_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
