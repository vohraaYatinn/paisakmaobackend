from django.db import models

class Banner(models.Model):
    banner_1 = models.ImageField(upload_to='banners/', blank=True, null=True)
    banner_2 = models.ImageField(upload_to='banners/', blank=True, null=True)
    banner_3 = models.ImageField(upload_to='banners/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)