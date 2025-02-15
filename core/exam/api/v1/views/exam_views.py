from rest_framework import viewsets
from ....models import Exam, Participation, Score, Question
from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAuthenticated
from authentication.permissions import IsStudent, IsInstructor, IsInstructorOwner
from ..serializers import (
    ExamRetrieveSerializer,
    ExamCreateUpdateSerializer,
    ExamListSerializer,
    ScoreSerializer,
    AnswerCreateSerializer,
    StudentQuestionRetrieveSerializer,
)
from rest_framework.decorators import action
from rest_framework.request import Request
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.select_related("instructor", "category").all()

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        if self.action in ["reply", "finish, next_question"]:
            return [IsAuthenticated(), IsStudent()]
        return [IsAuthenticated(), IsInstructor(), IsInstructorOwner()]

    def get_serializer_class(self):

        if self.action == "retrieve":
            return ExamRetrieveSerializer
        if self.action == "finish":
            return ScoreSerializer
        if self.action == "reply":
            return AnswerCreateSerializer
        if self.request.method not in SAFE_METHODS:
            return ExamCreateUpdateSerializer
        return ExamListSerializer

    def get_serializer_context(self):
        return {"user_id": self.request.user.id}

    def get_throttles(self):
        if self.action == "reply":
            self.throttle_scope = "reply"
        if self.action == "next_question":
            self.throttle_scope = "next_question"
        if self.action == "finish":
            self.throttle_scope = "finish"
        return super().get_throttles()

    @action(detail=True, methods=["GET"])
    def next_question(self, request: Request, pk):
        user_id = request.user.id
        exam = get_object_or_404(Exam, pk=pk)

        participation, created = Participation.objects.get_or_create(
            student_id=user_id,
            exam_id=pk,
            defaults={"expires_at": timezone.now() + exam.duration},
        )
        if (
            not created
            and Score.objects.filter(exam_id=exam, student_id=user_id).exists()
        ):
            return Response(
                {"detail": "you have already taken this test"},
                status=status.HTTP_403_FORBIDDEN,
            )
        if not created and timezone.now() >= participation.expires_at:
            return Response(
                {"detail": "the exam time is over"},
                status=status.HTTP_403_FORBIDDEN,
            )
        next_question = (
            Question.objects.filter(exam_id=pk)
            .exclude(answers__student=user_id)
            .first()
        )
        if not next_question:
            return Response(
                {"detail": "you have answered all the questions"},
                status=status.HTTP_403_FORBIDDEN,
            )
        serializer = StudentQuestionRetrieveSerializer(next_question)
        return Response(serializer.data)
