from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer



# class StudentList(APIView):

# 	def get(self, request, format=None):
# 		students 	= Student.objects.all()
# 		serializer 	= StudentSerializer(students, many=True)
# 		return Response(serializer.data)

# 	def post(self, request, format=None):
# 		serializer = StudentSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class StudentDetail(APIView):

# 	'''
# 		Create the below func for retrieve using GET, update PUT and delete Student
# 	'''
# 	def get_object(self, pk):
# 		try:
# 			return Student.objects.get(pk=pk)
# 		except Student.DoesNotExist:
# 			raise Http404

# 	def get(self, request, pk, format=None):
# 		student = self.get_object(pk)
# 		serializer = StudentSerializer(student)
# 		return Response(serializer.data)

# 	def put(self, request, pk, format=None):
# 		student = self.get_object(pk)
# 		serializer = StudentSerializer(student, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	def delete(self, request, pk, format=None):
# 		student = self.get_object(pk)
# 		student.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)


# to use mixins 
from django.db.models import Q

from rest_framework import mixins
from rest_framework import generics


class StudentList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

	# search field 
	filter_fields = ('name', 'student_id', 'course_title')

	def get_search(self):
		query = self.request.GET.get('q')
		if query is not None:
			qs = qs.filter(Q(name__icontains=query) |
							Q(course_title__icontains=query) |
							Q(student_id__incontains=query)).distinct()
		return  qs


	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class StudentDetail(mixins.RetrieveModelMixin, 
					mixins.UpdateModelMixin, 
					mixins.DestroyModelMixin,
					generics.GenericAPIView
				):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def patch(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

# to user generics
# from rest_framework import generics


# class StudentList(generics.ListCreateAPIView):
# 	queryset = Student.objects.all()
# 	serializer_class = StudentSerializer


# class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Student.objects.all()
# 	serializer_class = StudentSerializer
