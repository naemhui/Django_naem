from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash

from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


# 2개의 뷰함수 (1. 2.POST로 받아 실제로 진행해주는) 
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        # ModelForm의 첫 번째 인자는 데이터
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)


# signout
@login_required
def delete(request):
    # 원래라면 User 모델에서 누가 회원탈퇴를 요청한 건지 검색해야 함
    # 근데 여기서는 누가 요청한 건지 User 모델에서 검색할 필요가 없다.
    # request 객체에 요청을 보내는 user 정보가 함께 들어있기 때문에
    request.user.delete()
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)

@login_required
def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)  # 얘 순서 다르다
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # 세션 무효화 방지
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form' : form
    }
    return render(request, 'accounts/change_password.html', context)