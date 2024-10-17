from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'content',
        )

# 댓글 단일조회 할 때 쓰고 있는 클래스
class ArticleSerializer(serializers.ModelSerializer):
    class CommentDerailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content',)

    # comment_set 역참조 데이터를 override
    comment_set = CommentDerailSerializer(read_only=True, many=True)
    # 댓글 개수 제공을 위한 새로운 필드 생성
    # source 속성: 필드를 채우는 데 사용할 속성의 이름
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class ArticletitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)

    # 기존 article 데이터 값을 override
    # 그런데 기존 필드를 override하게 되면 Meta 클래스의 read_only_fields 사용 못함
    # 모델 시리얼라이저의 read_only인자 값으로 재설정
    article = ArticletitleSerializer(read_only=True)

    class Meta:
        model = Comment
        # fields에 작성된 필드는 모두 유효성 검사 목록에 포함됨
        fields = '__all__'

        # 외래키 필드를 읽기전용 필드로 지정
        # 이유는?
        # 외래키 데이터는
        # 유효성 검사에서 제외, 결과 데이터에는 포함하고 싶음
        read_only_fields = ('article',)