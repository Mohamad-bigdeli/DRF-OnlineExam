from .category_serializer import (
    CategorySerializer,
    FavoriteCategoryCreateSerializer,
    FavoriteCategoryListRetrieveSerializer,
)
from .exam_serializer import (
    ExamRelatedSerializer,
    ExamListSerializer,
    ExamRetrieveSerializer,
    ExamCreateUpdateSerializer
)
from .answer_serializer import (
    AnswerListRetrieveSerializer,
    AnswerCreateSerializer
)
from .question_serializer import (
    RelatedQuestionSerializer,
    RelatedQuestionOptionSerializer,
    StudentRelatedQuestionOptionSerializer,
    StudentQuestionRetrieveSerializer,
    AdminQuestionListSerializer,
    AdminQuestionRetrieveSerializer,
    QuestionListSerializer,
    QuestionRetrieveSerializer,
    QuestionOptionListSerializer,
    QuestionCreateUpdateSerializers,

)
from .score_serializer import (
    ScoreListRetrieveSerializer,
    ScoreSerializer,
    StudentScoreListRetrieveSerializer,
    ScoreBoardSerializer,
)

all = [
    "CategorySerializer",
    "FavoriteCategoryCreateSerializer",
    "FavoriteCategoryListRetrieveSerializer",
    "ExamRelatedSerializer",
    "ExamListSerializer",
    "ExamRetrieveSerializer",
    "ExamCreateUpdateSerializer",
    "AnswerListRetrieveSerializer",
    "AnswerCreateSerializer",
    "RelatedQuestionSerializer",
    "RelatedQuestionOptionSerializer",
    "StudentRelatedQuestionOptionSerializer",
    "StudentQuestionRetrieveSerializer",
    "AdminQuestionListSerializer",
    "AdminQuestionRetrieveSerializer",
    "QuestionListSerializer",
    "QuestionRetrieveSerializer",
    "QuestionOptionListSerializer",
    "QuestionCreateUpdateSerializers",
    "ScoreListRetrieveSerializer",
    "ScoreSerializer",
    "StudentScoreListRetrieveSerializer",
    "ScoreBoardSerializer"
]