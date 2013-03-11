from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^registerCharacter/$', views.register, name='register'),
    url(r'^describeCharacter/(?P<u_id>[\d]+)/$', views.describe, name='describeChar'),
    url(r'^createArmor/$', views.createArmor, name='createArmor'),
    url(r'^createWeapon/$', views.createWeapon, name='createWeapon'),
    url(r'^createMisc/$', views.createMisc, name='createMisc')
)
