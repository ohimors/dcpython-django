from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^events$', 'events.views.events', name='events'),
    url(r'^donate$', 'support.views.support', name='support'),
    url(r'^about$', 'app.views.about', name='about'),
    url(r'^deals$', 'app.views.deals', name='deals'),
    # url(r'^$', 'dcpython.views.home', name='home'),
    # url(r'^dcpython/', include('dcpython.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
