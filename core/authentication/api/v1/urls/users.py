from django.urls import path, include
from ..views import (
    UserRegistrationApiView,
    UserDestroyApiView,
    CustomTokenObtainPairView,
    ChangePasswordApiView,
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    # registration
    path("register/", UserRegistrationApiView.as_view(), name="register"),
    # delete user
    path("delete/", UserDestroyApiView.as_view(), name="delete"),
    # change password
    path(
        "change-password/",
        ChangePasswordApiView.as_view(),
        name="change-password",
    ),
    # jwt login
    path(
        "jwt/create/",
        CustomTokenObtainPairView.as_view(),
        name="jwt-create",
    ),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
]
