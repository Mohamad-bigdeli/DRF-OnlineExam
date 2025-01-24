from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from . import choices
from .managers import UserManager

# Create your models here.

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    phone = models.CharField(max_length=11, unique=True)
    role = models.CharField(choices=choices.USER_ROLE_CHOICES, max_length=20)

    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return self.phone
    
    @property
    def is_staff(self):
        return self.role == choices.USER_ROLE_ADMIN
    
    @property
    def is_instructor(self):
        return self.role == choices.USER_ROLE_INSTRUCTOR
    
    @property
    def is_student(self):
        return self.role == choices.USER_ROLE_STUDENT
    
    
