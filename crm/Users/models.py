from django.db import models
from Departments.models import Departments

# Create your models here.

class UsersTypes(models.Model):
	uty_id = models.AutoField(primary_key=True)
	uty_type = models.CharField(max_length=256, null=False)

	def __str__(self):
		return self.uty_type
		
class Users(models.Model):
	usr_id = models.AutoField(primary_key=True)
	usr_name = models.CharField(max_length=256, null=False)
	usr_lastname = models.CharField(max_length=256, null=False)
	usr_phone = models.CharField(max_length=256, null=False)
	usr_email = models.CharField(max_length=256, null=False)
	usr_address = models.CharField(max_length=256, null=False)
	usr_city = models.CharField(max_length=256, null=False)
	usr_state = models.CharField(max_length=256, null=False)
	usr_uty_id = models.ForeignKey(UsersTypes, on_delete=models.CASCADE)
	usr_dep_id = models.ForeignKey(Departments, on_delete=models.CASCADE)

	def __str__(self):
		return self.usr_name

