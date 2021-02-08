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
	id_message_list = models.AutoField(db_column='IdMessageList', primary_key=True)
	name = models.TextField(db_column='Name', blank=True, null=True)
	phone = models.CharField(db_column='Phone', max_length=20, blank=True, null=True)
	message = models.TextField(db_column='Message', blank=True, null=True)
	amount = models.FloatField(db_column='Amount', max_length=20, blank=True, null=True)
	departure_date = models.CharField(db_column='DepartureDate', max_length=20, blank=True, null=True)
	weight_greather = models.CharField(db_column='WeightGreather',max_length=20, blank=True, null=True)
	weight_type = models.CharField(db_column='WeightType',max_length=20, blank=True, null=True)
	status = models.ForeignKey('MessageListStatus', models.DO_NOTHING, db_column='MessagesListStatus',related_name='message_list_status')
	creation_user = models.ForeignKey(User, models.DO_NOTHING, db_column='CreationUser',related_name='creation_user')
	modification_user = models.ForeignKey(User, models.DO_NOTHING, db_column='ModificationUser',related_name='modification_user')
	
	def __str__(self):
		"""Return Name."""
		return str(self.name)+"-"+str(self.pk)

class MessageListStatus(HistoryModel,models.Model):
	id_message_list_status = models.AutoField(db_column='IdMessageListStatus', primary_key=True)
	description = models.CharField(db_column='Description',max_length=20, blank=True, null=True)
	creation_user = models.ForeignKey(User, models.DO_NOTHING, db_column='CreationUser',related_name='mls_creation_user')
	modification_user = models.ForeignKey(User, models.DO_NOTHING, db_column='ModificationUser',related_name='mls_modification_user')
	
	def __str__(self):
		"""Return Name."""
		return str(self.description)

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

class ErrorNumber(HistoryModel,models.Model):
	id_error_number= models.AutoField(db_column='IdErrorNumber', primary_key=True)
	message_list = models.ForeignKey('MessagesList',on_delete=models.CASCADE, db_column='MessageList')
	creation_user = models.ForeignKey(User, models.DO_NOTHING, db_column='CreationUser',related_name='en_creation_user')
	modification_user = models.ForeignKey(User, models.DO_NOTHING, db_column='ModificationUser',related_name='en_modification_user')
	
	def __str__(self):
		"""Return Name."""
		return str(self.message_list.name)
	

class ChromeDriverVerification(HistoryModel,models.Model):
	id_chrome_driver_verification= models.AutoField(db_column='IdChromeDriverVerification', primary_key=True)
	version = models.CharField(db_column='Version', max_length=100, blank=True, null=True)
	
	def __str__(self):
		"""Return Name."""
		return str(self.version)


admin.site.register(MessagesConfiguration)
admin.site.register(MessagesList)
admin.site.register(MessageListStatus)
admin.site.register(ConfigurationType)
admin.site.register(ErrorNumber)
# admin.site.register(ChromeDriverVerification)
