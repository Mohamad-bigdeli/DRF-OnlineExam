from rest_framework.routers import DefaultRouter
from ..views import ScoreViewSet, MyScoreViewSet

router = DefaultRouter()

urlpatterns = [

]

router.register(r"scores", ScoreViewSet, basename="scores")

router.register(r"my-scores", MyScoreViewSet, basename="my-scores")

urlpatterns+=router.urls