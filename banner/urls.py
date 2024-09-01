from django.urls import path
from banner.views import BannerView

urlpatterns = [
    path(r'banner-post-admin/', BannerView.as_view(), name="banner-post-admin"),
    path(r'banner-get/', BannerView.as_view(), name="banner-get"),
]

