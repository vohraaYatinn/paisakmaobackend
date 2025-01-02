import random

from django.db import transaction

from authentication.models import User
from notification.models import Notification
from referral.models import LeadsUsers
from services.models import ServicesWorking


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


    @staticmethod
    def add_lead_list_from_domain(request, data):
        fullName = data.get('fullName')
        email = data.get('email')
        phone = data.get('phone')
        date = data.get('date')
        serviceType = data.get('serviceType')
        senderId = data.get('senderId')
        serviceName = data.get('serviceName')
        compaignId = data.get('compaignId')
        tokenNumber = data.get('tokenNumber')
        price = data.get('price')
        service_compaign = ServicesWorking.objects.filter(id=compaignId)
        if not service_compaign:
            raise Exception("Something wrong with service compaign")

        try:
            req_user = User.objects.get(id=senderId)
        except:
            raise Exception("There is something wrong with the url")

        LeadsUsers.objects.create(user=req_user,customer_email=email,customer_name=fullName,customer_number=phone, type=serviceType, price=service_compaign[0].earnings, service_name= service_compaign[0].service_name.service_name, compaign_id=compaignId, unique_id=tokenNumber)
        return service_compaign[0].link
