from django.db import models

class Thema(models.Model):  # 테마
    t_no = models.IntegerField(primary_key=True)  # 테마번호
    t_name = models.CharField(max_length=20)  # 테마이름

