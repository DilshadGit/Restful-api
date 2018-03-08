from django.db import models

from utils.lang import UNI_DEPARTMENT


class Student(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	student_id = models.CharField(max_length=9, blank=True, null=True)
	bio = models.TextField(max_length=400)
	course_title = models.CharField(max_length=50, choices=UNI_DEPARTMENT)
	created_date = models.DateTimeField(auto_now_add=True)


	class Meta:
		ordering = ('created_date',)

	def __str__(self):
		return self.name
