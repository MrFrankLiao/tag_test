from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

def new2_register_view(request, username, activation_key):
    return redirect(reverse('new2_active_account', kwargs={'username': username, 'activation_key': activation_key}))

urlpatterns = patterns('',

    # Examples:
    # url(r'^$', 'tag_test.views.home', name='home'),
    # url(r'^tag_test/', include('tag_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin_tools/', include('admin_tools.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),

)
