# Generated by Django 3.1.3 on 2020-11-26 18:08

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
            name='MessagesList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('phone', models.CharField(blank=True, db_column='Phone', max_length=20, null=True)),
                ('message', models.TextField(blank=True, db_column='Message', null=True)),
                ('status', models.BooleanField(blank=True, db_column='Status', default=0, null=True)),
                ('creation_user', models.ForeignKey(db_column='CreationUser', on_delete=django.db.models.deletion.DO_NOTHING, related_name='creation_user', to=settings.AUTH_USER_MODEL)),
                ('modification_user', models.ForeignKey(db_column='ModificationUser', on_delete=django.db.models.deletion.DO_NOTHING, related_name='modification_user', to=settings.AUTH_USER_MODEL)),
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
                ('text', models.CharField(blank=True, db_column='Text', max_length=10, null=True)),
                ('value', models.IntegerField(blank=True, db_column='Value', null=True)),
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
