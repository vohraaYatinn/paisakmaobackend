from django.urls import path
from banner.views import BannerView
from course.views import CourseViewAdmin, VideoViewAdmin

urlpatterns = [
    # admin
    path(r'course-update-admin/', CourseViewAdmin.as_view(), name="course-update-admin"),
    path(r'videos-update-admin/', VideoViewAdmin.as_view(), name="course-update-admin"),
    path(r'course-get/', CourseViewAdmin.as_view(), name="course-get"),
    path(r'videos-get/', VideoViewAdmin.as_view(), name="videos-get"),

]
