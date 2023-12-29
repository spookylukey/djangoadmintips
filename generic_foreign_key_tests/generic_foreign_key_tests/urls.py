"""generic_foreign_key_tests URL Configuration

"""
from django.conf import settings
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path(r'admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
