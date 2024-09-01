from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response

from authentication.custom_permissions import IsUserAuth
from referral.manager import ReferralManager
from referral.serializer import LeadsUsersSerializer


class  AddLeadToSms(APIView):
    permission_classes = [IsUserAuth]
    @staticmethod
    def post(request):
        try:
            data = request.data
            obj_created = ReferralManager.send_otp_to_lead(request, data)
            return Response({"result" : "success", "message":"created successfully"}, 200)

        except Exception as err:
            return Response(str(err), 500)

class  getLeadsUser(APIView):
    permission_classes = [IsUserAuth]

    @staticmethod
    def get(request):
        try:
            data = request.data
            obj_created = ReferralManager.get_leads_list(request, data)
            leads_data = LeadsUsersSerializer(obj_created, many=True).data
            return Response({"result" : "success", "data":leads_data}, 200)

        except Exception as err:
            return Response(str(err), 500)