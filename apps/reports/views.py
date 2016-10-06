from django.shortcuts import render
from .forms import DoorForm
from apps.doors.models import *
from apps.cameras.models import *
from apps.projects.models import *
from django.db.models import Q, Prefetch
from django.forms import formset_factory, modelform_factory
from django import forms

# Create your views here.

def reportsView(request):
	list = Project.objects.all()
	title = 'All Doors Reports'
	return render(request, 'reports/all.html', {'list': list, 'title':title})
	
def hardwareInstallStatusView(request, id=None, issue=None):
	if issue:
		dQuerySet = Door.objects.filter(project_id=id).filter(Q(doorhardware__installed=False) | Q(devices__isnull=True)).prefetch_related(Prefetch('devices', queryset=DoorHardware.objects.only('installed').order_by('hardware__type'))).distinct()
	else:
		dQuerySet = Door.objects.filter(project_id=2).order_by('number').prefetch_related(Prefetch('devices', queryset=DoorHardware.objects.only('installed').order_by('hardware__type')))
	form = dQuerySet
	dev = ['Door Contact', 'Reader', 'Request To Exit', 'Lock']
	return render(request, 'reports/hardwareCompletionStatus.html', {'form': form, 'dev': dev})
	
def cameraInstallStatusView(request, id=None):
	
	dQuerySet = Camera.objects.filter(project_id=id).prefetch_related(Prefetch('device', queryset=Hardware.objects.only('model')))
	form = dQuerySet
	return render(request, 'reports/cameraCompletionStatus.html', {'form': form,})
