from django.db import models


# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    user_profile = models.ImageField(upload_to="user_profiles/", blank=True, null=True)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    dob = models.DateField()

    def __str__(self):
        return self.username
