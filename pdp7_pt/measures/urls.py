from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^measurement/(?P<series>[0-9]+)/$', views.measurement, name='measurement'),
]