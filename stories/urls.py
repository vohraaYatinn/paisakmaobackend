from django.urls import path
from stories.views import StoriesGet

urlpatterns = [

    path(r'success-stories-get/', StoriesGet
         .as_view(), name="success-stories-get"),

]
