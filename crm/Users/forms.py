from django import forms
from .models import Users, UsersTypes

class FormUsers(forms.ModelForm):
	class Meta:
		model = Users
		fields = '__all__'

class FormUserTypes
	class Meta:
		model = UsersTypes
		fields = '__all__'