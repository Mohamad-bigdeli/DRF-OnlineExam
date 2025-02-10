from rest_framework.routers import DefaultRouter
from ..views import ExamViewSet, AnswerViewSet, ExamQuestionViewSet, ExamScoreViewSet, ScoreBoardViewSet
from rest_framework_nested import routers

router = DefaultRouter()

urlpatterns = []

router.register(r"exams", ExamViewSet, basename="exams")

urlpatterns+=router.urls

exam_router = routers.NestedSimpleRouter(router, r"exams", lookup="exam")

exam_router.register(r"questions", ExamQuestionViewSet, basename="questions")
exam_router.register(r"answers", AnswerViewSet, basename="answers")
exam_router.register(r"scores", ExamScoreViewSet, basename="exam-scores")
exam_router.register(r"scoreboard", ScoreBoardViewSet, basename="scoreboard")

urlpatterns+=exam_router.urls