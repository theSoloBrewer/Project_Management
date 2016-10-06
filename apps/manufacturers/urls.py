from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'(?P<mid>[0-9]*)/', views.manufactureDetailsView, name='manufactureDetails'),
    url(r'^$', views.manufactureDetailsView, name='hardwareSelect'),
]