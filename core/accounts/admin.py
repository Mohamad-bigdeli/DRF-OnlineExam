from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import UserChangeForm, UserCreationForm


class CustomUserAdmin(UserAdmin):
    """
    Custom admin panel for user management with add and change forms plus password
    """
    
    form = UserChangeForm
    add_form = UserCreationForm

    model = User
    list_display = ("phone", "first_name", "last_name", "role", "is_active", "is_staff", "is_superuser")
    list_filter = ("phone", "role", "is_active", "is_superuser")
    searching_fields = ("phone",)
    ordering = ("phone",)
    filter_horizontal = []
    fieldsets = (
        (
            "Authentication",
            {
                "fields": ("phone", "password"),
            },
        ),
        (
            "permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (
            "group permissions",
            {
                "fields": ("groups", "user_permissions"),
            },
        ),
        (
            "important date",
            {
                "fields": ("last_login",),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )

admin.site.register(User, CustomUserAdmin)