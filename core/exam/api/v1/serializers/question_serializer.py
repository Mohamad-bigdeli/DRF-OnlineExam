from rest_framework import serializers
from ....models import Question, QuestionOption
from ..serializers import ExamRelatedSerializer
from django.db import transaction

class RelatedQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "question_text"]

class RelatedQuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = ["id", "option_text", "is_correct_answer"]

class StudentRelatedQuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        exclude = ["is_correct_answer", "created", "question"]
    
class StudentQuestionRetrieveSerializer(serializers.ModelSerializer):
    options = StudentRelatedQuestionOptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ["id", "question_text", "options"]

class AdminQuestionListSerializer(serializers.ModelSerializer):
    exam = ExamRelatedSerializer()

    class Meta:
        model = Question
        fields = ["id", "exam", "question_text", "created"]

class AdminQuestionRetrieveSerializer(serializers.ModelSerializer):
    exam = ExamRelatedSerializer()
    options = RelatedQuestionOptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ["id", "exam", "question_text", "options", "created"]
    
class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "question_text", "created"]

class QuestionRetrieveSerializer(serializers.ModelSerializer):
    options = RelatedQuestionOptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ["id", "question_text", "options", "created"]

class QuestionOptionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = ["option_text", "is_correct_answer"]

class QuestionCreateUpdateSerializers(serializers.ModelSerializer):
    options = QuestionOptionListSerializer(many=True)

    class Meta:
        model = Question
        fields = ["question_text", "options"]
    
    def validate_options(self, options):
        option_length = len(options)

        if option_length < 2:
            raise serializers.ValidationError(
                "Each question should contain at least 2 options"
            )

        if option_length > 10:
            raise serializers.ValidationError(
                "Each question should contain a maximum of 10 options"
            )

        correct_options_count = len(
            list(filter(lambda option: option["is_correct_answer"], options))
        )

        if correct_options_count == 0:
            raise serializers.ValidationError(
                "At least one option must be selected as the correct answer"
            )

        if correct_options_count > 1:
            raise serializers.ValidationError(
                "A question cannot have more than 1 correct answer"
            )

        return options
    
    @transaction.atomic()
    def create(self, validated_data):
        exam_id = self.context["exam_id"]
        options = validated_data["options"]

        question = Question.objects.create(
            exam_id=exam_id,
            question_text=validated_data["question_text"],
        )

        QuestionOption.objects.bulk_create(
            [
                QuestionOption(
                    question=question,
                    option_text=option["option_text"],
                    is_correct_answer=option["is_correct_answer"],
                )
                for option in options
            ]
        )

        return question