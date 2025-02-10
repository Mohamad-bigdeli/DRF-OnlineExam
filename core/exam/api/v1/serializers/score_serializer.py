from rest_framework import serializers
from ....models import Score
from ..serializers import ExamRelatedSerializer
from accounts.serializers import RelatedUserSerializer


class ScoreListRetrieveSerializer(serializers.ModelSerializer):
    student = RelatedUserSerializer()
    exam = ExamRelatedSerializer()

    class Meta:
        model = Score
        fields = ["student", "exam", "score", "created"]


class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = ["score", "rank"]
        read_only_fields = ["score", "rank"]


class StudentScoreListRetrieveSerializer(ScoreListRetrieveSerializer):
    class Meta(ScoreListRetrieveSerializer.Meta):
        excludes = ["student"]


class ScoreBoardSerializer(serializers.ModelSerializer):
    student = RelatedUserSerializer()

    class Meta:
        model = Score
        fields = ["student", "rank", "score"]