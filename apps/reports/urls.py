from django.conf.urls import include, url, patterns
from . import views

urlpatterns = [
	url(r'^doors/all$', views.reportsView, name='reportsLanding'),
	url(r'^doors/issue$', views.reportsView, name='reportsLanding'),
	url(r'^cameras/all$', views.reportsView, name='reportsLanding'),
	url(r'^cameras/issue$', views.reportsView, name='reportsLanding'),
    url(r'^doors/all/(?P<id>\d+)/', views.hardwareInstallStatusView, name='hardwareInstallStatus'),
	url(r'^doors/issue/(?P<id>\d+)', views.hardwareInstallStatusView, {'issue':True,}, name='hardwareInstallIssues'),
	url(r'^cameras/all/(?P<id>\d+)/', views.cameraInstallStatusView, name='cameraInstallStatus'),
] 