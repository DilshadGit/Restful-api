from django.conf.urls import include, url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
	url(r'^create/$', views.TutorAPIView.as_view(), name='create'),
	url(r'^list/$', views.TutorListView.as_view(), name='list'),
	url(r'^(?P<pk>[0-9]+)/$', views.TutorView.as_view(), name='tutor-detail'),
]