import random

from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.db.models import Q
import requests
from rest_framework.exceptions import ValidationError

from authentication.models import User
from banner.models import Banner


class BannerManager:

    @staticmethod
    def banner_upload(data):
        banner_1 = data.get('banner1', False)
        banner_2 = data.get('banner2', False)
        banner_3 = data.get('banner3', False)

        if not banner_1 and not banner_2 and not banner_3:
            raise ValidationError("At least one banner must be provided.")

        banner_instance = Banner()

        if banner_1:
            banner_instance.banner_1 = banner_1
        if banner_2:
            banner_instance.banner_2 = banner_2
        if banner_3:
            banner_instance.banner_3 = banner_3

        banner_instance.save()

        return banner_instance
    @staticmethod
    def banner_get(data):
        banner_instance = Banner.objects.filter().latest()
        return banner_instance