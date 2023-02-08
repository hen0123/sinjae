from django.contrib import admin
from .models import Profile

# Register your models here.

# User 모델 확장
from django.contrib.auth.admin import UserAdmin


from django.contrib.auth import get_user_model
User = get_user_model()

admin.site.register(User, UserAdmin)

admin.site.register(Profile)