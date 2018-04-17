from django.conf.urls import url
from . import views

urlpatterns = [
    	url(r'^$', views.thing_list, name='thing_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.thing_detail, name='thing_detail'),
]
