from .otp import (
    OTPRequestSerializer,
    OTPVerifySerializer,
)
from .users import (
    RegistrationSerializer,
    CustomTokenObtainPairSerializer,
    ChangePasswordSerializer,
)

all = [
    "OTPRequestSerializer",
    "OTPVerifySerializer",
    "RegistrationSerializer",
    "CustomTokenObtainPairSerializer",
    "ChangePasswordSerializer",
]
