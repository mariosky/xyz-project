from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()




urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'xyz.views.gallery', name='gallery'),

    url(r'^gallery_paint/(\d*)/$', 'xyz.views.gallery_paint', name='gallery_paint'),
    url(r'^artist/(\d*)/$', 'xyz.views.artist', name='artist'),
    url(r'^masonry$', 'xyz.views.gallery_masonry', name='gallery_masonry'),
    url(r'^about$', 'xyz.views.about', name='about'),
    url(r'^kenburns', 'xyz.views.gallery_kenburns', name='gallery_kenburns'),
    url(r'^grid', 'xyz.views.gallery_grid', name='gallery_grid'),
    url(r'^index.html$', 'xyz.views.gallery', name='gallery'),
    url(r'^last_generation$', 'xyz.views.generation', name='generation'),
    url(r'^generation/(\d*)/$', 'xyz.views.generation', name='generation'),
    url(r'^upload.html$', 'xyz.views.upload', name='upload'),
    url(r'^upload_minimal', 'xyz.views.upload_minimal', name='upload_minimal'),
    url(r'^evoart', 'xyz.views.evoart', name='evoart'),
    url(r'^logout', 'xyz.views.logout_view', name='logout_view'),
    url(r'^update_paint', 'xyz.views.update_paint', name='update_paint'),

    # url(r'^xyz_project/', include('xyz_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)