from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views import generic

from .models import Tickets, Progress, Tasks
from .form import FormTickets, FormProgress, FormTasks
# Create your views here.

class Index(generic.ListView):
	template_name = "Tickets/index.html"
	queryset = Tickets.objects.all()

	def get_queryset(self, *args, **kwargs):
		qs = Tickets.objects.all()
		print(self.request.GET)
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(Q(tck_id__icontains=query) | Q(tck_name__icontains=query))
		return qs
		
	def get_context_data(self, *args, **kwargs):
		context = super(Index, self).get_context_data(*args, **kwargs)
		context["create_form"] = FormTickets()
		return context

class Create_Ticket(generic.CreateView):
	template_name = 'Tickets/Create_Ticket.html'
	model = Tickets
	form_class = FormTickets
	success_url = "/"

	def get_context_data(self, *args, **kwargs):
		context = super(Index, self).get_context_data(*args, **kwargs)
		context["create_form"] = FormTickets()
		return context

class Edit_Ticket(generic.UpdateView):
	template_name = "Tickets/Edit_Ticket.html"
	model = Tickets
	fields = [""]
	success_url = "/tweet/list_tweet/"

class Delete_Ticket(generic.DeleteView):
	template_name = 'Tickets/.html'
	model = Tickets
	success_url = ''

class Detail_Ticket(generic.DetailView):
	template_name = "Tickets/Detail_Ticket.html"
	#model = Progress
		
	def get_context_data(self, *args, **kwargs):
		context = super(Index, self).get_context_data(*args, **kwargs)
		print(self.kwargs)
		query = self.request.GET.get("q", None)
		context["Progress"] = Progress.objects.filter(tkp_tck_id=query)
		return context

class Create_Task(generic.CreateView):
	template_name = 'Tickets/Create_Task.html'
	model = Tasks
	form_class = FormTasks
	success_url = "/"

	def get_context_data(self, *args, **kwargs):
		context = super(Index, self).get_context_data(*args, **kwargs)
		context["create_form"] = FormTasks()
		return context

class Edit_Task(generic.UpdateView):
	template_name = "Tickets/Edit_Task.html"
	model = Tasks
	fields = [""]
	success_url = "/"

class Delete_Task(generic.DeleteView):
	template_name = 'Tickets/Edit_Task.html'
	model = Tasks
	success_url = '/'

class Create_Ticket_Progress(generic.CreateView):
	template_name = 'Tickets/Create_Ticket_Progress.html'
	model = Tasks
	form_class = FormTasks
	success_url = "/"

	def get_context_data(self, *args, **kwargs):
		context = super(Index, self).get_context_data(*args, **kwargs)
		context["create_form"] = FormProgress()
		return context

class Delete_Ticket_Progress(generic.DeleteView):
	template_name = 'Tickets/Delete_Ticket_Progress.html'
	model = Progress
	success_url = '/'	