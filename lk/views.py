import json
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
import random

def get_lk_page(request):
	all_marks= AutoMark.objects.all()

	return render(request, 'lk/index.html', context={'all_marks': all_marks, 
													 'detals_count': len(UserDetal.objects.all()),
													 'stockroom_count': len(Stock.objects.all()), })
	
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

