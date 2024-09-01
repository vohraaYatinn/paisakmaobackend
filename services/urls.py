from django.urls import path
from services.views import ServiceGet

urlpatterns = [
    path(r'get-all-active-service/', ServiceGet.as_view(), name="get-all-active-service"),
]
