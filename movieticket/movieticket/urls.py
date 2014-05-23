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
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^facility/', include('facility.urls', namespace='facility')),
    url(r'^movie/', include('movie.urls', namespace='movie')),
    url(r'^search/$', 'book-ticket.views.book', name='book')
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
