from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movieticket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'facility.views.theaters_index', name='theaters-index'),
    url(r'^(?P<theater_slug>[a-zA-Z0-9-]+)/$',
        'facility.views.theater_show', name='theater-show')
)
