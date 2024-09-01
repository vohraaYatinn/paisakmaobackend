from rest_framework import serializers

from referral.models import LeadsUsers


class LeadsUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadsUsers
        fields = "__all__"

