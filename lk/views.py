import json
import random

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout

from .models import *


def logout_lk(request):
	logout(request)
	return redirect('/')
def rediredct_detal_list_page(request):
	return redirect('/lk/detals_list/')


def add_random_detal(request):
	for i in range(50000):
		UserDetal.objects.create(
			detal=AutoDetal.objects.get(pk=random.randint(1, 20)),
			donor_info=AutoDonor.objects.get(pk=random.randint(1, 25)),
			price=random.randint(1000, 20000),
			stockroom=Stock.objects.get(title='Авторазбор №1'),
			company=Company.objects.get(title='Разбор-маркет')
		)
		print('Добавленно деталей '+str(i))
	return redirect('/lk/detals_list/')

def add_detals(required):
	for i in range(20):
		detal = AutoDetal.objects.create(
			title='Тестовая деталь '+str(i+1),
			value=str(i+1),
		)
		print(detal)
	return redirect('/lk/detals_list/')


