from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns(
    url(r'^registerCharacter/$', views.register, name='register'),
)
