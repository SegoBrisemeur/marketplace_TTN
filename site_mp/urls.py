from django.conf.urls import url
from . import views

urlpatterns = [
    	url(r'^$', views.thing_list, name='thing_list'),
	url(r'^thing/(?P<pk>[0-9]+)/$', views.thing_detail, name='thing_detail'),
    	url(r'^thing/new/$', views.thing_new, name='thing_new'),
	url(r'^thing/(?P<uid64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/edit/$', views.thing_edit, name='thing_edit'),
        url(r'^thing/(?P<pk>[0-9]+)/contact/$', views.contact_author, name='contact_author'),


    	#url(r'^thing/(?P<pk>[0-9]+)/delete/$', views.delete_thing, name='delete_thing'),
]
