from django.db import transaction
import re
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
        upi = data.get('upi', False)
        upi_pattern = r'^[a-zA-Z0-9.\-_]{2,}@[a-zA-Z]{2,}$'
        if not re.match(upi_pattern, upi):
            raise Exception("Invalid UPI ID format. Please provide a valid UPI ID.")
        user_wallet = Wallet.objects.filter(user__phone_number=user)
        if user_wallet and float(amount) < float(user_wallet[0].balance) and upi:
            user_wallet[0].balance = float(user_wallet[0].balance) - float(amount)
            user_wallet[0].save()
        else:
            raise Exception("Please Ensure you have enough funds")
        return Withdrawal.objects.create(user=user_wallet[0].user, amount=amount, upi=upi)


    @staticmethod
    def get_withdraw_request(request, data):
        user = request.user.phone
        return Withdrawal.objects.filter(user__phone_number=user)[:4]

