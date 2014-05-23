from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movieticket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'movie.views.home', name='home'),
    url(r'^(?P<movie_id>\d+)/$', 'movie.views.show_movie', name='show-movie'),
    url(r'^(?P<version_slug>[a-zA-Z0-9-]+)/?$', 
        'movie.views.show_version', name='show-version'),
)
