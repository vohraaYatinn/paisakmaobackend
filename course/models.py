import uuid

from django.db import models
class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    couse_banner = models.ImageField(upload_to='course_banners/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=255)
    video_banner = models.ImageField(upload_to='video_banners/', blank=True, null=True)
    video_url = models.URLField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
