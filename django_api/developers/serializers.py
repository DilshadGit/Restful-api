from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Developer


class UserSerializer(serializers.ModelSerializer):
	developers 	= serializers.PrimaryKeyRelatedField(queryset=Developer.objects.all(), many=True)

	class Meta:
		model  = User 
		fields = ('id', 'username', 'developers')


class DeveloperSerializer(serializers.ModelSerializer):

	class Meta:
		model  = Developer
		fields = (
				'id', 
				'title', 
				'owner', 
				'highlighted', 
				'content', 
				'code', 
				'linenos', 
				'language', 
				'style'
			)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
