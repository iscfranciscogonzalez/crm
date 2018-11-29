from django.urls import path, include
from django.views.generic.base import RedirectView
from Departments import views

app_name = 'Departments'

urlpatterns = [
	path('', views.Index.as_view(), name='Index_Departments_view'),
	path('Create_Department/', views.Create_Department.as_view(), name='Create_Departments_view'),
	path('Edit_Department/<int:pk>', views.Edit_Department.as_view(), name='Edit_Department_view'),
	path('Delete_Department/<int:pk>', views.Delete_Department.as_view(), name='Delete_Departments_view'),
]