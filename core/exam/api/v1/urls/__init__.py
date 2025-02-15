from django.urls import path, include

urlpatterns = [
    path(
        "",
        include(
            "exam.api.v1.urls.category_urls",
        ),
    ),
    path(
        "",
        include(
            "exam.api.v1.urls.exam_urls",
        ),
    ),
    path(
        "",
        include(
            "exam.api.v1.urls.question_urls",
        ),
    ),
    path(
        "",
        include(
            "exam.api.v1.urls.score_urls",
        ),
    ),
]
