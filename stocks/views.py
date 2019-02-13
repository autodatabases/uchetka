from django.shortcuts import render

from .forms import *

# Create your views here.
def get_page(request):
	return render(request, 'stocks/index.html', context={'form_stock': SelectStock})