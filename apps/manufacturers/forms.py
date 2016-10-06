from django import forms
from .models import *

class manufactureDetailsForm(forms.ModelForm):
        
    class Meta:
        model = Manufacture
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
        }