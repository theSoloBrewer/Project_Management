from django.shortcuts import render
from .models import *
from django.views import generic
from .forms import doorDetailsForm, doorHardwareForm
from django import forms
from apps.hardware.models import Hardware
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ValidationError

from django.db.backends.signals import connection_created
from django.dispatch import receiver

#@receiver(connection_created)
#def connection_init(sender, connection, **kwargv):
#	connection.cursor().execute("SET autocommit=1")
	
def formValidSave(request,TargetForm,TargetInstance,project_id=None):
	form = TargetForm(instance=TargetInstance, initial={'project': TargetInstance.project.pk} )
	form.fields['project'].value = project_id
	if request.method == 'POST':
		form = TargetForm(request.POST,instance=TargetInstance)
		if form.is_valid():
				m = form.save()
				
	return form

	
	# Create your views here.
def doorDetailsView(request, id=None):
	if id:
		obj = Door.objects.get(pk=id)
		hardware_list = DoorHardware.objects.filter(door_id=id).prefetch_related()
	else:
		obj = Door()
		hardware_list = []
	form = formValidSave(request, doorDetailsForm, obj, obj.project.pk)
	if request.method == 'POST':
		return HttpResponseRedirect('/projects/' + request.POST['project'])
	return render(request, 'doors/details.html', {'form': form, 'list': hardware_list,})
	
	
	
def doorModalView(request, owner_id=None):
	if request.method == 'POST':
		form = formValidSave(request, doorDetailsForm, Door(project_id=owner_id), request.POST['project'])	  
		return render(request, 'doors/details.html', {'form': form,} )
	else:
		form = doorDetailsForm(initial={'project': owner_id,})
		# form.fields['members'].widget = forms.HiddenInput(attrs = {'value': owner_id})	 
		list = []
		return render(request, 'doors/details.html', {'form': form, 'list': list})
	return HttpResponse(status=205)
	
	
def doorHardwareStatus(request, owner_id):
	if request.method == 'POST':
		obj = DoorHardware.objects.get( pk=request.POST['hardware_id'])
		try:
			obj.installed = request.POST['status']
			hwForm = doorHardwareForm(instance=obj, data=obj.__dict__)
			if hwForm.is_valid():
				hwForm.save()
				return HttpResponse(request, content_type='text/plain', status=200)
			else:
				return HttpResponse(request, content_type='text/plain'	, status=301)
		
		except ValidationError, e:
			return e.message_dict
		
def doorHardwareRemoveView(request, owner_id):
	if request.method == 'POST':
		try:
			DoorHardware.objects.get(pk=request.POST['hardware_id']).delete()
			return HttpResponse(request, content_type='text/plain', status=205)
		
		except ValidationError, e:
			return e.message_dict
