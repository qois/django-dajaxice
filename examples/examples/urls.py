from django.conf.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import re_path, path

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from simple import views

dajaxice_autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'examples.views.home', name='home'),
    # url(r'^examples/', include('examples.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    re_path(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    re_path(r'', views.index)
]

urlpatterns += staticfiles_urlpatterns()
