from rest_framework import serializers 
from ....models import Exam
from accounts.serializers import RelatedUserSerializer

class ExamRelatedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        fields = ["id", "title"]

class ExamListSerializer(serializers.ModelSerializer):
    instructor = RelatedUserSerializer()
    category = serializers.CharField(source="category.title")

    class Meta:
        model = Exam
        exclude = ["description"]

class ExamRetrieveSerializer(serializers.ModelSerializer):
    instructor = RelatedUserSerializer()
    category = serializers.CharField(source="category.title")

    class Meta:
        model = Exam
        fields = [
            "id",
            "instructor",
            "title",
            "description",
            "category",
            "duration",
            "created",
        ]

class ExamCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        fields = [
            "title",
            "description",
            "category",
            "duration",
        ]

    def validate_duration(self, duration):
        if duration.total_seconds() < 60:
            raise serializers.ValidationError("The exam cannot be less than 60 seconds")
        return duration

    def create(self, validated_data):
        return Exam.objects.create(
            **validated_data,
            instructor_id=self.context["user_id"],
        )