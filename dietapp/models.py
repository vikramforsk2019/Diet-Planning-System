from django.db import models
import os
from django.utils import timezone
from accounts.models import Signup
from django.urls import reverse
class Health_data(models.Model):
	author=models.ForeignKey(Signup, on_delete=models.CASCADE, default=None)
	group= models.CharField(max_length=30)
	gender= models.CharField(max_length=30)
	title= models.CharField(max_length=225)
	des= models.CharField(max_length=225)
	age= models.IntegerField()
	weight=models.IntegerField()
	postfile=models.FileField()
	date = models.DateTimeField(default=timezone.now, editable=False)
	post_views=models.IntegerField(default=0)
	class Meta:
		db_table="health_data" 
	def __str__(self):
		return self.author.uname
	def get_absolute_url(self):
		return reverse('dietapp:cat',kwargs={'username': self.author.uname})
	