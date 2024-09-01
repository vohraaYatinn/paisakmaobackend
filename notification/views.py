from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response

from authentication.custom_permissions import IsUserAuth
from authentication.manager import AuthenticationManager
from notification.manager import NotificationManager
from notification.serializer import NotificationSerializer


class  NotificationGet(APIView):
    permission_classes = [IsUserAuth]

    @staticmethod
    def get(request):
        try:
            data = request.data
            notifications_data = NotificationManager.get_notifications(request, data)
            serialized_data = NotificationSerializer(notifications_data, many=True).data
            return Response({"result" : "success", "data":serialized_data}, 200)

        except Exception as err:
            return Response(str(err), 500)

class  NotificationSeenChange(APIView):
    permission_classes = [IsUserAuth]

    @staticmethod
    def post(request):
        try:
            data = request.data
            notifications_data = NotificationManager.change_notifications_seen(request, data)
            return Response({"result" : "success", "message":"message seen successfully"}, 200)

        except Exception as err:
            return Response(str(err), 500)

class  deleteNotification(APIView):
    permission_classes = [IsUserAuth]

    @staticmethod
    def post(request):
        try:
            data = request.data
            notifications_data = NotificationManager.delete_notifications(request, data)
            return Response({"result" : "success", "message":"message seen successfully"}, 200)

        except Exception as err:
            return Response(str(err), 500)