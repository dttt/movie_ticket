from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

from movieticket import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movieticket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'movie.views.home', name='home'),
    url(r'^$', include('django.contrib.flatpages.urls')),
    url(r'^tai-khoan/', include('users.urls', namespace='users')),
    url(r'^tin-khuyen-mai/', include('news.urls', namespace='news')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^cum-rap/', include('facility.urls', namespace='facility')),
    url(r'^phim/', include('movie.urls', namespace='movie')),
    url(r'^search/$', 'ticket.views.book', name='book'),
    url(r'^dat-ve/',
        include('reservation.urls', namespace='reservation')),
    url(r'^accounts/login/$', 'users.views.signin'),

    # URL for ajax request
    url(r'^ajax/theaters/$',
        'reservation.views.ajax_theaters', name='ajax-theaters'),
    url(r'^ajax/schedules/$',
        'reservation.views.ajax_schedules', name='ajax-schedules'),
    url(r'^ajax/seats/$',
        'reservation.views.ajax_seats', name="ajax-seats"),
    url(r'^ajax/finish/$',
        'reservation.views.ajax_finish', name="ajax-finish"),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
