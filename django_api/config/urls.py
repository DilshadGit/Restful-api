from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from posts import views

from posts.views import UserViewSet, GroupViewSet


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = router.urls


urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
    url(r'', include(router.urls)),
    url(r'^dev/', include('developers.urls', namespace='developers')),
    url(r'^post/', include('posts.urls', namespace='posts')),
    url(r'^student/', include('students.urls', namespace='students')),
    url(r'^tutor/', include('tutors.urls', namespace='tutors')),
    url(r'^university/', include('universities.urls', namespace='universities')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
