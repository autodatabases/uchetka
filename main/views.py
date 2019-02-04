from django.shortcuts import redirect, render

from lk.models import *
# Create your views here.

def redirect_lk(request):
	return redirect('/lk/')


def load_mark(request):
	with open ('AutoBase/all_marks.txt', 'r', encoding='utf-8') as file:
		all_marks = file.readlines()
		for mark in all_marks:
			data_mark =  eval(mark)
			print(data_mark['mark'])
			AutoMark.objects.get_or_create(title=data_mark['mark'],
											 value=data_mark['value'])
	return render(request, 'lk/index.html')

def load_model(request):
	with open ('AutoBase/all_marks.txt', 'r', encoding='utf-8') as file:
		all_marks = file.readlines()
	for mark in all_marks:
		data_mark =  eval(mark)
		mark_obj = AutoMark.objects.get(value=data_mark['value'])
		with open('AutoBase/'+ data_mark['mark'] +'/all_models.txt', 'r', encoding='utf-8') as models_file:
			all_models = models_file.readlines()
		for model in all_models:
			data_model = eval(model)
			print(data_mark['mark'], data_model['title'], mark_obj)
			AutoModel.objects.get_or_create(title=data_model['title'],
										    value=data_model['value'],
										    mark=mark_obj)
	return render(request, 'lk/index.html')

def load_gen(request):
	with open ('AutoBase/all_marks.txt', 'r', encoding='utf-8') as file:
		all_marks = file.readlines()
	for mark in all_marks:
		data_mark =  eval(mark)
		mark_obj = AutoMark.objects.get(value=data_mark['value'])
		with open('AutoBase/'+ data_mark['mark'] +'/all_models.txt', 'r', encoding='utf-8') as models_file:
			all_models = models_file.readlines()
		for model in all_models:
			data_model = eval(model)
			model_obj = AutoModel.objects.get(value=data_model['value'],
											  mark=mark_obj)
			try:
				with open('AutoBase/'+ data_mark['mark'] +'/' + data_model['title'] + '/all_generations.txt', 'r', encoding='utf-8') as gen_file:
					all_generations = gen_file.readlines()
			except FileNotFoundError:
				continue
			for gen in all_generations:
				data_gen = eval(gen)

				print(data_gen['title'].replace(data_gen['year'], '').strip(), data_gen['year'], data_gen['year'].replace('гг.', '').replace('н.в. ', 'n.v.').replace(' ', '').replace('-', '_'))
				AutoGeneration.objects.get_or_create(title=data_gen['title'].replace(data_gen['year'], '').strip(),
											    	 value=data_gen['year'].replace('гг.', '').replace('н.в. ', 'n.v.').replace(' ', '').replace('-', '_'),
											    	 year=data_gen['year'].strip(),
											    	 model=model_obj)
	return render(request, 'lk/index.html')

def load_data(request):
	colors = [{'title':'0.7', 'value': '0.7'},
			  {'title':'0.8', 'value': '0.8'},
			  {'title':'1.0', 'value': '1.0'},
			  {'title':'1.1', 'value': '1.1'},
			  {'title':'1.2', 'value': '1.2'},
			  {'title':'1.3', 'value': '1.3'},
			  {'title':'1.4', 'value': '1.4'},
			  {'title':'1.5', 'value': '1.5'},
			  {'title':'1.6', 'value': '1.6'},
			  {'title':'1.7', 'value': '1.7'},
			  {'title':'1.8', 'value': '1.8'},
			  {'title':'1.9', 'value': '1.9'},
			  {'title':'2.0', 'value': '2.0'},
			  {'title':'2.2', 'value': '2.2'},
			  {'title':'2.3', 'value': '2.3'},
			  {'title':'2.4', 'value': '2.4'},
			  {'title':'2.5', 'value': '2.5'},
			  {'title':'2.7', 'value': '2.7'},
			  {'title':'2.8', 'value': '2.8'},
			  {'title':'3.0', 'value': '3.0'},
			  {'title':'3.2', 'value': '3.2'},
			  {'title':'3.3', 'value': '3.3'},
			  {'title':'3.5', 'value': '3.5'},
			  {'title':'3.6', 'value': '3.6'},
			  {'title':'4.0', 'value': '4.0'},
			  {'title':'4.2', 'value': '4.2'},
			  {'title':'4.4', 'value': '4.4'},
			  {'title':'4.5', 'value': '4.5'},
			  {'title':'4.6', 'value': '4.6'},
			  {'title':'4.7', 'value': '4.7'},
			  {'title':'5.0', 'value': '5.0'},
			  {'title':'5.5', 'value': '5.5'},
			  {'title':'5.7', 'value': '5.7'},
			  {'title':'6.0', 'value': '6.0'}]

	for color in colors:
		print(color['title'], color['value'])
		# AutoEngineSize.objects.get_or_create(title=color['title'], value=color['value'])
	return render(request, 'lk/index.html')
