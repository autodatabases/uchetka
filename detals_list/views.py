import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from collections import OrderedDict

from lk.forms import *
from stocks.forms import *
from lk.models import *


class DetalList(View):
	# Рендеринг шаблона
	def render_template(self, request, query_result, selected):
		all_result = query_result.count()
		context = {'all_detals' : [{'detal': query_result[i], 'count': i+1 } for i in range(all_result)],
				   'filter_values': {'detal': AutoDetailTest.objects.all(), 'mark': AutoMark.objects.all(), 'stock': Stock.objects.all()},
				   'selected': selected,
				   'form_donor': DonorForm, 
				   'form_stock': StockForm,
				   'stockroom_count': Stock.objects.filter(account=request.user).count()}
		return render(request, 'detals_list/index.html', context=context)

	# GET Запрос	
	def get(self, request):
		query_result = UserDetal.objects.filter(account=request.user)[:25]
		return self.render_template(request, query_result, None)

	# POST Запрос
	def post(self, request):
		params = request.POST.getlist('param_filter')
		selected = {'price': params[0], 'detal': params[1],	'mark': params[2], 'model': params[3], 'generation': params[4], 'number': params[5], 'stock': params[6], 'cell': params[7]}
		return self.render_template(request, self.filter_detals(request, params), selected)

	# Фильтрация деталей
	def filter_detals(self, request, params):
		query_result = UserDetal.objects.filter(account=request.user)[:25]
		return query_result

	
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