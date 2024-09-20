from django.db import models

# Create your models here.
class Article(models.Model):  # 상속 (2000줄짜리 상속 받음)
    title = models.CharField(max_length=10)  # 이거 함수 아님. 클래스임
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    # 2번보다는 1번을 쓸 것