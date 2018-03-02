from django.db import models
from utils.lang import LEXERS, LANGUAGE_CHOICES, STYLE_CHOICES


class Post(models.Model):
	title = models.CharField(max_length=80)
	author = models.CharField(max_length=80)
	content = models.TextField()
	code = models.TextField()
	lineone = models.BooleanField(default=False)
	language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES, default='python')
	style = models.CharField(max_length=100, choices=STYLE_CHOICES, default='friendly')
	# image = models.ImageField()
	created = models.DateTimeField()


	class Meta:
		ordering = ('created',)

	def __str__(self):
		return self.title + self.created 
