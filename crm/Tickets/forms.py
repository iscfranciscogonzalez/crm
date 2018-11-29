from django import forms
from .models import Tickets, Progress, Tasks

class FormTickets(forms.ModelForm):
	class Meta:
		model = Tickets
		fields = '__all__'

class FormProgress(forms.ModelForm):
	class Meta:
		model = Progress
		fields = '__all__'

class FormTasks(forms.ModelForm):
	class Meta:
		model = Tasks
		fields = '__all__'