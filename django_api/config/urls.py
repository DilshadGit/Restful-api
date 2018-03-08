from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from posts import views

from posts.views import UserViewSet, GroupViewSet
from rest_framework.urlpatterns import format_suffix_patterns



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
urlpatterns = router.urls


urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^post/', include('posts.urls')),
    url(r'^student/', include('students.urls')),
    url(r'^university/', include('universities.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
