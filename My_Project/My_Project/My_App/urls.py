from django.conf.urls import patterns, url
from My_App import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'))

