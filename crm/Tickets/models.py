from django.db import models
from Users.models import Users

# Create your models here.
class Tickets(models.Model):
	tck_id = models.AutoField(primary_key=True)
	tck_name = models.CharField(max_length=256, null=False)
	tck_description = models.TextField(max_length=1000, null=False)
	tck_createDate = models.DateTimeField(auto_now_add=True, null=False)
	tck_startDate = models.DateTimeField(null=False)
	tck_targetDate = models.DateTimeField(null=False)
	tck_finishDate = models.DateTimeField(auto_now=True, null=False)
	tck_usr_inCharge = models.ForeignKey(Users, on_delete=models.CASCADE)

	def __str__(self):
		return self.tck_name

class Progress(models.Model):
	tkp_id = models.AutoField(primary_key=True)
	tkp_tck_id = models.ForeignKey(Tickets, on_delete=models.CASCADE)
	tkp_description = models.TextField(max_length=1000, null=False)
	tkp_date = models.DateTimeField(auto_now_add=True, null=False)

class Tasks(models.Model):
	tsk_id = models.AutoField(primary_key=True)
	tsk_name = models.CharField(max_length=256, null=False)
	tsk_tck_id = models.ForeignKey(Tickets, on_delete=models.CASCADE)
	tsk_createDate = models.DateTimeField(auto_now_add=True, null=False)
	tsk_targetDate = models.DateTimeField(null=False)
	tsk_finishDate = models.DateTimeField(auto_now=True, null=False)


