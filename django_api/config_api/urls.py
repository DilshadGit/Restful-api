from django.conf.urls import include, url
from rest_framework import routers
from posts import views

from posts.views import UserViewSet, GroupViewSet, PostListView
# from rest_framework.urlpatterns import format_suffix_patterns



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^posts/$', views.PostListView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
