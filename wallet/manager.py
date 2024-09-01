from django.db import transaction

from wallet.models import Wallet, Withdrawal


class WalletManager:
    @staticmethod
    def get_wallet_info(data):
        user = data.get('user', None)
        return Wallet.objects.filter(user=user).order_by("-created_at")

    @staticmethod
    @transaction.atomic
    def apply_withdraw_request(request, data):
        user = request.user.phone
        amount = data.get('amount', 0)
        user_wallet = Wallet.objects.filter(user__phone_number=user)
        if user_wallet:
            user_wallet[0].balance = float(user_wallet[0].balance) - float(amount)
            user_wallet[0].save()
        return Withdrawal.objects.create(user=user_wallet[0].user, amount=amount)


    @staticmethod
    def get_withdraw_request(request, data):
        user = request.user.phone
        return Withdrawal.objects.filter(user__phone_number=user)[:4]

