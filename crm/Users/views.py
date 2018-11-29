from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views import generic
# Create your views here.

from .models import Users
from .forms import FormUsers

class Index(generic.ListView):
	template_name = "Users/index.html"
	queryset = Users.objects.all()

	def get_queryset(self, *args, **kwargs):
		qs = Users.objects.all()
		print(self.request.GET)
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(Q(usr_id__icontains=query) | Q(usr_name__icontains=query))
		return qs
		
	def get_context_data(self, *args, **kwargs):
		context = super(Index, self).get_context_data(*args, **kwargs)
		context["create_form"] = FormUsers()
		return context

class Create_User(generic.CreateView):
	template_name = 'Users/Create_User.html'
	model = Users
	form_class = FormUsers
	success_url = "/Users"

	def get_context_data(self, *args, **kwargs):
		context = super(Create_User, self).get_context_data(*args, **kwargs)
		context["create_form"] = FormUsers()
		return context

class Edit_User(generic.UpdateView):
	template_name = "Users/Edit_User.html"
	model = Users
	fields = ["usr_name", 'usr_lastname', 'usr_phone', 'usr_phone', 'usr_email', 'usr_address', 'usr_city', 'usr_state', 'usr_type', 'usr_dep_id']
	success_url = "/Users"

class Delete_User(generic.DeleteView):
	template_name = 'Users/Delete_User.html'
	model = Users
	success_url = '/Users'
