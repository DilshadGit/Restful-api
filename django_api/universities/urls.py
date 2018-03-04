from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^list/$', views.uni_list),
    # url(r'^(?P<pk>[0-9]+)/$', views.post_detail),
]
