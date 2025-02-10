from rest_framework import viewsets, mixins
from ....models import Score, Participation
from ..serializers import (ScoreListRetrieveSerializer, ScoreListRetrieveSerializer,
                           StudentScoreListRetrieveSerializer, ScoreBoardSerializer)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from authentication.permissions import IsInstructor, IsStudent


class ScoreViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Score.objects.select_related("student", "exam").all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ScoreListRetrieveSerializer


class ExamScoreViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    permission_classes = [IsAuthenticated, IsInstructor]
    serializer_class = ScoreListRetrieveSerializer

    def get_queryset(self):
        return (
            Score.objects.select_related("student", "exam")
            .filter(
                exam_id=self.kwargs["exam_pk"],
                exam__instructor_id=self.request.user.id,
            )
            .all()
        )


class MyScoreViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    permission_classes = [IsAuthenticated, IsStudent]
    serializer_class = StudentScoreListRetrieveSerializer

    def get_queryset(self):
        return Score.objects.filter(student_id=self.request.user.id).all()




class ScoreBoardViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    serializer_class = ScoreBoardSerializer
    
    def get_queryset(self):
        return Score.objects.select_related("student").filter(exam_id=self.kwargs["exam_pk"]).order_by("-score")