from rest_framework import serializers
from accounts.serializers import RelatedUserSerializer
from ....models import Answer
from ....models import Participation
from django.utils import timezone
from .question_serializer import RelatedQuestionSerializer, RelatedQuestionOptionSerializer

class AnswerListRetrieveSerializer(serializers.ModelSerializer):

    student = RelatedUserSerializer()
    question = RelatedQuestionSerializer()
    selected_option = RelatedQuestionOptionSerializer()

    class Meta:
        model = Answer
        fields = ["id", "student", "question", "selected_option", "created"]
    
class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["question", "selected_option"]

    def validate(self, attrs):
        question_id = attrs["question"]
        student_id = self.context["user_id"]
        exam_id = self.context["exam_id"]

        participation = Participation.objects.filter(student_id=student_id,exam_id=exam_id).first()

        if not participation:
            return serializers.ValidationError("you have not taken this test")
        if timezone.now() >= participation.expires_at:
            return serializers.ValidationError("the exam time is over")
        answer_exist = Answer.objects.filter(student_id=student_id, question_id=question_id).exists()
        
        if answer_exist:
            return serializers.ValidationError("you have already taken this test")
        return super().validate(attrs)

    def create(self, validated_data):
        return Answer.objects.create(**validated_data, student_id=self.context["user_id"])
