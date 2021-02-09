from django.db import models
from django.forms import ModelForm,Form
from .models.speech import MessagesConfiguration

from django import forms

class MessagesConfigurationForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'


	class Meta:
		model = MessagesConfiguration
		fields = ['name', 'text','configuration_type']
		labels = {
			'name': 'Nombre',
			'text': 'Mensaje',
			'configuration_type': 'Tipo de cobro',
		}
