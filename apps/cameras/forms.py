from django import forms
from apps.common import NetworkInfo
from .models import *

class CameraForm(forms.ModelForm):
	class Meta:
		model = Camera
		exclude = ('network',)
	widgets={
		'project': forms.HiddenInput(),
		'name': forms.TextInput(attrs={'class':'form-control',}),
		'device': forms.Select(attrs={'class':'form-control',}),
		'installed': forms.CheckboxInput(attrs={'class':'form-control',}),
		'serial': forms.TextInput(attrs={'class':'form-control',}),			
		'description': forms.TextInput(attrs={'class':'form-control',}),
		'notes': forms.TextInput(attrs={'class':'form-control',}),
	}
	
		
class NetworkForm(forms.ModelForm):
	class Meta:
		model = NetworkInfo
		fields = '__all__'
		
	widgets={
		'ip_address': forms.TextInput(attrs={'class':'form-control'}),
		'gateway': forms.TextInput(attrs={'class':'form-control'}),	
		'subnet': forms.TextInput(attrs={'class':'form-control'}),	
	}
	