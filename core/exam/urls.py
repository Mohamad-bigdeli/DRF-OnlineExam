from django.urls import path, include

urlpatterns = [
    path("api/v1/", include("exam.api.v1.urls")),
]