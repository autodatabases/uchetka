from django.urls import path, include

from .views import *

urlpatterns = [
    path('', get_page, name='get_page'),
]