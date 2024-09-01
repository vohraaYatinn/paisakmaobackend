from rest_framework.views import APIView
from rest_framework.response import Response

from authentication.custom_permissions import IsUserAuth
from wallet.manager import WalletManager
from wallet.serializer import WithdrawalSerializer


class  WalletGet(APIView):

    @staticmethod
    def get(request):
        try:
            data = request.data
            notifications_data = WalletManager.get_wallet_info(data)
            return Response({"result" : "success", "data":notifications_data}, 200)

        except Exception as err:
            return Response(str(err), 500)

class  WithdrawRequest(APIView):
    permission_classes = [IsUserAuth]

    @staticmethod
    def get(request):
        try:
            data = request.query_params
            notifications_data = WalletManager.get_withdraw_request(request, data)
            serializer_data = WithdrawalSerializer(notifications_data, many=True).data
            return Response({"result" : "success", "data":serializer_data}, 200)

        except Exception as err:
            return Response(str(err), 500)

class  ApplyWithdrawRequest(APIView):
    permission_classes = [IsUserAuth]

    @staticmethod
    def post(request):
        try:
            data = request.data
            withdraw_req = WalletManager.apply_withdraw_request(request, data)
            return Response({"result" : "success", "message":"withdraw request has been applied successfully"}, 200)

        except Exception as err:
            return Response(str(err), 500)