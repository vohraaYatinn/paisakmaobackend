from django.urls import path
from services.views import ServiceGet, GetServicesByName

urlpatterns = [
    path(r'get-all-active-service/', ServiceGet.as_view(), name="get-all-active-service"),

    # //users
    path(r'get-user-service-by-name/', GetServicesByName.as_view(), name="get-user-service-by-name"),
]
