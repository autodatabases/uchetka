from django.contrib import admin

from .models import * 
# Register your models here.
myModels = [AutoMark, AutoModel, AutoGeneration, AutoDetailTest, AutoKuzov, AutoYearProduction,
		    AutoEngineType, AutoEngineSize, AutoTransmission, AutoColor, AutoDonor, UserDetal,
		    AutoHelm, AutoPrivod, Stock]
admin.site.register(myModels)