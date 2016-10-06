from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'delete/', views.projectDoorRemoveView, name='projectDoorRemove'),
    url(r'^(?P<id>\d+)/', views.projectDetailsView, name='projectDetails'),
    url(r'new/$', views.projectDetailsView, name='projectNewDetails'),
]