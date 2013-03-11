from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^main/',views.main ),

    url(r'^main/', views.main ),
    url(r'^create/crtskill/$', views.crtSkill, name="createskill"),
    url(r'^create/crtprof/$', views.crtProf, name="createprofession"),
    url(r'^create/crteffect/$', views.crtEff, name="createeffect"),
    url(r'^login/$', views.char_login, name="login"),
    url(r'^logout/$', views.char_logout, name="logout"),
    url(r'^log/$', views.show_log, name="log"),
    url(r'create/crtskill/', views.crtSkill),
    url(r'create/crtprof/', views.crtProf),
    url(r'create/crteffect/', views.crtEff),


)
