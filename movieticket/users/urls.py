from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movieticket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^dang-ki/', 'users.views.signup', name='signup'),
    url(r'^dang-nhap/', 'users.views.signin', name='signin'),
    url(r'^dang-xuat/', 'users.views.signout', name='signout'),
    url(r'^(?P<user_id>\d+)/$',
        'users.views.profile', name='profile'),
    url(r'^(?P<user_id>\d+)/sua-thong-tin$',
        'users.views.edit', name='edit'),
    url(r'^(?P<user_id>\d+)/sua-mat-khau$',
        'users.views.edit_password', name='edit-password'),
)
