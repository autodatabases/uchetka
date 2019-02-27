from django.urls import path, include

from .views import *

urlpatterns = [
    path('', get_addauto_page),
    path('select_auto/', select_auto),
]