from django.urls import path, include
from django.views.generic.base import RedirectView
from Users import views

app_name = 'Users'

urlpatterns = [
	path('', views.Index.as_view(), name='Index_Tickets_view'),
	path('Create_User', views.Create_User.as_view(), name='Create_User_view'),
	path('Edit_User/<str:pk>', views.Edit_User.as_view(), name='Edit_User_view'),
	path('Delete_User/<str:pk>', views.Delete_User.as_view(), name='Delete_User_view'),
]