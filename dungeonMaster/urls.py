from django.conf.urls import patterns, include, url
from character import urls
from gm import urls


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^dungeonMaster/', include('system.urls')),
    url(r'^dungeonMaster/', include('gm.urls')),
    url(r'^dungeonMaster/', include('character.urls')),
)
