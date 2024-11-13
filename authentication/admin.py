from django.contrib import admin
from authentication.models import User, ManageKyc

admin.site.register(User)
admin.site.register(ManageKyc)