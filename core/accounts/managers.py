from django.contrib.auth.models import BaseUserManager
from .choices import USER_ROLE_ADMIN
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):

    def create_user(self, first_name, last_name, phone, password, role, **extera_fields):
        if not phone:
            raise ValueError("pleas set the phone number")
        user = self.model(
            first_name = first_name,
            last_name = last_name, 
            phone = phone, 
            role = role,
            **extera_fields
            )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, phone, password, **extera_fields):
        
        extera_fields.setdefault("is_superuser", True)
        extera_fields.setdefault("is_active", True)
        extera_fields.setdefault("is_staff", True)

        if extera_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is is_staff=True"))
        if extera_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is is_superuser=True"))
        
        user = self.create_user(
            first_name = first_name,
            last_name = last_name, 
            phone = phone, 
            role=USER_ROLE_ADMIN,
            password=password,
            **extera_fields
        ) 
        return user