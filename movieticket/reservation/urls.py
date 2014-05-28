from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movieticket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^(?P<reservation_id>\d+)/$', 'reservation.views.show', name='show'),
    url(r'^select/$',
        'reservation.views.select_schedules', name='select-schedules'),
    url(r'^make/(?P<schedule_id>\d+)/$',
        'reservation.views.make', name='make'),
    url(r'^make/(?P<schedule_id>\d+)/(?P<quantity>\d+)/$',
        'reservation.views.select_tickets', name='select-tickets'),
)
