from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views import generic

# from rest_framework import routers

admin.autodiscover()

# router = routers.DefaultRouter()
# urlpatterns = patterns('',
#     url(r'^$', include(router.urls)),)

urlpatterns = patterns('',
    url(r'^$', 'outsidemerch.views.root', name='root'),
    url(r'^stages/', 'outsidemerch.views.stages', name='stages'),

    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^favicon.ico$", generic.RedirectView.as_view()),

)

if not settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
