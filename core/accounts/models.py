from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from . import choices
from .managers import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    phone = models.CharField(max_length=11, unique=True)
    role = models.CharField(choices=choices.USER_ROLE_CHOICES, max_length=20)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return self.phone
    
    @property
    def is_instructor(self):
        return self.role == choices.USER_ROLE_INSTRUCTOR
    
    @property
    def is_student(self):
        return self.role == choices.USER_ROLE_STUDENT
    
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    
