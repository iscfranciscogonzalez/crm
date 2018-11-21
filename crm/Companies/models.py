from django.db import models

# Create your models here.
class Companies(models.Model):
	cmp_id = models.AutoField(primary_key=True)
	cmp_name = models.CharField(max_length=256, null=False)
	cmp_address = models.CharField(max_length=256, null=False)
	cmp_city = models.CharField(max_length=256, null=False)
	cmp_state = models.CharField(max_length=256, null=False)
	cmp_postalCode = models.CharField(max_length=256, null=False)
	cmp_phone = models.CharField(max_length=14, null=False)
	cmp_email = models.CharField(max_length=256, null=False)

	def __str__(self):
		return self.cpc_name

class Contacts(models.Model):
	cpc_id = models.AutoField(primary_key=True)  
	cpc_cmp_id = models.ForeignKey('Companies', on_delete=models.CASCADE)
	cpc_departament = models.CharField(max_length=256, null=False)
	cpc_name = models.CharField(max_length=256, null=False)
	cpc_email = models.CharField(max_length=256, null=False)
	cpc_phone = models.CharField(max_length=256, null=False)
