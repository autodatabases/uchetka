from django.urls import path, include

from .views import *

urlpatterns = [
    path('', StaffPage.as_view(), name='get_page'),
]