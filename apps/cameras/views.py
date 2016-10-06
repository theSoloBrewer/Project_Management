from django.shortcuts import render
from django.forms import modelform_factory
from django import forms
from .models import *
#from .forms import *
from apps.hardware.models import Hardware
from apps.devices.models import Device
# Create your views here.
def CameraSelectionView(request, id=None):
	
	CamForm = modelform_factory(
		Camera,
		fields= '__all__',
		widgets={
			'project': forms.HiddenInput(),
			'name': forms.TextInput(attrs={'class':'form-control',}),
			'device': forms.Select(attrs={'class':'form-control',}),
			'installed': forms.CheckboxInput(attrs={'class':'form-control',}),
			'serial': forms.TextInput(attrs={'class':'form-control',}),
			'network': forms.TextInput(),
			'description': forms.TextInput(attrs={'class':'form-control',}),
			'notes': forms.Textarea(attrs={'class':'form-control',}),
			}
		)
	NetForm = modelform_factory(
		NetworkInfo,
		fields=('__all__'),
		widgets={
			'ip': forms.TextInput(attrs={'class':'form-control'}),
			'subnet': forms.TextInput(attrs={'class':'form-control'}),
			'gateway': forms.TextInput(attrs={'class':'form-control'}),
			'MAC': forms.TextInput(attrs={'class':'form-control'}),
			'vlan': forms.TextInput(attrs={'class':'form-control'}),
			}
		)
	
	
	# exsisting Camera
	try: 
		cObj = Camera.objects.get(pk=id)
		cForm = CamForm(instance=cObj)
		try:
			nObj = cObj.network
			nForm = NetForm(instance=nObj)
		except:
			nObj = None
			nForm = NetForm()
	# new Camera 
	except Camera.DoesNotExist:	 
		cObj = None
		cForm = CamForm()
		nObj = None
		nForm = NetForm()
		
	print(cForm)
	if request.method == 'POST':
		camform = CamForm(request.POST, instance=cObj)
		netform = NetForm(request.POST, instance=nObj)
		if camform.is_valid():
			tmpCam = camform.save(commit=False)
			if netform.is_valid():
				tmpForm = netform.save()
				tmpNet = NetworkInfo.objects.get(pk=tmpForm.id)
				tmpCam.serial = tmpNet.MAC
			tmpCam.network = tmpNet
			tmpCam.save()
	
	return render(request, 'cameras/details.html', {'form': cForm, 'netform': nForm})