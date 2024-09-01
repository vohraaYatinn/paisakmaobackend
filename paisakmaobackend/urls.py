from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/authentication/', include("authentication.urls"), name="authentication"),
    path(r'api/banner/', include("banner.urls"), name="banner"),
    path(r'api/course/', include("course.urls"), name="course"),
    path(r'api/notifications/', include("notification.urls"), name="notification"),
    path(r'api/referral/', include("referral.urls"), name="referral"),
    path(r'api/stories/', include("stories.urls"), name="stories"),
    path(r'api/wallet/', include("wallet.urls"), name="wallet"),
    path(r'api/services/', include("services.urls"), name="services"),
]
