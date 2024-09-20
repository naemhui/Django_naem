from django.contrib import admin

# Register your models here.
from .models import Article  # 현재 경로에 있는 models에서 Article 가져옴
admin.site.register(Article)  # admin site에 등록한다 로 외우기