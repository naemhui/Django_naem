from django.shortcuts import render, redirect
# 모델 클래스 가져오기
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    # 게시글 전체 조회 요청 to DB
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    # url로부터 전달받은 pk를 활용해 데이터를 조회
    # article = Article.objects.get(id=pk)
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


#######################################
def create(request):
    # 요청 메서드가 POST일 때
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)

    # 요청 메서드가 POST가 아닐 때 (GET일 때라고 하지 않았다!!!!!!)
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }

    return render(request, 'articles/create.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)
###########################################
# def new(request):
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }
#     # 게시글 작성 페이지 응답
#     return render(request, 'articles/new.html', context)


# def create(request):
#     # 1. 모델폼 인스턴스 생성 (+사용자 입력 데이터를 통째로 인자로 작성)
#     # field가 몇 개건 간에 그냥 아래처럼 통째로 넣어라
#     form = ArticleForm(request.POST)

#     # 2. 유효성 검사 : 이거 한 줄로 다 할 수 있음
#     # form.is_valid()  # return이 뭘까? T/F. 실패했다면 이유도 같이 알려줌
#     if form.is_valid():
#         article = form.save()  # 게시글 생성하는 코드이므로 return은 지금 막 생성한 article 객체이므로 이렇게 활용 가능
#         return redirect('articles:detail', article.pk)
    
#     # 다음은 유효성 검사 통과 못한 form -> 이유도 같이 알려줌
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html', context)
    ######################
    # 3. 저장


    # 1. 사용자 요청으로부터 입력 데이터를 추출
    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # article = Article(title=title, content=content)
    # article.save()
    # return redirect('articles:detail', article.pk)
####################################################


def delete(request, pk):
    # 어떤 게시글 삭제할지 조회
    article = Article.objects.get(pk=pk)

    # 조회한 게시글 삭제
    article.delete()
    return redirect('articles:index')


############################
# def edit(request, pk):
#     # 어떤 게시글을 수정할지 조회
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)


# def update(request, pk):
#     article = Article.objects.get(pk=pk)
#     # 1. 모델폼 인스턴스 생성 (+사용자 입력 데이터 & 기존 데이터)
#     form = ArticleForm(request.POST, instance=article)
#     # 2. 유효성 검사
#     if form.is_valid():
#         form.save()
#         return redirect('articles:detail', article.pk)
#     context = {
#         'article' : article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)

    # # 1. 어떤 게시글 수정할지 조회
    # article = Article.objects.get(pk=pk)
    # # 2. 사용자로부터 받은 새로운 입력 데이터 추출
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # # 3. 기존 게시글의 데이터를 사용자로 받은 데이터로 새로 할당
    # article.title = title
    # article.content = content
    # # 4. 저장
    # article.save()

