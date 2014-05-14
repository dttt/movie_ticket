from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movieticket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^signup/', 'users.views.signup', name='signup'),
    url(r'^login/', 'users.views.login', name='login'),
)
