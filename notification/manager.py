import random

from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.db.models import Q
import requests
from rest_framework.exceptions import ValidationError

from authentication.models import User
from banner.models import Banner
from course.models import Course, Video
from notification.models import Notification


class NotificationManager:
    @staticmethod
    def get_notifications(request, data):
        user = request.user.phone
        return Notification.objects.filter(user__phone_number=user).order_by("-created_at")

    @staticmethod
    def change_notifications_seen(request, data):
        user = request.user.phone
        notification_id = data.get("notificationId")
        notification_obj = Notification.objects.filter(user__phone_number=user, id=notification_id)
        if notification_obj:
            notification_obj[0].read = True
            notification_obj[0].save()


    @staticmethod
    def delete_notifications(request, data):
        user = request.user.phone
        notification_id = data.get("notificationId")
        notification_obj = Notification.objects.filter(user__phone_number=user, id=notification_id)
        if notification_obj:
            notification_obj[0].delete()
