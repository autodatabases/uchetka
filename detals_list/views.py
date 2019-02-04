import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from collections import OrderedDict

from lk.models import *

def get_detals_list_page(request):
	print(request.POST)
	query_donor = AutoDonor.objects.all()
	query_detal = AutoDetailTest.objects.all()
	selected_donor = 0 
	selected_checkbox_detal, selected_checkbox_donor = [], []
	i = 0
	if request.POST:
		if request.POST.getlist('detal') != []: # Если детали отмечены, то ... 
			query_detal = [AutoDetailTest.objects.get(value=elem) for elem in request.POST.getlist('detal')]
			selected_checkbox_detal = request.POST.getlist('detal')
		if request.POST.getlist('donor') != []: # Если доноры отмечены, то ... 
			query_donor = [AutoDonor.objects.get(pk=elem) for elem in request.POST.getlist('donor')]
			selected_checkbox_donor = [ int(elem) for elem in request.POST.getlist('donor')]
			selected_donor = request.POST['donor']

	query_result = UserDetal.objects.filter(account=request.user, detail__in=query_detal, donor_info__in=query_donor)
	all_detals = [ {'detal': query_result[i], 'count': i+1 } for i in range(len(query_result))]
	
	detals = set(list([elem.detail for elem in UserDetal.objects.filter(account=request.user)]))
	donors = set(list([elem.donor_info for elem in UserDetal.objects.order_by('donor_info__mark').filter(account=request.user) ]))
	stocks = Stock.objects.filter(account=request.user)
	context = {'all_marks': AutoMark.objects.all(), 'all_detals' : all_detals,
			   'detals_count': len(UserDetal.objects.filter(account=request.user)),'all_kuzovs': AutoKuzov.objects.all(),'all_years': AutoYearProduction.objects.all(),
			   'all_engine_type': AutoEngineType.objects.all(),'all_engine_size': AutoEngineSize.objects.all(),
			   'all_kpp': AutoTransmission.objects.all(),'all_color': AutoColor.objects.all(),
			   'all_helm': AutoHelm.objects.all(),'all_privod': AutoPrivod.objects.all(),
			   'detals_filter': detals, 'donors_filter': donors, 'stocks_filters': stocks,
			   'stockroom_count': len(Stock.objects.filter(account=request.user)), 'selected_donor': int(selected_donor),
			   'selected_checkbox_detal': selected_checkbox_detal, 'selected_checkbox_donor': selected_checkbox_donor,
			   }
	return render(request, 'detals_list/index.html', context=context)

def get_donor_page(request):
	print(request.POST)
	if request.is_ajax():
		donor = AutoDonor.objects.get(pk=request.POST['new_pk_donor'])
		new_content_data = {'mark': donor.mark.title,
							'model': donor.model.title,
							'generation': donor.generation.year,
							'kuzov': donor.kuzov.title,
							'year': donor.year.title,
							'engine_type': donor.engine_type.title,
							'engine_size': donor.engine_size.title,
							'transmission': donor.transmission.title,
							'color': donor.color.title,
							'helm': donor.helm.title,
							'privod': donor.privod.title,
							'probeg': donor.probeg,
							'vin_number': donor.vin_number,
							}
		data = json.dumps(new_content_data)

		return HttpResponse(data, content_type="application/json")

def save_new_donor_params(request):
	print(request.POST)
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
		data = 'Good'
		return HttpResponse(data, content_type="application/json")

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