from django.conf.urls.defaults import *

urlpatterns = patterns('subscription.views',
    url(r'^$', 'subscribe', name='subscribe'),
    url(r'^(\d+)/sucesso/$', 'success_or_notification_fail', name='success'),
    url(r'^(\d+)/sucesso_e_falha/$', 'success_or_notification_fail', {'template': 'subscription/notificationFail.html'}, name='fail'),
)
