from django.db import models
from django.forms import ModelForm
from .models.messagesconf import MessagesConfiguration

class MessagesConfigurationForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'
			
	class Meta:
		model = MessagesConfiguration
		fields = ['name', 'text','configuration_type']




