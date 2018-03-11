from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser 

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView


from rest_framework.response import Response
from rest_framework import status

from .models import Post
from .serializers import PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


'''
We used a POST to the view from clients don't need csrf toek like in django we need to use as
decorator view @csrf_exempt
'''
@csrf_exempt
def post_list(request):
    # retive all data from db as a list as json objects
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)


@csrf_exempt
def post_detail(request, pk):
    
    try:
        post = Post.objects.get(pk=pk)
    # if not exist than 404
    except Post.DoesNotExist:
        return HttpResponse(status=404)
    # retrieve the post with pk
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)

    # update
    elif request.method == 'PUT':
        data = JSONResponse().parse(request)
        serializer = PostSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer, status=400)
    # delete
    elif request.method == 'DELETE':
        post.delete()
        return HttpResponse(status=204)