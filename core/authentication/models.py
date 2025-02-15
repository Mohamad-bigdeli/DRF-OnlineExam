from django.db import models
from django.utils.timezone import now
from datetime import timedelta

# Create your models here.

class OtpCode(models.Model):
    otp = models.CharField(max_length=6)
    phone = models.CharField(max_length=11)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone
        