from django.urls import path, include

from .views import *

urlpatterns = [
    path('', get_lk_page),
    path('add_stockroom/', add_StockRoom),
    path('add_auto/', include('add_auto.urls')),
    path('detals_list/', include('detals_list.urls')),
]