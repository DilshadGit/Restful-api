from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

from utils.lang import LEXERS, LANGUAGE_CHOICES, STYLE_CHOICES


class Developer(models.Model):
	title 		= models.CharField(max_length=80, blank=True, null=True)
	owner 		= models.ForeignKey('auth.User', related_name='deverlopers', on_delete=models.CASCADE)
	highlighted = models.TextField()
	content 	= models.TextField()
	code 		= models.TextField()
	linenos 	= models.BooleanField(default=False)
	language 	= models.CharField(max_length=100, choices=LANGUAGE_CHOICES, default='python')
	style 		= models.CharField(max_length=100, choices=STYLE_CHOICES, default='friendly')
	created 	= models.DateTimeField(auto_now_add=True)


	class Meta:
		ordering = ('created',)

	def __str__(self):
		return self.title

	# Use the `pygments` library to create a highlighted HTML and pygments code highlighting library.
	def save(self, *args, **kwargs):
		lexer 				= get_lexer_by_name(self.language)
		linenos 			= self.linenos and 'table' or False
		options 			= self.title and {'title': self.title} or {}
		formatter 			= HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
		self.highlighted 	= highlight(self.code, lexer, formatter)
		super(Developer, self).save(*args, **kwargs)
	