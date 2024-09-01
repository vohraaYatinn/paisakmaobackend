from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from authentication.manager import AuthenticationManager
from banner.manager import BannerManager


# Create your views here.
class  BannerView(APIView):
    @staticmethod
    def post(request):
        try:
            data = request.data
            banner_upload = BannerManager.banner_upload(data)
            return Response({"result" : "success", "message":"banners have been updated"}, 200)

        except Exception as err:
            return Response(str(err), 500)

    @staticmethod
    def get(request):
        try:
            data = request.query_params
            banner_get = BannerManager.banner_get(data)
            return Response({"result" : "success", "data":banner_get}, 200)

        except Exception as err:
            return Response(str(err), 500)