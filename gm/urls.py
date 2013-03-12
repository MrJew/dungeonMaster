from django.conf.urls import patterns, include, url
from gm import views


urlpatterns = patterns('',
    url(r'^createQuest/$', views.createQuest, name='createQuest'),
    url(r'^createNotes/$', views.createNotes, name='createNotes'),



)
