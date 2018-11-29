from django.urls import path, include
from django.views.generic.base import RedirectView
from Tickets import views

app_name = 'Tickets'

urlpatterns = [
	path('', views.Index.as_view(), name='Index_Tickets_view'),
	path('Create_Ticket/', views.Create_Ticket.as_view(), name='Create_Ticket_view'),
	path('Edit_Ticket/', views.Edit_Ticket.as_view(), name='Edit_Ticket_view'),
	path('Delete_Ticket/', views.Delete_Ticket.as_view(), name='Delete_Tickets_view'),
	path('Detail_Ticket/', views.Detail_Ticket.as_view(), name='Detail_Tickets_view'),
	path('Create_Task/', views.Create_Task.as_view(), name='Create_Task_view'),
	path('Edit_Task/', views.Edit_Task.as_view(), name='Edit_Task_view'),
	path('Delete_Task/', views.Delete_Task.as_view(), name='Delete_Task_view'),
	path('Create_Ticket_Progress/', views.Create_Ticket_Progress.as_view(), name='Create_Ticket_Progress_view'),
	path('Delete_Ticket_Progress/', views.Delete_Ticket_Progress.as_view(), name='Delete_Ticket_Progress_view'),
]