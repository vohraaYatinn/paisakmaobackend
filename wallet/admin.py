from django.contrib import admin
from wallet.models import Wallet, EarningDetail, Withdrawal

admin.site.register(Wallet)
admin.site.register(EarningDetail)
admin.site.register(Withdrawal)
