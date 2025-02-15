from django.urls import path, include

urlpatterns = [
    path("otp/", include("authentication.api.v1.urls.otp")),
    path("users/", include("authentication.api.v1.urls.users")),
]
