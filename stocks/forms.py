from django import forms
from lk.models import *

class SelectStock(forms.Form):
	all_stock = [(elem.value, elem.title) for elem in Stock.objects.all()]
	stock = forms.ChoiceField(widget=forms.Select, choices=all_stock)
	stock.widget.attrs.update({'class': 'custom-select custom-select-sm', 'id': 'all_stock'})