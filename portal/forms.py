from django import forms

from .models import UserProfile


class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "username",
            "user_profile",
            "mobile_number",
            "email",
            "address",
            "dob",
        ]
        widgets = {
            "dob": forms.DateInput(attrs={"class": "datepicker"}),
        }
