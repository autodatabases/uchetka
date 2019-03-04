import json

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from collections import OrderedDict

from .forms import *
from lk.forms import *
from lk.models import *
from stocks.forms import *


class DetalList(View):
	# GET Запрос	
	def get(self, request):
		num_page = request.GET.get('page', 1)
		if num_page == '0': 
			num_page = 1
		return self.render_template(request, self.filter_detals(request, None), None, num_page)

	# POST Запрос
	def post(self, request):
		print(request.POST)
		params = request.POST.getlist('param_filter')
		query_result = self.filter_detals(request, params)
		selected = {'price': params[0], 'detal': params[1],	'mark': params[2], 'model': params[3], 'generation': params[4], 'number': params[5], 'stock': params[6], 'cell': params[7]}
		return self.render_template(request, query_result, selected)

	# Фильтрация деталей
	def filter_detals(self, request, params):
		company = Company.objects.filter(staff_users=request.user)
		if params == None: # Отфильтровать детали по компании
			query_result = Paginator(UserDetal.objects.filter(company=company[0]), 25)
		else: # Отфильтровать детали компании по параметрам
			query_result = Paginator(UserDetal.objects.filter(company=company[0]), 25)
		return query_result

	# Рендеринг шаблона
	def render_template(self, request, result, selected, num_page=1):
		query_result = result.page(num_page).object_list
		all_detals = query_result.count()
		print(dir(result))
		context = {'all_detals' : [{'detal': query_result[i], 'count': i+1 } for i in range(all_detals)],
				   'page': result,
				   'active_page': int(num_page),
				   'forms': {'donor': DonorForm, 
				   			 'add_stock': StockForm,
				   			 'auto_select': MarkModelGen,
				   			 'filters': {'small': SmallFilter, 'full': ''}},
				   'selected': selected,
				   'stockroom_count': Stock.objects.filter(company=(Company.objects.filter(staff_users=request.user)).count()),
				   'group_user': request.user.groups.all()[0].name}
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
			query_detals = UserDetal.objects.filter(detal=AutoDetal.objects.get(value=request.POST['filterValue']))
		
		arr_detal = []
		for elem in query_detals:
			arr_detal.append({'detal': {'title': elem.detal.title, 'value': elem.detal.value},
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