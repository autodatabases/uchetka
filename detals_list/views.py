import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from collections import OrderedDict

from lk.forms import *
from stocks.forms import *
from lk.models import *

def get_page(request):
	print(request.POST)
	query_donor = AutoDonor.objects.all()
	query_detal = AutoDetailTest.objects.all()
	query_stock = Stock.objects.filter(account=request.user)
	query_price = [0, 999999]
	if request.POST:
		if '' in request.POST.getlist('priceFilter'):
			if request.POST.getlist('priceFilter') != ['', '']:
				query_price = request.POST.getlist('priceFilter');
			else:
				if query_price[0] == '':
					query_price[0] = int(query_price[0].replace('', '0'))
				if query_price[1] == '':
					query_price[1] = int(query_price[1].replace('', '999999'))
		if request.POST.getlist('detal') != []: # Если детали отмечены, то ... 
			query_detal = [AutoDetailTest.objects.get(value=elem) for elem in request.POST.getlist('detal')]
		if request.POST.getlist('donor') != []: # Если доноры отмечены, то ... 
			query_donor = [AutoDonor.objects.get(pk=elem) for elem in request.POST.getlist('donor')]
		if request.POST.getlist('stock') != []: # Если склады отмечены, то ... 
			query_stock = [Stock.objects.get(pk=elem) for elem in request.POST.getlist('stock')]
	# Фильтруем список деталей | Да простит меня PEP 8
	query_result = UserDetal.objects.filter(account=request.user, price__gte=query_price[0], price__lte=query_price[1],	detail__in=query_detal, donor_info__in=query_donor, stockroom__in=query_stock)[0:100]
	all_detals = [{'detal': query_result[i], 'count': i+1 } for i in range(len(query_result))]
	# Для фильтров
	stocks_filters = Stock.objects.filter(account=request.user)
	detals_filter = set(list([elem.detail for elem in UserDetal.objects.filter(account=request.user)]))
	donors_filter = []
	for elem in UserDetal.objects.order_by('donor_info__mark', 'donor_info__model').filter(account=request.user):
		auto = elem.donor_info.mark.title, elem.donor_info.model.title, elem.donor_info.generation.year
		if {'full_name': auto} in donors_filter:
			continue
		else:
			donors_filter.append({'full_name': auto})
	context = {'all_marks': AutoMark.objects.all(), 'all_detals' : all_detals,
			   'detals_filter': detals_filter, 'donors_filter': donors_filter, 'stocks_filters': stocks_filters,
			   'stockroom_count': len(Stock.objects.filter(account=request.user)),
			   'form_donor': DonorForm, 'form_stock': StockForm
			   }
	return render(request, 'detals_list/index.html', context=context)

def get_donor_data(request):
	if request.is_ajax():
		donor = AutoDonor.objects.get(pk=request.POST['new_pk_donor'])
		data = {'mark': donor.mark.value, 'model': donor.model.value, 'generation': donor.generation.year,
				'kuzov': donor.kuzov.value, 'year': donor.year.value, 'engine_type': donor.engine_type.value,
				'engine_size': donor.engine_size.value, 'transmission': donor.transmission.value,
				'color': donor.color.value, 'helm': donor.helm.value, 'privod': donor.privod.value,
				'probeg': donor.probeg, 'vin_number': donor.vin_number }
		return HttpResponse(json.dumps(data), content_type="application/json")

def save_donor_data(request):
	if request.is_ajax():
		if request.POST['probeg']:
			probeg = request.POST['probeg']
		else:
			probeg = 0;
		donor_obj = AutoDonor.objects.get(pk=request.POST['idDonor'])
		donor_obj.kuzov = AutoKuzov.objects.get(value=request.POST['kuzov'])
		donor_obj.year = AutoYearProduction.objects.get(value=request.POST['year'])
		donor_obj.engine_type = AutoEngineType.objects.get(value=request.POST['engine_type'])
		donor_obj.engine_size = AutoEngineSize.objects.get(value=request.POST['engine_size'])
		donor_obj.transmission = AutoTransmission.objects.get(value=request.POST['transmission'])
		donor_obj.color = AutoColor.objects.get(value=request.POST['color'])
		donor_obj.helm = AutoHelm.objects.get(value=request.POST['helm'])
		donor_obj.privod = AutoPrivod.objects.get(value=request.POST['privod'])
		donor_obj.probeg = probeg
		donor_obj.vin_number = request.POST['vin']
		donor_obj.save()
		data = {'Good': 'good'}
		return HttpResponse(json.dumps(data), content_type="application/json")

def small_filter(request):
	if request.is_ajax():
		print(request.POST)
		if request.POST['filterValue'] == 'all':
			query_detals = UserDetal.objects.all()
		else:
			query_detals = UserDetal.objects.filter(detail=AutoDetailTest.objects.get(value=request.POST['filterValue']))
		
		arr_detal = []
		for elem in query_detals:
			arr_detal.append({'detal': {'title': elem.detail.title, 'value': elem.detail.value},
							  'stockroom': {'title': elem.stockroom.title, 'value': '1'},
							  'donor_info': {'id_donor': elem.donor_info.pk,
							  				 'mark': elem.donor_info.mark.title, 
							  				 'model': elem.donor_info.model.title,
							  				 'generation': elem.donor_info.generation.year},
							  'price': elem.price,
							  'description': elem.description, 
							  'photo': elem.photo.url, 
							  'account': request.user.username,
							  })
		data = json.dumps({'result_detal': arr_detal})
		return HttpResponse(data, content_type="application/json")