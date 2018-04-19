from django.conf.urls import url
from . import views

urlpatterns = [
    	url(r'^$', views.thing_list, name='thing_list'),
	url(r'^thing/(?P<pk>[0-9]+)/$', views.thing_detail, name='thing_detail'),
    	url(r'^thing/new/$', views.thing_new, name='thing_new'),
        url(r'^thing/(?P<pk>[0-9]+)/edit/$', views.thing_edit, name='thing_edit'),


]
