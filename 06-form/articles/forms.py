from django import forms
from .models import Article

# 게시글 생성을 위한 form이기 때문에 ArticleForm으로 이름 짓기
# class ArticleForm(forms.Form):
    # 사용자로부터 입력 받는 수단이기 때문에 다음 두 가지만 정의
    # title = forms.CharField(max_length=10)
    # content = forms.CharField(widget=forms.Textarea)
    # 근데! ModelForm 쓰면 위 코드 필요 없음

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget=forms.TextInput(
            attrs={
                'class':'my-title',
                'placeholder' : '제목을 입력해주세요',
                'maxlength' : 10,
            }
        ),
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class':'my-content',
                'placeholder' : 'Enter the content',
                'rows' : 5,
                'cols' : 50,
            }
        )
        ,
        error_messages={'required' : '내용을 입력해주세요.'}
    )

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)  # 사용자에게 입력받는 것 중 title은 빼겠다
