from django.conf.urls import url

from posts import views


urlpatterns = [
    url(r'^list/$', views.post_list),
    url(r'^(?P<pk>[0-9]+)/$', views.post_detail),
]
