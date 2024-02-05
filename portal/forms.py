from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User


class UserForm(forms.ModelForm):
    dob = forms.DateField(
        input_formats=["%d-%m-%Y"],
        widget=forms.DateInput(attrs={"class": "datepicker", "format": "%d-%m-%Y"}),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "user_profile",
            "mobile_number",
            "address",
            "dob",
        )
        widgets = {
            "password": forms.PasswordInput(render_value=False),
            "dob": forms.DateInput(attrs={"class": "datepicker"}),
        }


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
