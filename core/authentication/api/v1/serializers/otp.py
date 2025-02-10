from rest_framework import serializers
from utils.validators import phone_regex
from ....models import OtpCode
from utils.otp_generator import create_otp
from django.core.cache import cache
from django.conf import settings

class OTPRequestSerializer(serializers.Serializer):

    phone = serializers.CharField(max_length=11, validators=[phone_regex])

    def create(self, validated_data):
        otp_code = create_otp()
        otp, created = OtpCode.objects.get_or_create(otp=otp_code, phone=validated_data["phone"])
        cache.set(validated_data["phone"], otp.otp, settings.EXPIRY_TIME_OTP)
        otp.send_with_sms()
        return otp

class OTPVerifySerializer(serializers.Serializer):
    
    otp = serializers.CharField(max_length=6)
    phone = serializers.CharField(max_length=11, validators=[phone_regex])
