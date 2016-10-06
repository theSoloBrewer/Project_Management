from django import forms
from apps.hardware.models import Hardware
from .models import *

class doorDetailsForm(forms.ModelForm):
	def validChoice(value):
		if value >= 0:
			pass
		else:
			raise validationError('You need to choose a door to view')
		
	class Meta:
		model = Door
		exclude = ('devices',)
		widgets = {
			'id': forms.HiddenInput(),
			'project': forms.HiddenInput(),
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'number': forms.TextInput(attrs={'class':'form-control'}),
			'description': forms.TextInput(attrs={'class':'form-control'}),
			'notes': forms.Textarea(attrs={'class':'form-control'}),
		}
		
		def __init__(self, *args, **kwargs):
			super(doorDetailsForm, self).__init__(*args, **kwargs)
			
class doorHardwareForm(forms.ModelForm):
	class Meta:
		model = DoorHardware
		fields = ('installed',)
		exclude = ('hardware','door', )
		widgets = {
			'installed': forms.CheckboxInput(attrs={'class': 'status', 'value': 'False' }),
		}
		
	# def __init__(self, *args, **kwargs):
		# self.user = kwargs.pop('user', None)
		# super(hardwareMemberForm, self).__init__(*args, **kwargs)