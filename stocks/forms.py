from django import forms
from lk.models import *

class SelectStock(forms.Form):
	all_stock = []
	stock = forms.ChoiceField(widget=forms.Select, choices=all_stock)
	stock.widget.attrs.update({'class': 'custom-select custom-select-sm', 'id': 'all_stock'})


class StockForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['title', 'country', 'region', 'city', 'street', 'house']

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'По умолчанию: Склад № ... '}),
			'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Например: Российская Федерация'}),
			'region': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Например: Удмуртская Республика'}),
			'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Например: Ижевск'}),
			'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Например: Воткинское шоссе'}),
			'house': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '13'})
		}
	def save(self):
		new_stock = Stock.objects.create(
			title=self.cleaned_data['title'],
			value=self.cleaned_data['value'],
			country=self.cleaned_data['country'],
			region=self.cleaned_data['region'],
			city=self.cleaned_data['city'],
			street=self.cleaned_data['street'],
			house=self.cleaned_data['house'],
			account=self.cleaned_data['account'],
		)

		return new_stock