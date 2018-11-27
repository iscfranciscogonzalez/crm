from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views import generic

from .models import Departments
from .form import FormDepartments
# Create your views here.

class Index(generic.ListView):
	template_name = "Departments/index.html"
	queryset = Departments.objects.all()

	def get_queryset(self, *args, **kwargs):
		qs = Departments.objects.all()
		print(self.request.GET)
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(Q(cmp_name__icontains=query) | Q(cmp_id__icontains=query))
		return qs
		
	def get_context_data(self, *args, **kwargs):
		context = super(Index, self).get_context_data(*args, **kwargs)
		context["create_form"] = FormDepartments()
		return context

class Create_Department(generic.CreateView):
	template_name = 'Departments/Create_Department.html'
	model = Departments
	form_class = FormDepartments
	success_url = "/"

	def get_context_data(self, *args, **kwargs):
		context = super(Index, self).get_context_data(*args, **kwargs)
		context["create_form"] = FormDepartments()
			return context

class Edit_Department(generic.UpdateView):
	template_name = "Departments/Edit_Department.html"
	model = Tweet
	fields = [""]
	success_url = "/tweet/list_tweet/"

class Delete_Department(generic.DeleteView):
	template_name = 'Departments/.html'
	model = Articulos
	success_url = ''