from django.conf.urls import include, url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
	url(r'^list/$', views.DeveloperList.as_view()),
	url(r'^(?P<pk>[0-9]+)/$', views.DeveloperDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
