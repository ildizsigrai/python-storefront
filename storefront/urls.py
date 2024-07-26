
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from debug_toolbar import urls as debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar_urls)),
    ] + urlpatterns