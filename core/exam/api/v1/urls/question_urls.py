from rest_framework.routers import DefaultRouter
from ..views import QuestionViewSet

app_name = "api-v1"

router = DefaultRouter()

urlpatterns = []

router.register(r"questions", QuestionViewSet, basename="questions")

urlpatterns += router.urls
