from django.conf.urls import patterns, include, url
from gm import views


urlpatterns = patterns('',
    url(r'^createQuest/$', views.createQuest, name='createQuest'),
    url(r'^editQuest/(?P<quest_id>[\d]+)/$', views.editQuest, name='editQuest'),
    url(r'^createNotes/$', views.createNotes, name='createNotes'),
    url(r'^editNote/(?P<note_id>[\d]+)/$', views.editNotes, name='editNotes'),
    url(r'^giveItem/(?P<player_id>[\d]+)/$', views.giveItem, name='giveItem'),
    url(r'^giveEffect/(?P<player_id>[\d]+)/$', views.giveEffect, name='giveEffect'),

)
