from rest_framework import serializers

from .models import Tutor

'''
 What the serializers does convert to json and valides for the data passed
'''
class TutorSerializer(serializers.ModelSerializer):

	# url = serializers.HyperlinkedIdentityField(view_name='tutors:tutor-detail')

	class Meta:
		model = Tutor 
		fields = ('pk', 'name', 'university', 'subject', 'created_date')
		# if we want to make some field not be touchable we will use 
		# read_only_fields and name of the field name  or university or another
		read_only_fields = ['name']

	'''
	Now create func to tell the user that you can't create new user but not be the some or duplicated 
	name example
	'''
	def validate_name(self, value):
		qset = Tutor.objects.filter(name__iexact=value)

		if self.instance:
			qset = qset.exclude(pk=self.instance.pk)

		if qset.exists():
			raise serializers.ValidationError('The name must be unique')
		return value
