from django.shortcuts import render
from apps.doors.models import Door, DoorHardware
from .forms import *
from .models import *
from apps.manufacturers.models import Manufacture
from apps.devices.models import Device
from django.core import serializers
from django.http import HttpResponseRedirect


# Create your views here.
def hardwareDetailsView(request, hid=None):
	form = hardwareDetailsForm()
	try:
		hObj = Hardware.objects.get(pk=hid)
	except Hardware.DoesNotExist:
		hObj = None
	if request.method == 'POST':
		form = hardwareDetailsForm(request.POST, instance=hObj)
		if form.is_valid():
			print 'valid'
			f = form.save(commit=False)
			f.model = request.POST['model']
			f.save()
			return render(request, 'hardware/details.html', {'form': form})
		else:
			print form.errors
	else:
		form = hardwareDetailsForm(instance=hObj)
		form.fields['type'].choices = [(obj.id, obj.type) for obj in Device.objects.all()]
		form.fields['manufacture'].choices = [(obj.id, obj.name) for obj in Manufacture.objects.all()]
		form.fields['model'].choices = [(obj.id, obj.model) for obj in Hardware.objects.all()]
	
	return render(request, 'hardware/details.html', {'form': form})

def hardwareSelectView(request, owner_id=None):
	if request.method == 'POST':
		dh = DoorHardware(door=Door.objects.get(id=owner_id), hardware=Hardware.objects.get(id=request.POST['selectedChoice']), installed=False)
		dh.save()
		return HttpResponseRedirect('/doors/'+owner_id)
	form = hardwareSelectForm()
	print form
	list = Hardware.objects.all().prefetch_related()
	form.fields['device'].choices = [(obj.id, obj.type) for obj in Device.objects.all()]
	form.fields['manufacture'].choices = [(obj.id, obj.name) for obj in Manufacture.objects.all()]
	form.fields['model'].choices = [(obj.id, obj.model) for obj in Hardware.objects.all()]
	if owner_id:
		table_action = 'select'
	else:
		table_action = 'edit'
		
	return render(request, 'hardware/selection.html', {'form': form, 'list': list, 'owner_id': owner_id, 'table_action':table_action, })