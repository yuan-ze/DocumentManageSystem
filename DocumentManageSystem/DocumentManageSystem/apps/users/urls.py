from django.urls import path

from . import views

# Register your models here.

urlpatterns = [
    # 测试创建用户
    path('create/', views.CreateUserView.as_view()),
    # 教师注册
    path('register/', views.RegisterTeacherView.as_view()),
    # 用户登录
    path('login/', views.LoginView.as_view()),
]
