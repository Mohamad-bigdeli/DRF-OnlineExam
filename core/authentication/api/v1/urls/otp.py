from django.urls import path, include
from ..views import (OTPRequestApiView, OTPVerifyApiView)

urlpatterns = [
    path('otp-request/', OTPRequestApiView.as_view(), name='otp_request'),
    path('otp-verify/', OTPVerifyApiView.as_view(), name='otp_verify'),
]