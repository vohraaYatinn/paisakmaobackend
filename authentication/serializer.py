from rest_framework import serializers
from authentication.models import User
from wallet.models import Wallet

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"

class UserWithWalletSerializer(serializers.ModelSerializer):
    wallet = WalletSerializer()

    class Meta:
        model = User
        fields = "__all__"
