from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movieticket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^signup/', 'users.views.signup', name='signup'),
    url(r'^signin/', 'users.views.signin', name='signin'),
    url(r'^signout/', 'users.views.signout', name='signout'),
    url(r'^(?P<user_id>\d+)/profile/$',
        'users.views.profile', name='profile'),
)
