from django.conf.urls import patterns, include, url
import views

from django.contrib import admin

urlpatterns = patterns('',
    url(r'^main/',views.main ),
)
