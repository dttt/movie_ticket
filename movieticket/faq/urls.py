from django.conf.urls import patterns, url


urlpatterns = patterns('',

    url(r'^$', 'faq.views.index', name='index'),
)
