from django import forms
from .models import *

class projectDetailsForm(forms.ModelForm):
        
    class Meta:
        model = Project
        fields = ['id', 'job_code', 'title', 'comments','lat','lng' ]
        widgets = {
            'id': forms.HiddenInput(),
            'job_code': forms.TextInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
			'comments': forms.Textarea(attrs={'class':'form-control'}),
			'lat': forms.TextInput(attrs={'class':'form-control'}),
			'lng': forms.TextInput(attrs={'class':'form-control'}),
        }
    
    # def __init__(self, *args, **kwargs):
        # choices = kwargs.pop('choices', None)
        # super(projectDetailsForm, self).__init__(*args, **kwargs)
        # if choices:
            # self.fields['doors'].choices = choices
    