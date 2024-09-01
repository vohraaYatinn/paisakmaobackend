import random

from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.db.models import Q
import requests
from rest_framework.exceptions import ValidationError

from authentication.models import User
from banner.models import Banner
from course.models import Course, Video


class CourseManager:
    @staticmethod
    def course_upload(data):
        title = data.get('title', None)
        description = data.get('description', None)
        if not title or not description:
            raise ValidationError("All required fields (title, description, price) must be provided.")
        course = Course.objects.create(
            title=title,
            description=description
        )
        return course

    @staticmethod
    def video_upload(data):
        video = data.get('video', None)
        title = data.get('title', None)
        course = data.get('course_id', None)
        video = Video.objects.create(
            course_id=course,
            title=title,
            video_url=video
        )
        return video

    @staticmethod
    def course_get(data):
        return Course.objects.filter()

    @staticmethod
    def video_get(data):
        course_id = data.get('course_id', None)
        return Video.objects.filter(course_id=course_id)

