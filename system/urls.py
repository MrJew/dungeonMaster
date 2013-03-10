from django.conf.urls import patterns, include, url
import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^main/',views.main ),
    url(r'^admin/', include(admin.site.urls)),
)
