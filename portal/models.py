from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    user_profile = models.ImageField(upload_to="user_profiles/", blank=True, null=True)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    dob = models.DateField(null=True, blank=True)
