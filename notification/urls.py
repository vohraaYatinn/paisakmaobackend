from django.urls import path
from banner.views import BannerView
from notification.views import NotificationGet, NotificationSeenChange, deleteNotification

urlpatterns = [
    path(r'get-notifications/', NotificationGet
         .as_view(), name="notification-get"),
    path(r'change-seen-notifications/', NotificationSeenChange
         .as_view(), name="notification-get"),
    path(r'delete-notifications/', deleteNotification
         .as_view(), name="notification-get"),


]
