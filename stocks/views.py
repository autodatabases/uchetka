from django.shortcuts import render

# Create your views here.
def get_page(request):
	return render(request, 'stocks/index.html')