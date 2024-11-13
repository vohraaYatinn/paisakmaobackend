from rest_framework.views import APIView
from rest_framework.response import Response
from adminpannel.manager import AdminManager
from adminpannel.serializer import UserSerializer, UserSerializerWithWallet, ReferredUserSerializer, \
    KycSerializerWithUser, WithdrawSerializerWithUser, WithdrawSerializer, OfferServicesSerializer, BannerSerializer, \
    StoriesSerializer, LeadsWithUserSerializer


class AdminView(APIView):
    @staticmethod
    def post(request):
        try:
            data = request.data
            check_lgoin = AdminManager.admin_check_login(data)
            return Response({"result" : "success", "message":"login successfull", "login":check_lgoin}, 200)

        except Exception as err:
            return Response(str(err), 500)

class fetchReferralAmount(APIView):
    @staticmethod
    def post(request):
        try:
            data = request.data
            AdminManager.change_referral_amount(data)
            return Response({"result" : "success", "message":"amount changed successfully"}, 200)

        except Exception as err:
            return Response(str(err), 500)

    @staticmethod
    def get(request):
        try:
            data = request.data
            referral_amount = AdminManager.fetch_referral_amount(data)
            return Response({"result" : "success", "message":"amount fetched successfully", "amount":referral_amount}, 200)

        except Exception as err:
            return Response(str(err), 500)

class UserManagement(APIView):

    @staticmethod
    def get(request):
        try:
            data = request.data
            all_users = AdminManager.gwt_all_users(data)
            serialized_data = UserSerializerWithWallet(all_users, many=True).data
            return Response({"result" : "success", "message":"amount fetched successfully", "data":serialized_data}, 200)

        except Exception as err:
            return Response(str(err), 500)

class UserReferralManagement(APIView):

    @staticmethod
    def get(request):
        try:
            data = request.query_params
            referred_users = AdminManager.get_user_referrals(data)
            serialized_data = ReferredUserSerializer(referred_users, many=True).data
            return Response({"result" : "success", "message":"amount fetched successfully", "data":serialized_data}, 200)

        except Exception as err:
            return Response(str(err), 500)

class BanUserManagement(APIView):

    @staticmethod
    def post(request):
        try:
            data = request.data
            AdminManager.ban_user_by_admin(data)
            return Response({"result" : "success", "message":"action on user have been done successfully"}, 200)
        except Exception as err:
            return Response(str(err), 500)

class DeleteUserManagement(APIView):

    @staticmethod
    def post(request):
        try:
            data = request.data
            AdminManager.delete_user_by_admin(data)
            return Response({"result" : "success", "message":"action on user have been done successfully"}, 200)
        except Exception as err:
            return Response(str(err), 500)

class KycRequest(APIView):

    @staticmethod
    def get(request):
        try:
            data = request.data
            kyc_user = AdminManager.handle_kyc_user(data)
            serialized_data = KycSerializerWithUser(kyc_user, many=True).data
            return Response({"result" : "success", "message":"kyc user data has been fetched successfully", "data":serialized_data}, 200)
        except Exception as err:
            return Response(str(err), 500)

    @staticmethod
    def post(request):
        try:
            data = request.data
            AdminManager.approval_rejection_of_kyc_user(data)
            return Response({"result" : "success", "message":"action on kyc have been done successfully"}, 200)
        except Exception as err:
            return Response(str(err), 500)


class SingleKycRequest(APIView):

    @staticmethod
    def get(request):
        try:
            data = request.query_params
            kyc_user = AdminManager.get_single_kyc(data)
            serialized_data = KycSerializerWithUser(kyc_user, many=True).data
            return Response({"result" : "success", "message":"kyc user data has been fetched successfully", "data":serialized_data}, 200)
        except Exception as err:
            return Response(str(err), 500)

class WithdrawRequests(APIView):

    @staticmethod
    def get(request):
        try:
            data = request.data
            withdraw_request = AdminManager.get_withdrawal_requests(data)
            serialized_data = WithdrawSerializerWithUser(withdraw_request, many=True).data
            return Response({"result" : "success", "message":"withdraw request has been fetched successfully", "data":serialized_data}, 200)
        except Exception as err:
            return Response(str(err), 500)

    @staticmethod
    def post(request):
        try:
            data = request.data
            check = AdminManager.approval_rejection_of_withdrawal_requests(data)
            return Response({"result" : "success", "message":"action on withdraw have been done successfully"}, 200)
        except Exception as err:
            return Response(str(err), 500)

