from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    url(r'^dungeonMaster/', include('system.urls')),
    url(r'^dungeonMaster/', include('gm.urls')),
    url(r'^dungeonMaster/', include('character.urls')),
)
