from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', RegCompany.as_view(), name='reg_company_url'),
    path('', AuthUser.as_view(), name='auth_user_url'),
    path('lk/', include('lk.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