class ServicesManagement(APIView):

    @staticmethod
    def get(request):
        try:
            data = request.data
            services_list = AdminManager.get_all_services(data)
            serialized_data = WithdrawSerializer(services_list, many=True).data
            return Response({"result" : "success", "message":"Services has been fetched successfully", "data":serialized_data}, 200)
        except Exception as err:
            return Response(str(err), 500)

    @staticmethod
    def post(request):
        try:
            data = request.data
            AdminManager.add_services(data)
            return Response({"result" : "success", "message":"new services has been added successfully"}, 200)
        except Exception as err:
            return Response(str(err), 500)

class ActionServicesManagement(APIView):

    @staticmethod
    def post(request):
        try:
            data = request.data
            AdminManager.remove_services(data)
            return Response({"result" : "success", "message":"services has been deleted successfully"}, 200)
        except Exception as err:
            return Response(str(err), 500)

class BannerUpdate(APIView):

    @staticmethod
    def post(request):
        try:
            data = request.data
            AdminManager.banner_update(data)
            return Response({"result" : "success", "message":"services has been deleted successfully"}, 200)
        except Exception as err:
            return Response(str(err), 500)

class SuccessStoryUpdate(APIView):

    @staticmethod
    def post(request):
        try:
            data = request.data
            AdminManager.success_story_update(data)
            return Response({"result" : "success", "message":"services has been deleted successfully"}, 200)
        except Exception as err:
            return Response(str(err), 500)


class GetOffersRelatedToServices(APIView):
    @staticmethod
    def get(request):
        try:
            data = request.query_params
            offer_services_list = AdminManager.get_offers_related_services(data)
            serialized_data = OfferServicesSerializer(offer_services_list, many=True).data
            return Response({"result" : "success", "message":"services has been deleted successfully", "data":serialized_data}, 200)
        except Exception as err:
            return Response(str(err), 500)

    @staticmethod
    def post(request):
        try:
            data = request.data
            AdminManager.add_offers_related_services(data)
            return Response({"result" : "success", "message":"services has been added successfully"}, 200)
        except Exception as err:
            return Response(str(err), 500)


class ActionOnOffersRelatedToServices(APIView):
    @staticmethod
    def post(request):
        try:
            data = request.data
            AdminManager.action_offers_related_services(data)
            return Response({"result" : "success", "message":"services has been deleted successfully"}, 200)
        except Exception as err:
            return Response(str(err), 500)


class GetBannerSuccessImages(APIView):

    @staticmethod
    def get(request):
        try:
            data = request.data
            req_banner, req_story = AdminManager.get_banner_stories(data)
            serialized_data_banner = BannerSerializer(req_banner).data
            serialized_data_stories = StoriesSerializer(req_story).data

            return Response({"result": "success", "banner_data":serialized_data_banner, "stories_data": serialized_data_stories }, 200)
        except Exception as err:
            return Response(str(err), 500)


class FetchDashboard(APIView):

    @staticmethod
    def get(request):
        try:
            data = request.data
            dashboard_data = AdminManager.fetch_dashboard_data(data)
            return Response({"result" : "success", "message":"services has been deleted successfully", "data": dashboard_data}, 200)
        except Exception as err:
            return Response(str(err), 500)

class LeadsManagement(APIView):

    @staticmethod
    def get(request):
        try:
            data = request.data
            dashboard_data = AdminManager.fetch_leads_details(data)
            serialized_Data = LeadsWithUserSerializer(dashboard_data, many=True).data
            return Response({"result" : "success", "message":"leads has been fetched successfully", "data": serialized_Data}, 200)
        except Exception as err:
            return Response(str(err), 500)

    @staticmethod
    def post(request):
        try:
            data = request.data
            dashboard_data = AdminManager.fetch_dashboard_data(data)
            return Response({"result" : "success", "message":"services has been deleted successfully", "data": dashboard_data}, 200)
        except Exception as err:
            return Response(str(err), 500)