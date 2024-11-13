from django.contrib import admin

from services.models import ServicesType, ServicesWorking, ServiceDetails

admin.site.register(ServicesType)
admin.site.register(ServicesWorking)
admin.site.register(ServiceDetails)
