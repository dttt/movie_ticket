from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movieticket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^theaters/', 'facility.views.theaterIndex', name='theater-index')
)
