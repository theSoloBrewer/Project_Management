"""Project_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('apps.home.urls')),
    url(r'^projects/', include('apps.projects.urls')),
    url(r'^doors', include('apps.doors.urls')),
    url(r'^hardware/', include('apps.hardware.urls')),
    url(r'^manufacturers/', include('apps.manufacturers.urls')),
	url(r'^cameras/', include('apps.cameras.urls')),
	url(r'^reports/', include('apps.reports.urls')),
] 

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
