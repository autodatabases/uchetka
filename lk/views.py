import json
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

def get_lk_page(request):
	all_marks= AutoMark.objects.all()

	return render(request, 'lk/index.html', context={'all_marks': all_marks, 
													 'detals_count': len(UserDetal.objects.all()),
													 'stockroom_count': len(Stock.objects.all()) })
	
def rediredct_detal_list_page(request):
	return redirect('/lk/detals_list/')

def add_StockRoom(request):
	print(dir(request.user))
	if request.is_ajax():
		new_stockroom = Stock()
		new_stockroom.title = request.POST['titleStockRoom']
		new_stockroom.street = request.POST['streetStockRoom']
		new_stockroom.house = request.POST['houseStockRoom']
		new_stockroom.account = request.user
		new_stockroom.save()
		data = json.dumps('good')
		return HttpResponse(data, content_type="application/json")

