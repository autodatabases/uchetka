from django import forms
from lk.models import *

class SmallFilter(forms.Form):
	all_detals = [(elem.value, elem.title) for elem in AutoDetal.objects.all()]
	detal = forms.ChoiceField(widget=forms.Select)
	detal.widget.attrs.update({'class': 'custom-select', 'name': 'detal'})
	
	all_marks = [(elem.value, elem.title) for elem in AutoMark.objects.all()]
	mark = forms.ChoiceField(widget=forms.Select, choices=all_marks)
	mark.widget.attrs.update({'class': 'custom-select', 'id': 'all_marks', 'name': 'mark',
							  'onchange': 'load_models(this)'})

	model = forms.ChoiceField(widget=forms.Select)
	model.widget.attrs.update({'class': 'custom-select', 'id': 'all_models', 'name': 'model',
							   'onchange': 'load_generations(this)'})

	generation = forms.ChoiceField(widget=forms.Select)
	generation.widget.attrs.update({'class': 'custom-select', 'id': 'all_generations', 'name': 'generation'})

	all_numbers= []
	number = forms.ChoiceField(widget=forms.Select)
	number.widget.attrs.update({'class': 'custom-select', 'name': 'number'})

	all_stocks = []
	stock = forms.ChoiceField(widget=forms.Select)
	stock.widget.attrs.update({'class': 'custom-select', 'name': 'stock'})

	all_stock_params = []
	stock_param = forms.ChoiceField(widget=forms.Select)
	stock_param.widget.attrs.update({'class': 'custom-select', 'name': 'stock_param'})

