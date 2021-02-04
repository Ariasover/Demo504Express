from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	class Meta(UserCreationForm.Meta):
		fields = UserCreationForm.Meta.fields + ("email",'first_name')