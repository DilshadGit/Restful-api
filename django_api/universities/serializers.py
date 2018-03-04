from rest_framework import serializers

from utils.lang import UNI_DEPARTMENT

from .models import University


class UniversitySerializer(serializers.ModelSerializer):
	name 		= serializers.CharField(max_length=80, required=False, allow_blank=True)
	department 	= serializers.ChoiceField(choices=UNI_DEPARTMENT)
	content 	= serializers.CharField(style={'content_template': 'uni.html'})

	class Meta:
		model = University
		fields = '__all__'


	def create(self, validated_data):
		universities = University.objects.create(**validated_data)
		return universities

	def edit(self, instance, validated_data):
		instance.name 		= validated_data.get('name', instance.name) 
		instance.department = validated_data.get('department', instance.department) 
		instance.content 	= validated_data.get('content', instance.content) 
		
		instance.save()
		return instance