from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    user_profile = models.ImageField(upload_to="user_profiles/", blank=True, null=True)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    dob = models.DateField(null=True, blank=True)


class Profile(models.Model):
    ROLE_CHOICES = [
        ("manager", "Manager"),
        ("employee", "Employee"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    join_date = models.DateField()
    is_delete = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
