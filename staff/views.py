import json

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.models import Group, User


from .forms import * 
from lk.models import *


class StaffPage(View):
	# GET Запрос
	def get(self, request):
		if request.user.groups.all()[0].name in ['Директор']:
			company = Company.objects.filter(staff_users=request.user)
			all_staff = company[0].staff_users.all()
			return render(request, 'staff/index.html', context={'forms': {'staff': NewStaffUser},
																'staff_users': all_staff,
																'stock_count': company[0].stocks.all().count(),
																'group_user': request.user.groups.all()[0].name})
		else:
			return redirect('/lk/')

	# POST Запрос
	def post(self, request):
		print(request.POST)
		if request.is_ajax():
			if request.POST['type'] == 'delete_user':
				data = self.delete_user(request)
			if request.POST['type'] == 'load_info':
				data = self.load_user_info(request)
			if request.POST['type'] == 'add_user':
				data = self.add_user(request)
			return HttpResponse(json.dumps(data), content_type="application/json")
		else:
			return redirect('/lk/staff/')
	
	# Загрузить информацию о сотруднике		
	def load_user_info(self, request):
		user = User.objects.get(id=request.POST['user'])
		data = [{'param': str(user.first_name)},
				{'param': str(user.username)},
				{'param': str(user.email)},
				{'param': str(user.groups.all()[0].name)},
				{'param': 'Авторазбор №1'}]
		return data

	# Добавить сотрудника
	def add_user(self, request):
		bound_form = NewStaffUser(request.POST)
		if bound_form.is_valid():
			print('good')
			user = User.objects.create_user(username=bound_form.cleaned_data['staff_login'],
											email=bound_form.cleaned_data['staff_email'],
											password=bound_form.cleaned_data['staff_password'],
											first_name=bound_form.cleaned_data['staff_fio'])
			user.save()
			user.groups.add(Group.objects.get(name=bound_form.cleaned_data['staff_group']))
			company = Company.objects.filter(staff_users=request.user)
			company[0].staff_users.add(user)
		return {'newuser_id': str(user.pk), 'newuser_name': user.first_name}

	# Удалить сотрудника
	def delete_user(self, request):
		try:
			user = User.objects.get(id=request.POST['user'])
			if user == request.user:
				data = {'user_id': 'Not delete login user'}
				return data
			else:
				user.delete()
				data = {'user_id': request.POST['user']}
				return data
		except User.DoesNotExist:
			data = {'user_id': 'Not found'}
			return data