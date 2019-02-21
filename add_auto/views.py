import json

from django.shortcuts import render, redirect
from django.http import HttpResponse

from lk.models import *
from lk import models as modellls

def select_auto(request):
	if request.is_ajax():
		print(request.POST)
		if 'selectedMark' in request.POST:
			selectedMark = request.POST['selectedMark']
			mark_obj = AutoMark.objects.get(value=selectedMark)
			query_models = AutoModel.objects.filter(mark=mark_obj)
			models_dict = []
			for model in query_models:
				models_dict.append({'title': model.title, 'value': model.value})
			data = json.dumps({'models': models_dict})
		if 'selectedModel' in request.POST:
			selectedModel = request.POST['selectedModel']
			model_obj = AutoModel.objects.get(value=selectedModel)
			query_generations = AutoGeneration.objects.filter(model=model_obj)
			generations_dict = []
			for gen in query_generations:
				generations_dict.append({'title': gen.year, 'value': gen.value})
			data = json.dumps({'generations': generations_dict})
		return HttpResponse(data, content_type="application/json")

def get_addauto_page(request):
	print(request.POST)
	selectedMark = AutoMark.objects.get(value=request.POST['mark'])
	selectedModel = AutoModel.objects.get(value=request.POST['model'], 
			   							  mark=selectedMark)
	selectedGeneration = AutoGeneration.objects.get(value=request.POST['generation'],
											   		model=selectedModel)
	new_donor = AutoDonor()
	new_donor.mark = selectedMark
	new_donor.model = selectedModel
	new_donor.generation = selectedGeneration
	new_donor.kuzov = AutoKuzov.objects.get(value='noselect')
	new_donor.year = AutoYearProduction.objects.get(value='noselect')
	new_donor.engine_type = AutoEngineType.objects.get(value='noselect')
	new_donor.engine_size = AutoEngineSize.objects.get(value='noselect')
	new_donor.transmission = AutoTransmission.objects.get(value='noselect')
	new_donor.color = AutoColor.objects.get(value='noselect')
	new_donor.helm = AutoHelm.objects.get(value='noselect')
	new_donor.privod = AutoPrivod.objects.get(value='noselect')
	new_donor.probeg = 0
	new_donor.vin_number = ''
	new_donor.save()
	context = {'all_detals': AutoDetailTest.objects.all(), 'selectedMark': selectedMark,
			   'selectedModel': selectedModel, 'selectedGeneration': selectedGeneration,
			   'all_kuzovs': AutoKuzov.objects.all(),'all_years': AutoYearProduction.objects.all(),
			   'all_engine_type': AutoEngineType.objects.all(),'all_engine_size': AutoEngineSize.objects.all(),
			   'all_kpp': AutoTransmission.objects.all(),'all_color': AutoColor.objects.all(),
			   'all_helm': AutoHelm.objects.all(),'all_privod': AutoPrivod.objects.all(),
			   'new_donor': new_donor, 'all_stockrooms': Stock.objects.all()}
	return render(request, 'add_auto/index.html', context=context)

def add_detals(request):
	print(request.POST)
	for detal in request.POST:
		if 'checkbox' in detal:
			print({'detal': AutoDetailTest.objects.get(value=detal.split('_')[0]),
				   'donor': AutoDonor.objects.get( pk = len(AutoDonor.objects.all()) ),
				   'price': request.POST[detal.split('_')[0]+'_price'],
				   'info': request.POST[detal.split('_')[0]+'_info']})
			print(AutoDetailTest.objects.get(value=detal.split('_')[0]))
			UserDetal.objects.get_or_create(detail=AutoDetailTest.objects.get(value=detal.split('_')[0]),
											donor_info=AutoDonor.objects.get(pk = request.POST['idDonor']),
									    	price=int(request.POST[detal.split('_')[0]+'_price']),
									    	description=request.POST[detal.split('_')[0]+'_info'], 
									    	stockroom=Stock.objects.get(pk=request.POST['selectStock']),
										    account=request.user)

	return redirect('/lk/detals_list/')