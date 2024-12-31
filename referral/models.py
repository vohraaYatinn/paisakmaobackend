import uuid
from django.db import models
from authentication.models import User

# Create your models here.
class Referral(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrals_made')
    referred_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrals_received')
    referral_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} referred {self.referred_user}'


class ReferralAdminPricing(models.Model):
    price = models.IntegerField()



# unverified
# pending
#successfull
# failed

class LeadsUsers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leads_user')
    customer_name = models.CharField(max_length=40)
    customer_number = models.CharField(max_length=20)
    customer_email = models.CharField(max_length=100)
    compaign_id = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    service_name = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    otp_to_verify = models.CharField(max_length=5)
    status = models.CharField(max_length=20, default="unverified")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.price
