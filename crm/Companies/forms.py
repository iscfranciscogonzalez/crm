from django import forms
from .models import Companies, Contacts

class FormCompanies(forms.ModelForm):
	class Meta:
		model = Companies
		fields = '__all__'

class FormContacts(forms.ModelForm):
	class Meta:
		model = Contacts
		fields = '__all__'