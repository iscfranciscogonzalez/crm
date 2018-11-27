from django.urls import path
from django.views.generic.base import RedirectView
from Companies import views

app_name='Companies'

urlpatterns = [
	path('', views.Index.as_view(), name='Index_Companies_view'),
]