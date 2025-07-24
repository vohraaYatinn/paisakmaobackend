from django.db.models import Q

from rest_framework.exceptions import ValidationError
from adminpannel.models import AdminLogin
from authentication.models import User, ManageKyc
from banner.models import Banner, SuccessStory
from referral.models import ReferralAdminPricing, Referral, LeadsUsers
from services.models import ServicesType, ServicesWorking
from wallet.models import Withdrawal, Wallet
from django.utils import timezone
from datetime import timedelta
from django.db import models

class AdminManager:

    @staticmethod
    def admin_check_login(data):
        username = data.get('userId', False)
        password = data.get('password', False)
        check_login = AdminLogin.objects.filter(username=username, password=password).exists()
        return check_login

    @staticmethod
    def fetch_referral_amount(data):
        referral_amount = ReferralAdminPricing.objects.filter()[0].price
        return referral_amount

    @staticmethod
    def change_referral_amount(data):
        value = data.get('value', False)
        if not value:
            raise Exception("value not updated")
        referral_amount = ReferralAdminPricing.objects.filter()[0]
        referral_amount.price = value
        referral_amount.save()


    @staticmethod
    def gwt_all_users(search_query=''):
        users = User.objects.all()

        if search_query:
            users = users.filter(
                Q(full_name__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(phone_number__icontains=search_query) |
                Q(referral_code__icontains=search_query)
            )

        return users

    @staticmethod
    def get_user_referrals(data):
        user_id = data.get('userId', False)
        if not user_id:
            raise Exception("userId not updated")
        referred_users = Referral.objects.filter(user__id=user_id).select_related("referred_user")
        return referred_users

    @staticmethod
    def ban_user_by_admin(data):
        user_id = data.get('userId', False)
        if not user_id:
            raise Exception("userId not updated")
        req_user = User.objects.get(id=user_id)
        req_user.is_active = not req_user.is_active
        req_user.save()

    @staticmethod
    def delete_user_by_admin(data):
        user_id = data.get('userId', False)
        if not user_id:
            raise Exception("userId not updated")
        delete_user = User.objects.filter(id=user_id).delete()

    @staticmethod
    def handle_kyc_user(data):
        kyc_user = ManageKyc.objects.filter(status="pending").select_related("user")
        return kyc_user


    @staticmethod
    def get_single_kyc(data):
        kyc_id = data.get('kycId', False)
        kyc_user = ManageKyc.objects.filter(id=kyc_id).select_related("user")
        return kyc_user


    @staticmethod
    def approval_rejection_of_kyc_user(data):
        kyc_id = data.get('kycId', False)
        action = data.get('action', False)
        if not kyc_id or not action:
            raise Exception("kycId or action is compulsory")
        kyc_user = ManageKyc.objects.filter(id=kyc_id)
        kyc_user[0].status = action
        if action == "reject":
            kyc_user[0].user.is_kyc_given = False
        else:
            kyc_user[0].user.is_verified = True
        kyc_user[0].user.save()

        kyc_user[0].save()


    @staticmethod
    def get_withdrawal_requests(data):
        data = dict(data)
        status = data.get('params[status]', ["Pending"])
        withdraw_request = Withdrawal.objects.filter(status=status[0]).select_related("user")
        return withdraw_request


    @staticmethod
    def approval_rejection_of_withdrawal_requests(data):
        withdraw_id = data.get('WithdrawId', False)
        action = data.get('action', False)
        if action == "approve":
            action = "Completed"
        elif action == "reject":
            action = "Failed"
        if not withdraw_id or not action:
            raise Exception("WithdrawId or action is compulsory")
        withdraw_req = Withdrawal.objects.get(id=withdraw_id).order_by("-processed_at")
        withdraw_req.status = action
        withdraw_req.save()
        return True

    @staticmethod
    def approval_rejection_of_leads_requests(data):
        withdraw_id = data.get('WithdrawId', False)
        action = data.get('action', False)
        if not withdraw_id or not action:
            raise Exception("WithdrawId or action is compulsory")
        withdraw_req = LeadsUsers.objects.get(id=withdraw_id)
        withdraw_req.status = action
        withdraw_req.save()
        if action == "successfull":
            user = withdraw_req.user
            wallet_user = Wallet.objects.get(user=user)
            wallet_user.balance =float(wallet_user.balance) + float(withdraw_req.price)
            wallet_user.save()
        return True

    @staticmethod
    def get_all_services(data):
        services_list = ServicesType.objects.all()
        return services_list


    @staticmethod
    def add_services(data):
        service_name = data.get('serviceName', False)
        if not service_name:
            raise Exception("Service name is compulsory")
        check_service = ServicesType.objects.filter(service_name=service_name).exists()
        if check_service:
            raise Exception("service with this name already exists")
        ServicesType.objects.create(service_name = service_name)


    @staticmethod
    def remove_services(data):
        service_id = data.get('serviceId', False)
        if not service_id:
            raise Exception("service_id is compulsory")
        ServicesType.objects.filter(id=service_id).delete()

    @staticmethod
    def banner_update(data):
        banner_number = data.get('bannerNumber', False)
        banner_image = data.get('bannerImage', False)
        if not banner_number or not banner_image:
            raise Exception("banner number and banner image is compulsory")
        req_banner = Banner.objects.filter()[0]
        if banner_number == 1:
            req_banner.banner_1 = banner_image
        if banner_number == 2:
            req_banner.banner_2 = banner_image
        if banner_number == 3:
            req_banner.banner_3 = banner_image
        req_banner.save()

    @staticmethod
    def success_story_update(data):
        story_number = data.get('storyNumber', False)
        story_image = data.get('storyImage', False)
        if not story_number or not story_image:
            raise Exception("story number and story image is compulsory")
        req_story = SuccessStory.objects.filter()[0]
        if story_number == 1:
            req_story.banner_1 = story_image
        if story_number == 2:
            req_story.banner_2 = story_image
        if story_number == 3:
            req_story.banner_3 = story_image
        req_story.save()

    @staticmethod
    def get_banner_stories(data):
        req_banner = Banner.objects.filter()[0]
        req_story = SuccessStory.objects.filter()[0]
        return req_banner, req_story


    @staticmethod
    def get_offers_related_services(data):
        service_id = data.get('serviceId', False)
        if not service_id:
            raise Exception("service id is compulsory")
        services_list = ServicesWorking.objects.filter(service_name__id=service_id)
        return services_list

    @staticmethod
    def add_offers_related_services(data):
        service_id = data.get('serviceId')
        company_name = data.get('companyName')
        earnings = data.get('earnings')
        title = data.get('title')
        link = data.get('link')
        description = data.get('description')
        image = data.get('image')  # should be InMemoryUploadedFile

        if not all([service_id, company_name, earnings, title, description, link]):
            raise Exception("All fields except image are required")

        ServicesWorking.objects.create(
            service_name_id=service_id,
            company_name=company_name,
            earnings=earnings,
            title=title,
            description=description,
            link=link,
            image=image  # this will auto-save the image
        )

    @staticmethod
    def action_offers_related_services(data):
        service_working_id = data.get('serviceWorkingId', False)
        if not service_working_id:
            raise Exception("Service id is compulsory")
        check_service = ServicesWorking.objects.filter(id=service_working_id).delete()


    @staticmethod
    def fetch_dashboard_data(data):
        male_count = User.objects.filter(gender='M').count()
        female_count = User.objects.filter(gender='F').count()
        other_count = User.objects.filter(gender='O').count()
        referred_count = User.objects.filter(referred_by__isnull=False).count()
        not_referred_count = User.objects.filter(referred_by__isnull=True).count()
        now = timezone.now()

        # Total number of users
        total_users = User.objects.count()

        if total_users == 0:
            return {
                'daily_active_percentage': 0,
                'monthly_active_percentage': 0,
                'yearly_active_percentage': 0
            }

        # Daily active users (users who logged in in the last 24 hours)
        daily_active_users = User.objects.filter(last_login__gte=now - timedelta(days=1)).count()

        # Monthly active users (users who logged in in the last 30 days)
        monthly_active_users = User.objects.filter(last_login__gte=now - timedelta(days=30)).count()

        # Yearly active users (users who logged in in the last 365 days)
        yearly_active_users = User.objects.filter(last_login__gte=now - timedelta(days=365)).count()

        # Calculate percentage values
        daily_active_percentage = daily_active_users / total_users
        monthly_active_percentage = monthly_active_users / total_users
        yearly_active_percentage = yearly_active_users / total_users

        return {
            'male_count': male_count,
            'female_count': female_count,
            'other_count': other_count,
            'referred_count': referred_count,
            'not_referred_count': not_referred_count,
            'daily_active_percentage': round(daily_active_percentage, 2),  # Rounded to 2 decimal places
            'monthly_active_percentage': round(monthly_active_percentage, 2),
            'yearly_active_percentage': round(yearly_active_percentage, 2),
        }

    @staticmethod
    def fetch_leads_details(data):
        get_leads = LeadsUsers.objects.filter().select_related("user").order_by(
            models.Case(
                models.When(status="unverified", then=0),  # Bring "pending" to the top
                default=1,
                output_field=models.IntegerField(),
            ),
            "id"  # Secondary sorting (optional)
        )
        return get_leads

    @staticmethod
    def edit_offers_related_services(data):
        service_id = data.get('serviceId')
        company_name = data.get('companyName')
        title = data.get('title')
        link = data.get('link')
        description = data.get('description')
        image = data.get('image')
        offer_id = data.get('serviceWorkingId')
        is_live = data.get('is_live')
        if is_live == "false":
            is_live = False
        else:
            is_live = True

        if not all([offer_id, service_id, company_name, title, description, link]):
            raise Exception("All fields except image are required")

        try:
            offer = ServicesWorking.objects.get(id=offer_id)
        except ServicesWorking.DoesNotExist:
            raise Exception("Offer with the given ID does not exist")

        offer.service_name_id = service_id
        offer.company_name = company_name
        offer.title = title
        offer.description = description
        offer.link = link
        offer.is_live = is_live

        if image:
            offer.image = image

        offer.save()
