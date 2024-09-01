from stories.models import SuccessStory


class StoryManager:
    @staticmethod
    def get_success_stories(data):
        user = data.get('user', None)
        return SuccessStory.objects.filter(user=user).order_by("-created_at")

