# Django
from django import forms

# Django filters
import django_filters

# Models
from .models.speech import *

class OrderFilter(django_filters.FilterSet):
	
	name = django_filters.CharFilter(label="Nombre",widget=forms.TextInput(attrs={ 'class': 'input-sm form-control'}))
	class Meta:
		model = MessagesConfiguration
		fields = ['name']

