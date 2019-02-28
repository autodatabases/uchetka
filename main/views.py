from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.views.generic import View

from lk.models import *
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
		return render(request, 'lk/registration.html')
	# POST Запрос
	def post(self, request):
		print(request.POST)
		