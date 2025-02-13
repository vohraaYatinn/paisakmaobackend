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
        bank_name = data.get('bank_name', '').strip()
        account_number = data.get('account_number', '').strip()
        ifsc_code = data.get('ifsc_code', '').strip()

        # Validate IFSC code format (Assuming standard Indian IFSC format)
        if not re.match(r'^[A-Z]{4}0[A-Z0-9]{6}$', ifsc_code):
            raise Exception("Invalid IFSC Code format. Please provide a valid IFSC Code.")

        # Validate bank details are not empty
        if not bank_name or not account_number or not ifsc_code:
            raise Exception("Bank name, account number, and IFSC code are required.")

        # Check user wallet balance
        user_wallet = Wallet.objects.filter(user__phone_number=user).first()
        if not user_wallet or float(amount) > float(user_wallet.balance):
            raise Exception("Please ensure you have enough funds.")

        # Deduct amount from wallet
        user_wallet.balance = float(user_wallet.balance) - float(amount)
        user_wallet.save()

        # Create withdrawal request
        return Withdrawal.objects.create(
            user=user_wallet.user,
            amount=amount,
            bank_name=bank_name,
            account_number=account_number,
            ifsc_code=ifsc_code
        )

    @staticmethod
    def get_withdraw_request(request, data):
        user = request.user.phone
        return Withdrawal.objects.filter(user__phone_number=user).order_by("-requested_at")

