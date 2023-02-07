from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

class Thema(models.Model): #테마
    t_no = models.IntegerField(primary_key=True)    # 테마번호
    t_name = models.CharField(max_length=20)    # 테마이름


class Path(models.Model):   # 구간
    p_no = models.IntegerField(primary_key=True)    # 구간번호
    th_no = models.ForeignKey(Thema, on_delete=models.CASCADE, db_column='t_no')     # FK 테마-테마번호
    p_name = models.CharField(max_length=20)    # 구간이름
    detail = models.TextField()   # 위치(경로)
    distance = models.CharField(max_length=10)  # 길이
    time = models.CharField(max_length=10)  # 시간


