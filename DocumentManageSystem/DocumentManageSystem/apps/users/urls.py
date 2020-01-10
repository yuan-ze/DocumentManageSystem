from django.urls import path

from . import views

# Register your models here.

urlpatterns = [
    # 测试创建用户
    path('create/', views.CreateUserView.as_view()),
    # 教师注册
    path('regiest/', views.RegiestTeacherView.as_view()),
]
