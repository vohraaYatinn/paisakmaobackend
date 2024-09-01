from rest_framework.views import APIView
from rest_framework.response import Response
from authentication.custom_permissions import IsUserAuth
from services.manager import ServiceManager


class  ServiceGet(APIView):
    permission_classes = [IsUserAuth]
    @staticmethod
    def get(request):
        try:
            data = request.query_params
            get_services = ServiceManager.send_otp_to_lead(request, data)
            return Response({"result" : "success", "message":"created successfully"}, 200)

        except Exception as err:
            return Response(str(err), 500)
