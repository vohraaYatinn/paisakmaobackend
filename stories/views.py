from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from authentication.manager import AuthenticationManager
from stories.manager import StoryManager

class StoriesGet(APIView):

    @staticmethod
    def get(request):
        try:
            data = request.data
            notifications_data = StoryManager.get_success_stories(data)
            return Response({"result" : "success", "data":notifications_data}, 200)

        except Exception as err:
            return Response(str(err), 500)