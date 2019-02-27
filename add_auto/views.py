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

	return render(request, 'add_auto/index.html')
