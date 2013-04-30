from django.conf.urls.defaults import patterns, url

urlpatterns = patterns ('rankProj.views',
    url(r'^$', 'show_rank'),
    url(r'^(?P<proj_title>\w+)/$', 'show_proj'),

)
