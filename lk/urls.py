from django.urls import path, include

from .views import *

urlpatterns = [
    path('', rediredct_detal_list),
    path('add_stockroom/', add_StockRoom),
    path('add_auto/', include('add_auto.urls')),
    path('detals_list/', include('detals_list.urls')),
]