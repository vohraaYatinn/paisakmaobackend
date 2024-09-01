from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from authentication.manager import AuthenticationManager
from course.manager import CourseManager


# Create your views here.
class  CourseViewAdmin(APIView):

    @staticmethod
    def post(request):
        try:
            data = request.data
            banner_upload = CourseManager.course_upload(data)
            return Response({"result" : "success", "message":"banners have been updated"}, 200)

        except Exception as err:
            return Response(str(err), 500)

    @staticmethod
    def get(request):
        try:
            data = request.data
            banner_upload = CourseManager.course_get(data)
            return Response({"result" : "success", "message":"banners have been updated"}, 200)

        except Exception as err:
            return Response(str(err), 500)

class  VideoViewAdmin(APIView):

    @staticmethod
    def post(request):
        try:
            data = request.data
            banner_upload = CourseManager.video_upload(data)
            return Response({"result" : "success", "message":"banners have been updated"}, 200)

        except Exception as err:
            return Response(str(err), 500)

    @staticmethod
    def get(request):
        try:
            data = request.data
            banner_upload = CourseManager.video_get(data)
            return Response({"result" : "success", "message":"banners have been updated"}, 200)

        except Exception as err:
            return Response(str(err), 500)
