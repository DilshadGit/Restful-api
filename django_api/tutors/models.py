from django.db import models

from universities.models import University


class Tutor(models.Model):
	name = models.CharField(max_length=50)
	university = models.ForeignKey(University, on_delete=models.CASCADE)
	subject = models.CharField(max_length=80)
	created_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.name
