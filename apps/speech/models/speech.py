"""Messages models."""

# Django
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import admin

# Utilities
from apps.utils.models import HistoryModel

class ConfigurationType(HistoryModel,models.Model):
	id_configuration_type= models.AutoField(db_column='IdConfigurationType', primary_key=True)
	title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)
	creation_user = models.ForeignKey(User, models.DO_NOTHING, db_column='CreationUser',related_name='ct_creation_user')
	modification_user = models.ForeignKey(User, models.DO_NOTHING, db_column='ModificationUser',related_name='ct_modification_user')

	def __str__(self):
		"""Return title."""
		return self.title
		
class MessagesConfiguration(HistoryModel,models.Model):
	id_message_configuration = models.AutoField(db_column='IdMessageConfiguration', primary_key=True)
	name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)
	text = models.TextField(db_column='Text', blank=True, null=True)
	value = models.IntegerField(db_column='Value', blank=True, null=True)
	is_active = models.BooleanField(db_column='IsActive', blank=True, null=True,default=0)
	configuration_type = models.ForeignKey(ConfigurationType, models.DO_NOTHING, db_column='ConfigurationType')
	creation_user = models.ForeignKey(User, models.DO_NOTHING, db_column='CreationUser',related_name='mc_creation_user')
	modification_user = models.ForeignKey(User, models.DO_NOTHING, db_column='ModificationUser',related_name='mc_modification_user')
	
	def __str__(self):
		"""Return Name."""
		return self.name


admin.site.register(MessagesConfiguration)
admin.site.register(ConfigurationType)
