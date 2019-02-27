from django.contrib import admin

from .models import * 
# Register your models here.
myModels = [AutoMark, AutoModel, AutoGeneration, AutoDetal, AutoKuzov, AutoYearProduction,
		    AutoEngineType, AutoEngineSize, AutoTransmission, AutoColor, AutoDonor, UserDetal,
		    AutoHelm, AutoPrivod, Stock, Photo, Company]
admin.site.register(myModels)