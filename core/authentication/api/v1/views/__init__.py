from .otp import (
    OTPRequestApiView,
    OTPVerifyApiView,
)
from .users import (
    UserRegistrationApiView,
    UserDestroyApiView,
    CustomTokenObtainPairView,
    ChangePasswordApiView,
)

all = [
    "OTPRequestApiView",
    "OTPVerifyApiView",
    "UserRegistrationApiView" "UserDestroyApiView",
    "CustomTokenObtainPairView",
    "ChangePasswordApiView",
]
