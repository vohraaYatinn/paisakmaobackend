from rest_framework import serializers
from services.models import ServicesWorking


class ServiceWorkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesWorking
        fields = "__all__"

