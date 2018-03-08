from django.contrib.auth.models import User, Group
from rest_framework import serializers, viewsets

from utils.lang import LEXERS, LANGUAGE_CHOICES, STYLE_CHOICES

from .models import Post


## This is login part
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User 
		fields = (
				'url',
				'username', 
				'email', 
				'is_staff', 
				'groups', 
				'date_joined',
				'is_superuser'
			)


# we create Group Serializer to tell each user level
class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group 
		fields = ('url', 'name')


class PostSerializer(serializers.ModelSerializer):
	id 			= serializers.IntegerField(read_only=True)
	title 		= serializers.CharField(max_length=100, required=False, allow_blank=True)
	author 		= serializers.CharField(max_length=100, required=False, allow_blank=True)
	content 	= serializers.CharField(style={'content_template': 'content.html'})
	code 		= serializers.CharField(style={'code_template': 'textarea.html'})
	linenos 	= serializers.BooleanField(required=False)
	language 	= serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
	style 		= serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')


	class Meta:
		model = Post
		# fields = '__all__' 
		# or
		fields = ('id', 'title', 'author', 'content', 'code', 'linenos', 'language', 'style')


	def create(self, validated_data):
		posts = Post.objects.create(**validated_data)
		return posts

	def edit(self, instance, validated_data):
		instance.title 		= validated_data.get('title', instance.title) 
		instance.author 	= validated_data.get('author', instance.author) 
		instance.content 	= validated_data.get('content', instance.content) 
		instance.code 		= validated_data.get('code', instance.code) 
		instance.linenos 	= validated_data.get('linenos', instance.linenos) 
		instance.language 	= validated_data.get('language', instance.language) 
		instance.style 		= validated_data.get('style', instance.style) 

		instance.save()
		return instance

