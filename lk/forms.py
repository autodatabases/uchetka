from django import forms
from lk.models import *

class Photo(forms.Form):
	photo = forms.ImageField()