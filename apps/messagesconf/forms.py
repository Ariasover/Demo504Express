from django.db import models
from django.forms import ModelForm,Form
from .models.messagesconf import MessagesConfiguration,MessagesList

from django import forms

class OneMessageForm(ModelForm):
	phone = forms.CharField(label='Teléfono', max_length=100)
	message = forms.CharField(label="Mensaje",required=True, widget=forms.Textarea(attrs={'rows': 4, 'cols': 5}))
	configuration_type = forms.ModelChoiceField(label = "Tipo de cobro",queryset=MessagesConfiguration.objects.all())
	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = MessagesList
		fields = ['phone','message','configuration_type']

	

class MessagesConfigurationForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

        
			
	class Meta:
		model = MessagesConfiguration
		fields = ['name', 'text','configuration_type']




