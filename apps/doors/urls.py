from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'delete/(?P<owner_id>\d+)', views.doorHardwareRemoveView, name='HardwareRemove'),
    url(r'^/new/(?P<owner_id>\d+)/', views.doorModalView, name='doorModal'),
    url(r'status/(?P<owner_id>\d+)/', views.doorHardwareStatus, name='doorHardwareStatus'),
    url(r'^/(?P<id>\d+)/', views.doorDetailsView, name='doorDetails'),
]