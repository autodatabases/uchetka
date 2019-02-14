from django.urls import path, include

from .views import *

urlpatterns = [
    path('', get_page),
    path('load_donor/', get_donor_data),
    path('save_donor/', save_donor_data),
    path('small_filter/', small_filter),
] 

