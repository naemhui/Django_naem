from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    # 게시글 전체 조회 요청 to DB
    # 모델클래스.objects.all() -> 모델 클래스 가져와야 됨. 
    # 근데 model은 동일한 위치에 있음. 가져오면 됨 -> import
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request, 'articles/index.html', context)  # 이제 드디어 쿼리셋 사용 가능
    # 약속된 경로 이후의 것만 작성