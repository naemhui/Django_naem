from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# django에서는 이걸 하지 말라고 함 : User 모델을 직접 참조하는 것을 권장하지 않음
# from .models import User
# class Meta(UserCreationForm):
#     model = User()
# 그래서 django는 User모델을 간접적으로 참조할 수 있는 방법을 별도로 제공한다.
from django.contrib.auth import get_user_model  # 활성화된 User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # 위까지 한 후, model 만 갈아끼우면 됨
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    # password = None

    class Meta(UserChangeForm.Meta):  # 상속 받고
        model = get_user_model()  # 여기만 재정의
        fields = ('first_name', 'last_name', 'email',)
