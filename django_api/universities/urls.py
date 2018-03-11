from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    url(r'^list/$', views.uni_list, name='uni_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.uni_detail, name='uni-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
