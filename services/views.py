from rest_framework.views import APIView
from rest_framework.response import Response
from authentication.custom_permissions import IsUserAuth
from services.manager import ServiceManager
from services.serializer import ServiceWorkingSerializer


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


class  GetServicesByName(APIView):
    @staticmethod
    def get(request):
        try:
            data = request.query_params
            get_services = ServiceManager.get_services_by_name(request, data)
            serializer_data = ServiceWorkingSerializer(get_services, many=True).data
            return Response({"result" : "success", "data":serializer_data}, 200)

        except Exception as err:
            return Response(str(err), 500)
