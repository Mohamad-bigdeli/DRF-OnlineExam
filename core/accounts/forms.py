from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone"]

    def clean_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("passwords doesn't match")

        return password2

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")

        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError("Phone already exist.")
        if not phone.isdigit():
            raise forms.ValidationError("Invalid phone number.")
        if not phone.startswith("09"):
            raise forms.ValidationError("Phone must start with 09 digits.")
        return phone

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone", "is_active", "role"]

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")

        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError("Phone already exist.")
        if not phone.isdigit():
            raise forms.ValidationError("Invalid phone number.")
        if not phone.startswith("09"):
            raise forms.ValidationError("Phone must start with 09 digits.")
        return phone
