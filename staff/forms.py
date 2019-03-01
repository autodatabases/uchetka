from django import forms
from django.contrib.auth.models import Group

from lk.models import *

class NewStaffUser(forms.Form):
	
	staff_login = forms.CharField(max_length=50)
	staff_login.widget.attrs.update({'class': 'form-control', 'placeholder': 'Логин', 'required': ''})

	staff_fio = forms.CharField(max_length=50)
	staff_fio.widget.attrs.update({'class': 'form-control', 'placeholder': 'Фамилия Имя Отчество', 'required': ''})

	staff_email = forms.CharField(max_length=50)
	staff_email.widget.attrs.update({'class': 'form-control', 'placeholder': 'Email', 'required': ''})

	staff_password = forms.CharField(max_length=50)
	staff_password.widget.attrs.update({'class': 'form-control', 'placeholder': 'Пароль', 'required': '', 'type': 'password'})

	all_groups = [(elem.name, elem.name) for elem in Group.objects.all()]
	staff_group = forms.ChoiceField(widget=forms.Select, choices=all_groups)
	staff_group.widget.attrs.update({'class': 'custom-select'})

	all_stocks = [(elem.pk, elem.title) for elem in Stock.objects.all()]
	staff_stock = forms.ChoiceField(widget=forms.Select, choices=all_stocks)
	staff_stock.widget.attrs.update({'class': 'custom-select'})



