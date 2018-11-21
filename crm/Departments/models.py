from django.db import models

# Create your models here.
class Departments(models.Model):
	dep_id = models.AutoField(primary_key=True)
	dep_name = models.CharField(max_length=256, null=False)

	def __str__(self):
		return self.dep_name