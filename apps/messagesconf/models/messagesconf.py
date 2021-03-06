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


admin.site.register(MessagesList)
admin.site.register(MessageListStatus)
admin.site.register(ErrorNumber)
# admin.site.register(ChromeDriverVerification)
