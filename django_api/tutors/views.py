from rest_framework import generics

from .models import Tutor
from .serializers import TutorSerializer


class TutorListView(generics.ListCreateAPIView):
	queryset = Tutor.objects.all()
	serializer_class = TutorSerializer


class TutorAPIView(generics.CreateAPIView):
	lookup_field = 'pk'
	serializer_class = TutorSerializer

	def get_queryset(self):
		return Tutor.objects.all()

	'''
	 Here we have created a function to add the user name before this function not able to add the user
	 name so create a function to allowed us to add the user name. 
	'''
	def perform_create(self, serializer):
		serializer.save(user=self.request.user)



class TutorView(generics.RetrieveUpdateDestroyAPIView):
	lookup_fields = 'pk'
	serializer_class = TutorSerializer

	def get_queryset(self):
		return Tutor.objects.all()

	# def get_object(self):
	# 	pk = Tutor.objects.get(pk=pk)
	# 	return pk
