from django import forms

class DoorForm(forms.Form):
	number = forms.CharField()
	title = forms.CharField()