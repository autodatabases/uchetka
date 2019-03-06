from django import forms
from lk.models import *

class SmallFilter(forms.Form):
	all_detals = [(elem.value, elem.title) for elem in AutoDetal.objects.all()]
	detal = forms.ChoiceField(widget=forms.Select, choices=all_detals)
	detal.widget.attrs.update({'class': 'custom-select'})
	
	all_marks = [('noselect', 'Все марки')]
	for elem in AutoMark.objects.all():
		all_marks.append((elem.value, elem.title))
	mark = forms.ChoiceField(widget=forms.Select, choices=all_marks)
	mark.widget.attrs.update({'class': 'custom-select', 'id': 'all_marks', 'onchange': 'load_models(this)'})

	model = forms.ChoiceField(widget=forms.Select, choices=[('noselect', 'Все модели')])
	model.widget.attrs.update({'class': 'custom-select', 'id': 'all_models', 'onchange': 'load_generations(this)'})

	generation = forms.ChoiceField(widget=forms.Select, choices=[('noselect', 'Все поколения')])
	generation.widget.attrs.update({'class': 'custom-select', 'id': 'all_generations'})

	number = forms.CharField(max_length=50)
	number.widget.attrs.update({'class': 'form-control', 'placeholder': 'Оригинальный номер'})

	all_stocks = [(elem.pk, elem.title) for elem in Stock.objects.all()]
	stock = forms.ChoiceField(widget=forms.Select, choices=all_stocks)
	stock.widget.attrs.update({'class': 'custom-select'})

	all_stock_params = []
	stock_param = forms.ChoiceField(widget=forms.Select, choices=[('noselect', 'Не выбрано')])
	stock_param.widget.attrs.update({'class': 'custom-select'})

