from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.thing_list, name='thing_list'),
]
