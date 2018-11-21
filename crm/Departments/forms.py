from django import forms
from .models import Departments

class FormDepartments(forms.ModelForm):
	class Meta:
		model = Departments
		fields = '__all__'