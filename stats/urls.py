from django.urls import path

from .views import *

urlpatterns = [
    path('', Stats.as_view(), name='get_stats_url'),
]