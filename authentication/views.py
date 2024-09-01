from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response

from authentication.custom_permissions import IsUserAuth
from authentication.manager import AuthenticationManager
from authentication.serializer import UserSerializer, UserWithWalletSerializer
import jwt

# Create your views here.
class  OtpVerification(APIView):
    # permission_classes = [IsAuthenticated]
    @staticmethod
    def post(request):
        try:
            data = request.data
            verification_code, user = AuthenticationManager.otp_send_phone(data)

            return Response({"result" : "success", "verification_code":verification_code['data']['verificationId']}, 200)

        except Exception as err:
            return Response(str(err), 500)

    @staticmethod
    def get(request):
        try:
            data = request.query_params
            verification_verify, user_exist = AuthenticationManager.otp_verify_phone(data)
            serialized_data = UserSerializer(user_exist).data
            payload = {
                'user': user_exist.phone_number
            }
            token = jwt.encode(payload, 'secretKeyRight34', algorithm='HS256')
            return Response({"result" : "success", "data":verification_verify, "user":serialized_data, "token":token}, 200)

        except Exception as err:
            return Response(str(err), 500)


# Create your views here.
class SignupApi(APIView):
    @staticmethod
    def post(request):
        try:
            data = request.data
            verification_code = AuthenticationManager.signup_user(data)
            return Response({"result" : "success", "verification_code":verification_code['data']['verificationId']}, 200)

        except ValidationError as err:
            err = str(err)
            start_index = err.find("string='") + len("string='")
            end_index = err.find("', code=")
            error_message = err[start_index:end_index]

            return Response({"result" : "failure", "message":error_message}, 200)
        except Exception as err:
            return Response({"result" : "failure", "message":str(err)}, 200)
# Create your views here.

class getDashboardData(APIView):
    permission_classes = [IsUserAuth]
    @staticmethod
    def get(request):
        try:
            data = request.query_params
            user_data = AuthenticationManager.dashboard_data(request, data)
            serialized_data = UserWithWalletSerializer(user_data[0]).data
            return Response({"result" : "success", "data":serialized_data}, 200)

        except ValidationError as err:
            return Response(str(err), 500)
        except Exception as err:
            return Response(str(err), 500)

class fetchMyReferrals(APIView):
    permission_classes = [IsUserAuth]
    @staticmethod
    def get(request):
        try:
            data = request.query_params
            user_data = AuthenticationManager.fetch_my_referrals(request, data)
            serialized_data = UserWithWalletSerializer(user_data, many=True).data
            return Response({"result" : "success", "data":serialized_data}, 200)

        except ValidationError as err:
            return Response(str(err), 500)
        except Exception as err:
            return Response(str(err), 500)
