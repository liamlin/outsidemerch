from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views import generic


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'outsidemerch.views.root', name='root'),
    url(r'^demo/(?P<stage_id>\d)/(?P<current_time>\d+)/', 'outsidemerch.views.root', name='root'),
    url(r'^demo/(?P<stage_id>\d)/', 'outsidemerch.views.demo_stage', name='demo_stage'),
    url(r'^demo/(?P<current_time>\d+)/', 'outsidemerch.views.demo_time', name='demo_time'),
    url(r'^stage/(?P<stage_id>\d)/demo/(?P<current_time>\d+)', 'outsidemerch.views.stage', name='stage_demo'),
    url(r'^stage/(?P<stage_id>\d)/', 'outsidemerch.views.stage', name='stage'),

    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^favicon.ico$", generic.RedirectView.as_view()),

)

if not settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
