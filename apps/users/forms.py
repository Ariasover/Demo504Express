from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import Group, User


class CustomUserCreationForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	class Meta(UserCreationForm.Meta):
		fields = UserCreationForm.Meta.fields + ("email",'first_name')


class CustomGroupForm(forms.Form):	
	# def __init__(self, *args, **kwargs):
	# 	super(CustomGroupForm, self).__init__(*args, **kwargs)
	# 	for visible in self.visible_fields():
	# 		visible.field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = Group
		fields = '__all__'
		# labels = {
		# 	'name': 'Nombre',
		# 	'text': 'Mensaje',
		# 	'configuration_type': 'Tipo de cobro',
		# }
	# class Meta(UserCreationForm.Meta):
	# 	fields = UserCreationForm.Meta.fields + ("email",'first_name')