from django.urls import path, include

from .views import *

urlpatterns = [
    path('', rediredct_detal_list_page),
    path('add_random_detals/', add_random_detal),
    path('add_auto/', include('add_auto.urls')),
    path('detals_list/', include('detals_list.urls')),
    path('stocks/', include(('stocks.urls', 'stocks'), namespace='stocks ')),
]