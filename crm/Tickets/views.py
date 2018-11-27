from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views import generic

from .models import Tickets, Progress, Tasks
from .form import FormTickets, FormProgress, FormTasks
# Create your views here.

class 