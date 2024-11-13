from rest_framework import serializers

from authentication.models import User, ManageKyc
from banner.models import Banner, SuccessStory
from referral.models import Referral, LeadsUsers
from services.models import ServicesType, ServicesWorking
from wallet.models import Wallet, Withdrawal


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class ReferredUserSerializer(serializers.ModelSerializer):
    referred_user = UserSerializer()
    class Meta:
        model = Referral
        fields = "__all__"

class walletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"


class UserSerializerWithWallet(serializers.ModelSerializer):
    wallet = walletSerializer()
    class Meta:
        model = User
        fields = "__all__"


class KycSerializerWithUser(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = ManageKyc
        fields = "__all__"



class WithdrawSerializerWithUser(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Withdrawal
        fields = "__all__"



class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesType
        fields = "__all__"



class OfferServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesWorking
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class StoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccessStory
        fields = "__all__"



class LeadsWithUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = LeadsUsers
        fields = "__all__"

