from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    # variable routing 안 하는 이유 : views.py delete 참고
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
]
