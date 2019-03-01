from django import forms
from lk.models import *

class RegForm(forms.Form):
	company_title = forms.CharField(max_length=50)
	company_title.widget.attrs.update({'class': 'form-control', 'placeholder': 'Название компании', 'required': ''})
	
	company_country = forms.CharField(max_length=50)
	company_country.widget.attrs.update({'class': 'form-control', 'placeholder': 'Страна', 'required': ''})

	company_region = forms.CharField(max_length=50)
	company_region.widget.attrs.update({'class': 'form-control', 'placeholder': 'Регион', 'required': ''})

	company_city = forms.CharField(max_length=50)
	company_city.widget.attrs.update({'class': 'form-control', 'placeholder': 'Город', 'required': ''})

	director_login = forms.CharField(max_length=50)
	director_login.widget.attrs.update({'class': 'form-control', 'placeholder': 'Логин', 'required': ''})

	director_fio = forms.CharField(max_length=50)
	director_fio.widget.attrs.update({'class': 'form-control', 'placeholder': 'Фамилия Имя Отчество', 'required': ''})

	director_email = forms.CharField(max_length=50)
	director_email.widget.attrs.update({'class': 'form-control', 'placeholder': 'Email', 'required': ''})

	director_password = forms.CharField(max_length=50)
	director_password.widget.attrs.update({'class': 'form-control', 'placeholder': 'Пароль', 'required': '', 'type': 'password'})


