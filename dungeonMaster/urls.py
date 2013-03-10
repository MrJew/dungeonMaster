from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^dungeonMaster/', include('system.urls')),
    url(r'^dungeonMaster/', include('gm.urls')),
    url(r'^dungeonMaster/', include('character.urls')),
)
