"""Messages models."""

# Django
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import admin

# Utilities
from apps.utils.models import HistoryModel

class MessagesList(HistoryModel,models.Model):
	# id_message_list = models.AutoField(db_column='IdMessage', primary_key=True)
	name = models.TextField(db_column='Name', blank=True, null=True)
	phone = models.CharField(db_column='Phone', max_length=20, blank=True, null=True)
	message = models.TextField(db_column='Message', blank=True, null=True)
	status = models.BooleanField(db_column='Status', blank=True, null=True,default=0)
	creation_user = models.ForeignKey(User, models.DO_NOTHING, db_column='CreationUser',related_name='creation_user')
	modification_user = models.ForeignKey(User, models.DO_NOTHING, db_column='ModificationUser',related_name='modification_user')
	
class MessagesConfiguration(HistoryModel,models.Model):
	id_message_configuration = models.AutoField(db_column='IdMessageConfiguration', primary_key=True)
	text = models.TextField(db_column='Text', blank=True, null=True)
	value = models.IntegerField(db_column='Value', blank=True, null=True)
	creation_user = models.ForeignKey(User, models.DO_NOTHING, db_column='CreationUser',related_name='mc_creation_user')
	modification_user = models.ForeignKey(User, models.DO_NOTHING, db_column='ModificationUser',related_name='mc_modification_user')
	

# admin.site.register(MessagesList)
admin.site.register(MessagesConfiguration)
