from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movieticket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'movie.views.home', name='home'),
    url(r'^$', include('django.contrib.flatpages.urls')),
    url(r'^users/', include('users.urls', namespace='users')),
)
