import random
from django.db import transaction
from authentication.models import User
from notification.models import Notification
from referral.models import LeadsUsers
from services.models import ServicesWorking


class ServiceManager:
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
    def get_services_by_name(request, data):
        service_type = data.get('service_type')
        data = ServicesWorking.objects.filter(service_name__service_name__icontains=service_type).select_related("service_name")
        return data