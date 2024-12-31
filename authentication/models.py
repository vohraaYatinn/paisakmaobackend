
from django.db import models
import uuid

class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    password = models.CharField(max_length=128, null=True)
    referral_code = models.CharField(max_length=100, unique=True, blank=True, null=True)
    referred_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='referrals')
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True, null=True)
    is_kyc_given = models.BooleanField(default=False, null=True)
    is_verified = models.BooleanField(default=False, null=True)
    last_login = models.DateTimeField(auto_now_add=True, null=True)
    profile_photo = models.ImageField(upload_to='profile/', blank=True, null=True)


    def __str__(self):
        return f'{self.full_name}'


class ManageKyc(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kycuser', null=True, blank=True)
    document_type = models.CharField(max_length=255)
    front_image = models.ImageField(upload_to='kycimage/', blank=True, null=True)
    back_image = models.ImageField(upload_to='kycimage/', blank=True, null=True)
    status = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.document_type}'
