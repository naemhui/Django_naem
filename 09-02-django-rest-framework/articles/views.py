from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_list_or_404
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_list_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(
            article, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



@api_view(['GET'])
def comment_list(request):
    # 댓글 전체 조회
    comments = Comment.objects.all()
    # 댓글 목록 쿼리셋을 직렬화(serialization)
    # 어떤 포맷이든 재가공하기 쉽게 하는 것
    # 어떤 운영체재나 언어를 쓰는 개발자든 유연하게 사용할 수 있도록
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # 단일 대글 조회
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'GET':
        # 단일 댓글 직렬화
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)    


@api_view(['POST'])
def comment_create(request, article_pk):
    # 게시글 조회 (어떤 게시글에 작성되는 댓글인지)
    article = Article.objects.get(pk=article_pk)
    # 사용자 입력 데이터를 직렬화 (사용자가 입력한 댓글 데이터) -> 외래키 없음
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # 외래키 데이터 입력 후 저장
        # article(serializers.py의 필드명) = article(위의 변수명)
        serializer.save(article=article)  # drf의 modelserializer에서는 이렇게 넣음
        return Response(serializer.data, status=status.HTTP_201_CREATED)