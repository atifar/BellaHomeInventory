from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'bhf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^inventory/', include('inventory.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', name='auth_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/inventory/products'}, name='auth_logout'),
]

if settings.DEBUG:

    # Appending url pattern for serving user uploaded files
    urlpatterns.append(url(r'^media/(?P<path>.*)', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT}))
