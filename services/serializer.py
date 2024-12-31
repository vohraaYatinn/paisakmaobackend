from rest_framework import serializers
from services.models import ServicesWorking, ServicesType


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesType
        fields = "__all__"


class ServiceWorkingSerializer(serializers.ModelSerializer):
    service_name = ServiceTypeSerializer()
    class Meta:
        model = ServicesWorking
        fields = "__all__"

