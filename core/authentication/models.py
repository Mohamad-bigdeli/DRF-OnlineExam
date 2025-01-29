from django.db import models
from utils.otp_generator import create_otp
from utils.kave_sms import SmsMessage
from utils.thread_sms import ThreadSms
from django.utils.timezone import now
from datetime import timedelta

# Create your models here.

class OtpCode(models.Model):
    otp = models.CharField(max_length=6)
    phone = models.CharField(max_length=11)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone
        
    def send_with_sms(self):
        otp = self.otp
        sms_message = SmsMessage(
            receptor=self.phone,
            message=f"otp code:{otp}",
        )
        ThreadSms(sms_message).start()

