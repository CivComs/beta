from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'beta.views.home', name='home'),
    # url(r'^beta/', include('beta.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^$', "beta.views.index"),
    (r'^admin/', include(admin.site.urls)),
    (r'^invite/', include('privatebeta.urls')),
)
