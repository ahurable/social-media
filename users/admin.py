from django.contrib import admin
from .models import CustomUserModel, Profile
# Register your models here.


admin.site.register(CustomUserModel)
admin.site.register(Profile)