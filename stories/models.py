import uuid

from django.db import models

from authentication.models import User


# Create your models here.
class SuccessStory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='success_stories')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
