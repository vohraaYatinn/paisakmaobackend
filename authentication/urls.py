from django.urls import path
from authentication.views import OtpVerification, SignupApi, getDashboardData, fetchMyReferrals, ChangeProfilePhoto

urlpatterns = [
    path(r'phone-otp-send/', OtpVerification.as_view(), name="phone_otp_send"),
    path(r'phone-otp-verify/', OtpVerification.as_view(), name="phone_otp_verify"),
    path(r'phone-signup/', SignupApi.as_view(), name="phone-signup"),
    path(r'change-profile-photo/', ChangeProfilePhoto.as_view(), name="change-profile-photo"),
    path(r'fetch-main-data/', getDashboardData.as_view(), name="fetch-main-data"),
    path(r'fetch-my-referrals/', fetchMyReferrals.as_view(), name="fetch-my-referrals"),
    path(r'fetch-my-referrals/', fetchMyReferrals.as_view(), name="fetch-my-referrals"),
]

