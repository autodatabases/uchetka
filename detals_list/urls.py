from django.urls import path, include

from .views import *

urlpatterns = [
    path('', get_detals_list_page),
    path('load_donor/', get_donor_page),
    path('save_donor/', save_new_donor_params),
    path('small_filter/', small_filter),
] 

