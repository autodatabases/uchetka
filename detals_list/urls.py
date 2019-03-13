from django.urls import path, include

from .views import *

urlpatterns = [
    path('', DetalList.as_view()),
    path('small_filter/', small_filter),
] 

