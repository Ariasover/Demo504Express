"""Messages models."""

# Django
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import admin

# Utilities
from apps.utils.models import HistoryModel

class Messages(HistoryModel,models.Model):
    id_message = models.AutoField(db_column='IdMessage', primary_key=True)
	creation_user = models.ForeignKey(User, models.DO_NOTHING, db_column='CreationUser',related_name='creation_user')  # Field name made lowercase.
	modification_user = models.ForeignKey(User, models.DO_NOTHING, db_column='CreationUser',related_name='modification_user')  # Field name made lowercase.
	message = models.TextField(db_column='Message', blank=True, null=True)  # Field name made lowercase.
    

admin.site.register(Messages)
