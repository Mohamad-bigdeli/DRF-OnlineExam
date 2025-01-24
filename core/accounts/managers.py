from django.contrib.auth.models import BaseUserManager
from .choices import USER_ROLE_ADMIN

class UserManager(BaseUserManager):

    def create_user(self, first_name, last_name, phone, password, role):
        if not phone:
            raise ValueError("pleas set the phone number")
        user = self.model(
            first_name = first_name,
            last_name = last_name, 
            phone = phone, 
            role = role
            )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, phone, password):
        
        user = self.create_user(
            first_name = first_name,
            last_name = last_name, 
            phone = phone, 
            role=USER_ROLE_ADMIN,
            password=password
        ) 
        return user