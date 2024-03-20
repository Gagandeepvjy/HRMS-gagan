from django.contrib import admin

from .models import LeaveRequest, Profile, User

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(LeaveRequest)
