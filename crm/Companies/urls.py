from django.urls import path
from django.views.generic.base import RedirectView
from Companies import views

app_name='Companies'

urlpatterns = [
	path('', views.Index.as_view(), name='Index_Companies_view'),
	path('Create_Company', views.Create_Company.as_view(), name='Create_Company_view'),
	path('Edit_Company/<int:pk>', views.Edit_Company.as_view(), name='Index_Companies_view'),
	path('Delete_Company/<int:pk>', views.Delete_Company.as_view(), name='Index_Companies_view'),
	path('Contacts', views.Contacts_List.as_view(), name='Index_Companies_view'),
	path('Create_Contact', views.Create_Contact.as_view(), name='Index_Companies_view'),
	path('Edit_Contact/<int:pk>', views.Edit_Contact.as_view(), name='Index_Companies_view'),
	path('Delete_Contact/<int:pk>', views.Delete_Contact.as_view(), name='Index_Companies_view'),
]