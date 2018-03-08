from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import University
from .serializers import UniversitySerializer


@api_view(['GET', 'POST'])
def uni_list(request, format=None):

	if request.method == 'GET':
		universities = University.objects.all()
		serializer = UniversitySerializer(universities, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = UniversitySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def uni_detail(request, pk, format=None):
	# check if the data we need is exisit if not return Http404 where we return HTTP_404_NOT_FOUND
	try:
		uni = University.objects.get(pk=pk)
	except University.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	# retrienve detail
	if request.method == 'GET':
		serliazer = UniversitySerializer(uni)
		return Response(serliazer.data)
	# update detail
	elif request.method == 'PUT':
		serializer = UniversitySerializer(uni, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	#delete detail
	elif request.method == 'DELETE':
		serializer.delete()
		return Response(status=status.HTTP_204_NOT_CONTENT)
