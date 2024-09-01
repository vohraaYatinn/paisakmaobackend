from django.urls import path
from banner.views import BannerView
from referral.views import AddLeadToSms, getLeadsUser

urlpatterns = [

    path(r'add-lead/', AddLeadToSms
         .as_view(), name="add-lead"),
    path(r'get-leads-user/', getLeadsUser
         .as_view(), name="get-leads-user"),

]
