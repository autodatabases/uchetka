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
			detail=AutoDetailTest.objects.get(pk=random.randint(1, 20)),
			donor_info=AutoDonor.objects.get(pk=random.randint(1, 25)),
			price=random.randint(1000, 20000),
			stockroom=Stock.objects.get(value=1),
			account=request.user
		)
		print('Добавленно деталей '+str(i))
	return redirect('/lk/detals_list/')

