from django.urls import path
from banner.views import BannerView
from referral.views import AddLeadToSms, getLeadsUser, addDomainListLead

urlpatterns = [

    path(r'add-lead/', AddLeadToSms
         .as_view(), name="add-lead"),
    path(r'get-leads-user/', getLeadsUser
         .as_view(), name="get-leads-user"),
    path(r'add-leads-from-inquiry/', addDomainListLead
         .as_view(), name="add-leads-from-inquiry"),

]
