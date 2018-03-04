from django.db import models

from utils.lang import UNI_DEPARTMENT

class University(models.Model):
	name 		= models.CharField(max_length=80)
	department 	= models.CharField(max_length=50, choices=UNI_DEPARTMENT)
	content 	= models.TextField()
	created 	= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name