from django.db import models


from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models.signals import post_save
from PIL import Image

# Create your models here.

# user 확장
# (id, 비밀번호, 이메일, 이름, 전화번호, 주소)

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')

    def __str__(self):
        return {self.user.username}


def on_post_save_for_user(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        Profile.objects.create(user=user)

# User 회원 가입 시 Profile 생성하기
post_save.connect(on_post_save_for_user, sender=settings.AUTH_USER_MODEL)


# 위치 중요!!! 무조건 class보다 아래에 있어야 함!
User = get_user_model()