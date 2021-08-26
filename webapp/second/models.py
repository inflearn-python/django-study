from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)  # 데이터가 실제로 생성될 때 현재시간이 자동으로 기록
    updated_at = models.DateTimeField(auto_now=True)  # 수정될때만 자동으로 등록
