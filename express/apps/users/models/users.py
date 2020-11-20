"""Users models."""

# Django
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import admin

# Utilities
from apps.utils.models import HistoryModel

class Profile(HistoryModel,models.Model):
    id_profile = models.AutoField(db_column='IdProfile', primary_key=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


admin.site.register(Profile)
