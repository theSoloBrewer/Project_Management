from django import forms
from apps.manufacturers.models import Manufacture
from .models import *

class hardwareDetailsForm(forms.ModelForm):
        
    class Meta:
        model = Hardware
        fields = '__all__'
        widgets = {
            'manufacture': forms.Select(attrs={'class':'form-control'}),
            'type': forms.Select(attrs={'class':'form-control'}),
            'model': forms.TextInput(attrs={'class':'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(hardwareDetailsForm, self).__init__(*args, **kwargs)
   
class hardwareSelectForm(forms.Form):
    device = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control col-xs-6 col-md-4', 'size': '10'}))
    manufacture = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control col-xs-6 col-md-4', 'size': '10'}))
    model = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control col-xs-6 col-md-4', 'size': '10'}))
    #choices = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control', 'size': '20'}))
    