from .category_views import (
    CategoryViewSet,
    FavoriteCategoryViewSet,
)
from .exam_views import ExamViewSet
from .answer_views import AnswerViewSet
from .question_views import QuestionViewSet, ExamQuestionViewSet
from .score_views import (
    ScoreViewSet,
    ExamScoreViewSet,
    MyScoreViewSet,
    ScoreBoardViewSet,
)

all = [
    "CategoryViewSet",
    "FavoriteCategoryViewSet",
    "ExamViewSet",
    "AnswerViewSet",
    "QuestionViewSet",
    "ExamQuestionViewSet",
]
