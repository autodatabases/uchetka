from django import forms
from lk.models import *

class Photo(forms.Form):
	photo = forms.ImageField()

class DonorPanel(forms.Form):
	vin = forms.CharField(max_length=50)
	vin.widget.attrs.update({'class': 'form-control', 'id': 'donorVin'})

	probeg = forms.CharField(max_length=50)
	probeg.widget.attrs.update({'class': 'form-control', 'id': 'donorProbeg'})

	all_marks = [(elem.value, elem.title) for elem in AutoMark.objects.all()]
	mark = forms.ChoiceField(widget=forms.Select, choices=all_marks)
	mark.widget.attrs.update({'class': 'custom-select', 'id': 'all_marks'})
