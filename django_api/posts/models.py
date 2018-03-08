from django.db import models
from utils.lang import LEXERS, LANGUAGE_CHOICES, STYLE_CHOICES


class Post(models.Model):
	title 		= models.CharField(max_length=80, blank=True, null=True)
	author 		= models.CharField(max_length=80, blank=True, null=True)
	content 	= models.TextField()
	code 		= models.TextField()
	lineone 	= models.BooleanField(default=False)
	language 	= models.CharField(max_length=100, choices=LANGUAGE_CHOICES, default='python')
	style 		= models.CharField(max_length=100, choices=STYLE_CHOICES, default='friendly')
	created 	= models.DateTimeField(auto_now_add=True)


	class Meta:
		ordering = ('created',)

	def __str__(self):
		return self.title
