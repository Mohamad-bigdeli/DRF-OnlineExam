from django.urls import path, include

app_name = "exam"

urlpatterns = [
    path("api/v1/", include("exam.api.v1.urls")),
]