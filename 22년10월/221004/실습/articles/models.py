from django.db import models

# Create your models here.
# 모델 생성
# 기본 구성
# 제목 : 문자열(char). 최대 글자수 제한
# 내용 : text. (null 금지)
# 생성 날짜 : 지금 날짜 자동 입력
# 수정 날짜 : 지금 날짜 자동 입력


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
