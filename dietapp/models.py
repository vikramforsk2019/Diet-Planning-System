from django.db import models
import os

class Health_data(models.Model):
	userid=models.IntegerField()
	group= models.CharField(max_length=40)
	age= models.IntegerField()
	weight=models.IntegerField()
	postfile=models.FileField()
	class Meta:
		db_table="health_data" 	
