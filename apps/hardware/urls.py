from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^edit/selection/', views.hardwareSelectView, name='hadwareEditSelect'),
    url(r'^add/(?P<owner_id>\d+)/$', views.hardwareSelectView, name='hardwareSelect'),
	url(r'^new/$', views.hardwareDetailsView, name='hardwareNewDetails'),
    url(r'(?P<hid>\d+)/', views.hardwareDetailsView, name='hardwareDetails'),
]