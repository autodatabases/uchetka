import json
import requests

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
		company = Company.objects.filter(staff_users=request.user)
		detals_company = UserDetal.objects.filter(company=company[0])
		query_result = Paginator(detals_company, 25)
		if request.is_ajax():
			data =  self.load_ajax_page(num_page)
			return HttpResponse(json.dumps(data), content_type="application/json")
		else:
			return self.render_template(request, query_result, num_page)

	# POST Запрос
	def post(self, request):
		print(request.POST)
		if request.is_ajax():
			if request.POST['type'] == 'load_cats':
				data = self.load_cats(request)
			return HttpResponse(json.dumps(data), content_type="application/json")
		else:
			query_result = self.filter_detals(request)
			return self.render_template(request, query_result)

	# Фильтрация деталей
	def filter_detals(self, request):
		company = Company.objects.filter(staff_users=request.user)
		detals_company = UserDetal.objects.filter(company=company[0])
		if request.POST['detal'] != 'noselect':
			detals_company = detals_company.filter(detal__value=request.POST['detal'])
		if request.POST['mark'] != 'noselect':
			donor =AutoDonor.objects.filter(mark__value=request.POST['mark'])
			detals_company = detals_company.filter(donor_info__in=donor)
		# if request.POST['model'] != 'noselect':
		# 	detals_company = detals_company.filter(donor_info__model=AutoModel.objects.get(value=request.POST['model']))		
		# if request.POST['generation'] != 'noselect':
		# 	detals_company = detals_company.filter(donor_info__generation=AutoGeneration.objects.get(value=request.POST['generation']))		
		# if request.POST['number'] != 'noselect':
		# 	pass
		# if request.POST['stock'] != 'noselect':	
		# 	detals_company = detals_company.filter(stockroom=Stock.objects.get(pk=request.POST['stock']))	
		# if request.POST['stock_param'] != 'noselect':
		# 	pass	
		return Paginator(detals_company, 25)

	# Подгрузка страниц 
	def load_ajax_page(self, num_page):
		data = {'new_detals': [{'title': elem.detal.title,
							    'donor': {'mark': elem.donor_info.mark.title,
							 		      'model': elem.donor_info.model.title,
							 		      'generation': elem.donor_info.generation.title},
							    'price': elem.price,
							    'description': elem.description,
							    'stockroom': elem.stockroom.title,
		} for elem in query_result.page(num_page).object_list ] }
		return data

	# Подгрузка каталогов
	def load_cats(self, request):
		data = {'key':'283R8Q8ckCYq9cyQSgYiXDpYFguSf7ox', 'group': 'passenger'}
		if request.POST['cat'] == 'getModels':
			data.update({'act': 'getModels', 'make': request.POST['mark']})
		if request.POST['cat'] == 'getCars':
			data.update({'act': 'getCars', 'make': request.POST['mark'], 'model': request.POST['model']})
		r = requests.post('https://partsapi.ru/api.php', data=data)
		return json.loads(r.content)

	# Рендеринг шаблона
	def render_template(self, request, result, num_page=1):
		query_result = result.page(num_page).object_list
		all_detals = query_result.count()
		context = {'all_detals' : [{'detal': query_result[i], 'count': i+1 } for i in range(all_detals)],
				   'page': result,
				   'active_page': int(num_page),
				   'forms': {'donor': DonorForm, 
				   			 'add_stock': StockForm,
				   			 'auto_select': MarkModelGen,
				   			 'filters': {'small': SmallFilter, 'full': ''}},
				   'selected': '',
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