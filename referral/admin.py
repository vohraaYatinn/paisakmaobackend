from django.contrib import admin

from referral.models import Referral, ReferralAdminPricing, LeadsUsers

admin.site.register(Referral)
admin.site.register(ReferralAdminPricing)
admin.site.register(LeadsUsers)
