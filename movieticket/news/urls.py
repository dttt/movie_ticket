from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movieticket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^(?P<new_slug>[a-zA-Z0-9-]+)/?$', 'news.views.show', name='show'),
)
