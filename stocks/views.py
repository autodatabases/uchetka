from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import *
from lk.models import *

def get_page(request):
	return render(request, 'stocks/index.html', context={'form_stock': SelectStock})

def create_stock(request):
	bound_form = StockForm(request.POST)
	if bound_form.is_valid():
		bound_form.cleaned_data.update({'account': request.user, 'value': len(Stock.objects.filter(account=request.user))+1})
		bound_form.save()
	return redirect('/lk/stocks/')