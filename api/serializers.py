from rest_framework import serializers

from portal.models import User


class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "user_profile",
            "mobile_number",
            "address",
            "dob",
        ]
