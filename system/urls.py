from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',

    url(r'^main/',views.main ),
    url(r'^main/', views.main ),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'create/crtskill/', views.crtSkill),
    url(r'create/crtprof/', views.crtProf),
    url(r'create/crteffect/', views.crtEff),

)
