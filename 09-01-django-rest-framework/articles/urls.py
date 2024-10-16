from django.urls import path
from articles import views

# app_name, url 이름 사라짐 (template 안 쓸 거니까)
urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
]
