from rest_framework import serializers

from .models import Student
from utils.lang import UNI_DEPARTMENT


class StudentSerializer(serializers.ModelSerializer):
	name 			= serializers.CharField(max_length=100)
	student_id 		= serializers.CharField(max_length=9)
	bio 			= serializers.CharField(style={'template_name': 'content.html'})
	course_title 	= serializers.ChoiceField(choices=UNI_DEPARTMENT)
	

	class Meta:
		model = Student 
		fields = ('name', 'student_id', 'bio', 'course_title')

