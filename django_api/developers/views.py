from django.contrib.auth.models import User

#test
# from rest_framework import viewsets

from rest_framework import generics
from rest_framework import permissions

from .models import Developer
from .serializers import UserSerializer, DeveloperSerializer
from .permissions import IsOwnerOrReadOnly


class UserList(generics.ListAPIView):
	queryset 			= Developer.objects.all()
	serializer_class 	= UserSerializer


class UserDetail(generics.RetrieveAPIView):
	queryset 			= User.objects.all()
	serializer_class 	= UserSerializer


class DeveloperList(generics.ListAPIView):
	queryset 			= Developer.objects.all()
	serializer_class 	= DeveloperSerializer

	# permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class DeveloperDetail(generics.RetrieveAPIView):
	queryset 			= Developer.objects.all()
	serializer_class 	= DeveloperSerializer

	# permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


# ## for viewset
# class DeveloperView(viewsets.ModelViewSet):
# 	queryset 			= Developer.objects.all()
# 	serializer_class 	= DeveloperSerializer


