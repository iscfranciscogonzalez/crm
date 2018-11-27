from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q

from django.views import generic

# Create your views here.
def Index(request):
	return render(request, 'home/index.html')
