from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    url(r'^$', 'player.views.index'),
    url(r'^device$', 'player.views.device'),
    url(r'^socket.io', 'player.views.api'),
)

urlpatterns += staticfiles_urlpatterns()
