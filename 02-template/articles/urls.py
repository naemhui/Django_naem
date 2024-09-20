from django.urls import path
# 명시적 상대경로 (장고에서 권장하는 방법) 현재 위치로
from . import views

urlpatterns = [
    path('index/', views.index),
    path('dinner/', views.dinner),
    path('search/', views.search),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('hello/<str:name>', views.greeting),
]