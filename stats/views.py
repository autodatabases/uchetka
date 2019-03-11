from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class Stats(View):
	def get(self, request):
		return render(request, 'stats/index.html')