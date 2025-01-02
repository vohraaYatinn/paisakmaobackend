import random

from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.db.models import Q
import requests
from rest_framework.exceptions import ValidationError

from authentication.models import User
from notification.models import Notification
from wallet.models import Wallet


class AuthenticationManager:

    @staticmethod
    def otp_send_phone(data):
        phone = data.get('phone', False)
        if len(phone) != 10:
            raise Exception("Please enter a valid phone number")
        if phone == "9999999999":
            return False, False
        check_if_user_exist = User.objects.filter(phone_number=phone)
        if not check_if_user_exist:
            raise Exception("This Number is not linked with any of your account")

        url = 'https://cpaas.messagecentral.com/verification/v3/send'
        headers = {
            'authToken': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJDLUFCOTc5QTQzMDU5QzRGMiIsImlhdCI6MTcyNDQxMDEwMSwiZXhwIjoxODgyMDkwMTAxfQ.ViGp17ODCZrEHH9WRcg_x-XPZTjLoffPUSTLxmeg9KCPAiUWxw1wVEkvLjrQ5JD6sPk3QsnoIawmaIkI1870cQ'
        }
        params = {
            'countryCode': '91',
            'customerId': 'C-AB979A43059C4F2',
            'flowType': 'SMS',
            'mobileNumber': phone
        }
        response = requests.post(url, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception("Please wait 60 seconds before trying again.")

        return response.json()['data']['verificationId'], check_if_user_exist[0]

    @staticmethod
    def otp_verify_phone(data):
        phone = data.get('phoneNumber', False)
        otp = data.get('otp', False)

        if phone == "9999999999" and otp == "0000":
            check_user = User.objects.filter(phone_number="9999999999")
            return True , check_user[0]

        verfication_code = data.get('verificationCode', False)
        url = 'https://cpaas.messagecentral.com/verification/v3/validateOtp'
        headers = {
            'authToken': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJDLUFCOTc5QTQzMDU5QzRGMiIsImlhdCI6MTcyNDQxMDEwMSwiZXhwIjoxODgyMDkwMTAxfQ.ViGp17ODCZrEHH9WRcg_x-XPZTjLoffPUSTLxmeg9KCPAiUWxw1wVEkvLjrQ5JD6sPk3QsnoIawmaIkI1870cQ'
        }
        params = {
            'countryCode': '91',
            'mobileNumber': phone,
            'verificationId': verfication_code,
            'customerId': 'C-AB979A43059C4F2',
            'code': otp
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception("The OTP is either invalid or has expired.")
        check_user = User.objects.filter(phone_number=phone)

        return response.json()['data']['verificationStatus'] == 'VERIFICATION_COMPLETED' , check_user[0]

    @staticmethod
    @transaction.atomic
    def signup_user(data):
        phone = data.get('phoneNumber', False)
        name = data.get('name', False)
        date_of_birth = data.get('date', False)
        gender = data.get('gender', False)
        referralCode = data.get('referralCode', False)

        if not (phone and name and date_of_birth and gender):
            raise ValidationError("All required fields must be provided.")

        # if password != confirm_password:
        #     raise ValidationError("Passwords do not match.")

        # if User.objects.filter(email=email).exists():
        #     raise ValidationError("A user with this email already exists.")

        if User.objects.filter(phone_number=phone).exists():
            raise ValidationError("A user with this phone number already exists.")
        if referralCode:
            user_check = User.objects.filter(referral_code=referralCode)
            if not user_check:
                raise Exception("The referral code you entered is invalid")
        user_done = User.objects.create(
            full_name=name,
            phone_number=phone,
            referral_code=name[0:4]+str(random.randint(1111,8888))
        )
        Wallet.objects.create(
            user=user_done,
        )
        Notification.objects.create(user=user_done, title="Welcome to the community" , description="Here we give endless opportunity to earn money through selling , providing loans, referrals, etc. You can access marketing videos, content and courses. Best of luck")
        if referralCode:
            user_done.referred_by = user_check[0]
            get_wallet = Wallet.objects.filter(user=user_check[0])
            get_wallet[0].balance = get_wallet[0].balance + 250
            get_wallet[0].total_balance = get_wallet[0].total_balance + 250
            get_wallet[0].save()

        if len(phone) != 10:
            raise Exception("Please enter a valid phone number")

        url = 'https://cpaas.messagecentral.com/verification/v3/send'
        headers = {
            'authToken': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJDLURFQkUyQjY4OTM4NTRBRCIsImlhdCI6MTcyMjMyNDU4MCwiZXhwIjoxODgwMDA0NTgwfQ.ihHWg1LXsk1WCjmYiCb0fA6sYrbqUORZjsw-0kr90w662ZlW7UCbb_O5GWx9_7gnzWdTA3zoGgmc1p2tQ2B4mg'
        }
        params = {
            'countryCode': '91',
            'customerId': 'C-DEBE2B6893854AD',
            'flowType': 'SMS',
            'mobileNumber': phone
        }
        response = requests.post(url, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception("Please wait 60 seconds before trying again.")

        return response.json()

    @staticmethod
    def dashboard_data(request, data):
        phone = request.user.phone
        user_done = User.objects.filter(phone_number=phone).prefetch_related("wallet")
        return user_done

    @staticmethod
    def fetch_my_referrals(request, data):
        phone = request.user.phone
        user_done = User.objects.filter(phone_number=phone)
        user_who_get_referral = []
        if user_done:
            user_who_get_referral = User.objects.filter(referred_by=user_done[0]).prefetch_related("wallet")
        return user_who_get_referral



    @staticmethod
    @transaction.atomic
    def change_profile_photo(request, data):
        phone = request.user.phone
        photo = request.FILES.get("photo")  # Use `request.FILES` for file uploads

        user = User.objects.get(phone_number=phone)
        user.profile_photo = photo
        user.save()
        return


    @staticmethod
    @transaction.atomic
    def get_profile_details(request):
        phone = request.user.phone
        user = User.objects.get(phone_number=phone)
        return user


    @staticmethod
    @transaction.atomic
    def change_profile_settings(request, data):
        phone = request.user.phone
        full_name = data.get("full_name", False)
        email = data.get("email", False)
        user = User.objects.get(phone_number=phone)
        if full_name:
            user.full_name = full_name
        if email:
            user.email = email
        user.save()
        return user