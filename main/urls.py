from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_lk),
    path('lk/', include('lk.urls')),
    path('load_data/', load_data),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)