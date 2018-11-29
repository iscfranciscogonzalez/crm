from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q

from django.views import generic

from Companies.models import Companies, Contacts
from .forms import FormCompanies, FormContacts

class Index(generic.ListView):
	template_name = "Companies/index.html"
	queryset = Companies.objects.all()

	def get_queryset(self, *args, **kwargs):
		qs = Companies.objects.all()
		print(self.request.GET)
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(Q(cmp_name=query) | Q(cmp_id=query))
		return qs
		
	def get_context_data(self, *args, **kwargs):
		context = super(Index, self).get_context_data(*args, **kwargs)
		context["create_form"] = FormCompanies()
		return context

class Create_Company(generic.CreateView):
	template_name = 'Companies/Create_Company.html'
	model = Companies
	form_class = FormCompanies
	success_url = "/Companies"

	def get_context_data(self, *args, **kwargs):
		context = super(Create_Company, self).get_context_data(*args, **kwargs)
		context["create_form"] = FormCompanies()
		return context

class Edit_Company(generic.UpdateView):
	template_name = "Companies/Edit_Company.html"
	model = Companies
	fields = ["cmp_name", "cmp_address", "cmp_city", "cmp_state", "cmp_postalCode", "cmp_phone", "cmp_email"]
	success_url = "/Companies"

class Delete_Company(generic.DeleteView):
	template_name = 'Companies/.html'
	model = Companies
	success_url = ''

class Contacts_List(generic.ListView):
	template_name = "Companies/Contacts_List.html"
	queryset = Contacts.objects.all()

	def get_queryset(self, *args, **kwargs):
		qs = Contacts.objects.all()
		print(self.request.GET)
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(Q(cpc_id=query) | Q(cpc_name=query))
		return qs
		
	def get_context_data(self, *args, **kwargs):
		context = super(Contacts_List, self).get_context_data(*args, **kwargs)
		context["create_form"] = FormContacts()
		return context

class Create_Contact(generic.CreateView):
	template_name = 'Companies/Create_Contact.html'
	model = Contacts
	form_class = FormContacts
	success_url = "/Companies/Contacts"

	def get_context_data(self, *args, **kwargs):
		context = super(Create_Contact, self).get_context_data(*args, **kwargs)
		context["create_form"] = FormContacts()
		return context

class Edit_Contact(generic.UpdateView):
	template_name = "Companies/Edit_Contact.html"
	model = Contacts
	fields = ["cpc_departament", "cpc_name", "cpc_email", "cpc_phone"]
	success_url = "/Companies/Contacts"

class Delete_Contact(generic.DeleteView):
	template_name = 'Companies/Delete_Contact.html'
	model = Contacts
	success_url = '/Companies/Contacts'

