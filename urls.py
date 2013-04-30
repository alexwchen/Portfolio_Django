from django.conf.urls.defaults import patterns, include, url
from django.views.static import * 
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    # Index Page
    url(r'^$', 'rankProj.views.show_rank'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^.*/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
    # Portfolio Pages
    url(r'^portfolio/', include('rankProj.urls')),
    (r'^portfolio/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^portfolio/.*/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # Publication Pages
    url(r'^publication/$','rankProj.views.publication_rank'),
    url(r'^publication/(?P<proj_title>\w+)/$','rankProj.views.publication_link'),
    (r'^publication/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^publication/.*/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
    # Resume Pages
    url(r'^education/$','education.views.education_rank'),
    (r'^education/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
    # Education Pages
    url(r'^resume/$','resume.views.resume_display'),
    (r'^resume/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
    # Contact Pages
    url(r'^contact/$','resume.views.contact_display'),
    (r'^contact/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    
    # User Voting Action Handler
    url(r'^user_vote/', include('user_vote.urls')),
)
# Uncomment the admin/doc line below to enable admin documentation:
# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
            url(r'^static/(?P<path>.*)$', 'serve'),
                )
