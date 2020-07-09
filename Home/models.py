from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	#auto_now=True          updated dates
	#auto_now_add=True      created dates
	author = models.ForeignKey(User, on_delete=models.CASCADE)				#author can be used to access field values from User table as it's the link between the two tables



	def __str__(self):
		return self.title