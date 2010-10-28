from django.conf.urls.defaults import *

from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^eventex/', include('eventex.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    #(r'^$', homepage, {'template': 'index.html'}),

    url(r'^$', 'core.views.homepage', name='homepage'),

    (r'^inscricao/', include('subscription.urls', namespace='subscription')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root' : settings.MEDIA_ROOT}),
    )
