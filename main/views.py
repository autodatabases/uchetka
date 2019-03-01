from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import View

from lk.models import *
from .forms import * 
# Create your views here.

class AuthUser(View):
	# GET Запрос
	def get(self, request):
		if request.user.is_authenticated:
			return redirect('/lk/')
		else:
			return render(request, 'lk/auth-page.html')
	# POST Запрос
	def post(self, request):
		print(request.POST)
		user = authenticate(username=request.POST['login'], password=request.POST['pass'])
		if user is not None:
			# the password verified for the user
			if user.is_active:
				print("User is valid, active and authenticated")
				login(request, user)
				return redirect('/lk/')
			else:
				print("The password is valid, but the account has been disabled!")
				return render(request, 'lk/auth-page.html')
		else:
			# the authentication system was unable to verify the username and password
			print("The username and password were incorrect.")
			return render(request, 'lk/auth-page.html')


class RegCompany(View):
	# GET Запрос
	def get(self, request):
		return render(request, 'lk/registration.html', context={'forms': {'reg': RegForm}})
	# POST Запрос
	def post(self, request):
		print(request.POST)
		bound_form = RegForm(request.POST)
		if bound_form.is_valid():
			print(bound_form.cleaned_data)
			user = User.objects.create_user(username=bound_form.cleaned_data['director_login'],
											email=bound_form.cleaned_data['director_email'],
											password=bound_form.cleaned_data['director_password'])
			user.save()
			company = Company.objects.create(title=bound_form.cleaned_data['company_title'],
											 country=bound_form.cleaned_data['company_country'],
											 region=bound_form.cleaned_data['company_region'],
											 city=bound_form.cleaned_data['company_city'])
			company.save()
			company.staff_users.add(user)
			login(request, user)
			print(Company.objects.all())
		return redirect('/lk/')
		