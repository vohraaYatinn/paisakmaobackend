from django.urls import path
from adminpannel.views import AdminView, fetchReferralAmount, UserManagement, UserReferralManagement, BanUserManagement, \
    DeleteUserManagement, KycRequest, WithdrawRequests, ServicesManagement, ActionServicesManagement, BannerUpdate, \
    SuccessStoryUpdate, GetOffersRelatedToServices, ActionOnOffersRelatedToServices, SingleKycRequest, \
    GetBannerSuccessImages, FetchDashboard, LeadsManagement

urlpatterns = [
    path(r'admin-login/', AdminView.as_view(), name="banner-post-admin"),
    path(r'fetch-referral-amount/', fetchReferralAmount.as_view(), name="fetch-referral-amount"),
    path(r'change-referral-amount/', fetchReferralAmount.as_view(), name="change-referral-amount"),
    path(r'get-all-users/', UserManagement.as_view(), name="get-all-users"),
    path(r'get-user-referrals/', UserReferralManagement.as_view(), name="get-user-referrals"),
    path(r'ban-user/', BanUserManagement.as_view(), name="ban-user"),
    path(r'delete-user/', DeleteUserManagement.as_view(), name="delete-user"),
    path(r'kyc-request/', KycRequest.as_view(), name="kyc-request"),
    path(r'single-kyc-request/', SingleKycRequest.as_view(), name="single-kyc-request"),
    path(r'action-kyc-request/', KycRequest.as_view(), name="action-kyc-request"),
    path(r'withdraw-management/', WithdrawRequests.as_view(), name="withdraw-management"),
    path(r'withdraw-action/', WithdrawRequests.as_view(), name="withdraw-action"),
    path(r'get-services/', ServicesManagement.as_view(), name="get-services"),
    path(r'add-services/', ServicesManagement.as_view(), name="add-services"),
    path(r'remove-services/', ActionServicesManagement.as_view(), name="remove-services"),
    path(r'get-offers-related-to-service/', GetOffersRelatedToServices.as_view(), name="get-offers-related-to-service"),
    path(r'add-offers-related-to-service/', GetOffersRelatedToServices.as_view(), name="add-offers-related-to-service"),
    path(r'remove-offers-related-to-service/', ActionOnOffersRelatedToServices.as_view(), name="remove-offers-related-to-service"),
    path(r'get-banner-stories-images/', GetBannerSuccessImages.as_view(), name="get-banner-stories-images"),
    path(r'banner-update/', BannerUpdate.as_view(), name="banner-update"),
    path(r'success-story/', SuccessStoryUpdate.as_view(), name="success-story"),
    path(r'fetch-dashboard/', FetchDashboard.as_view(), name="fetch-dashboard"),
    path(r'leads-management-dashboard/', LeadsManagement.as_view(), name="leads-management-dashboard"),
]

