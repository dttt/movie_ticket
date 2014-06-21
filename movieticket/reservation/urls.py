from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movieticket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',
        'reservation.views.select_schedules', name='select-schedules'),
    url(r'^(?P<reservation_id>\d+)/$', 'reservation.views.show', name='show'),
    url(r'^(?P<schedule_id>\d+)/dat/$',
        'reservation.views.make', name='make'),
    url(r'^hoan-tat/$', 'reservation.views.finish', name='finish'),
)
