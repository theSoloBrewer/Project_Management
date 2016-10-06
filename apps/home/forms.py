from django import forms
        
class welcomePageForm(forms.Form):
      
    projectFilter = forms.CharField(label='Filter', max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}), required=False)    
    