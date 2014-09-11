from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'accupasslog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/logs', 'log.api.home'),
    url(r'^api/log', 'log.api.createLog'),
)
