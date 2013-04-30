from django.conf.urls.defaults import patterns, url

urlpatterns = patterns ('user_vote.views',

    url(r'^window_load_time_stemp/$', 'window_load_time_stemp'),
    url(r'^window_unload_time_stemp/$', 'window_unload_time_stemp'),
    url(r'^voting_project/$', 'voting_project'),
    url(r'^rankfilter/$', 'rankfilter'),
)
