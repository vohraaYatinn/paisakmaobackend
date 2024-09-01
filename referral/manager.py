import random

from django.db import transaction

from authentication.models import User
from notification.models import Notification
from referral.models import LeadsUsers


class ReferralManager:
    @staticmethod
    @transaction.atomic()
    def send_otp_to_lead(request, data):
        user = request.user.phone
        req_user = User.objects.get(phone_number=user)
        service_type = data.get('service_type')
        customer_number = data.get('customer_number')
        service_name = data.get('service_name')
        price = 250
        otp = 1023
        check_one = LeadsUsers.objects.filter(user=req_user, customer_number=customer_number, type=service_type, price=price,
                                  service_name=service_name, otp_to_verify=otp)
        if check_one:
            for i in check_one:
                i.delete()
        return LeadsUsers.objects.create(user=req_user,customer_number=customer_number, type=service_type, price=price, service_name= service_name)

    @staticmethod
    def verify_lead(request, data):
        user = request.user.phone
        service_type = data.get('service_type')
        customer_number = data.get('customer_number')
        # otp_customer = data.get('otp_customer')
        service_name = data.get('service_name')
        lead = LeadsUsers.objects.filter(user__phone_number=user,customer_number=customer_number, status="unverified", service_type=service_type, service_name=service_name, otp_to_verify =otp_customer)
        if lead:
            lead[0].status = "pending"
            lead[0].save()
        else:
            raise Exception("We cannot verify this lead, Please try again later")

    @staticmethod
    def get_leads_list(request, data):
        user = request.user.phone
        lead = LeadsUsers.objects.filter(user__phone_number=user)
        return lead