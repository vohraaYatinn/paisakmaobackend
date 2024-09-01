from django.urls import path
from wallet.views import WalletGet, WithdrawRequest, ApplyWithdrawRequest

urlpatterns = [

    path(r'notification-get/', WalletGet
         .as_view(), name="notification-get"),
    path(r'withdraw-request/', WithdrawRequest
         .as_view(), name="withdraw-request"),
    path(r'apply-withdraw-request/', ApplyWithdrawRequest
         .as_view(), name="apply-withdraw-request"),

]
