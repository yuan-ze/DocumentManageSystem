from django.contrib.auth import login
from django.shortcuts import render
from django.views import View
from django import http
import re

from users.models import UserModel, TeacherModel


# Create your views here.

class LoginView(View):
    """用户登录"""

    def post(self, request):
        # 接收参数
        try:
            username = request.POST['username']
            password = request.POST['password']
        except:
            return http.HttpResponseForbidden('缺少必传参数')

        # 用户验证
        user = UserModel.objects.get(username=username)
        if user is None:
            return http.HttpResponseForbidden('用户不存在')
        if not user.check_password(password):
            return http.HttpResponseForbidden('密码输入错误')

        # 验证通过，实现状态保持
        login(request, user)

        return http.JsonResponse({'msg': '登录成功'})


class RegisterTeacherView(View):
    """教师注册"""

    def post(self, request):
        # 接收参数
        try:
            username = request.POST['username']
            password = request.POST['password']
            password2 = request.POST['password2']
            name = request.POST['name']
            sex = request.POST['sex']
            college = request.POST['college']
            title = request.POST['title']
        except:
            return http.HttpResponseForbidden('缺少必传参数')

        # 校验参数
        if not username.isdigit():
            return http.HttpResponseForbidden('工号必须为数字')
        if not re.match(r'^[a-zA-Z0-9]{8,20}$', password):
            return http.HttpResponseForbidden('请输入8-20个字符的密码')
        if password != password2:
            return http.HttpResponseForbidden('两次输入的密码不一致')
        if name == '':
            return http.HttpResponseForbidden('请输入姓名')
        if sex not in ['男', '女']:
            return http.HttpResponseForbidden('请输入性别')
        # 创建用户
        try:
            user = UserModel.objects.create_user(
                username=username,
                password=password,
                name=name,
                sex=sex,
                role='teacher'
            )
            TeacherModel.objects.create(
                index=username,
                college=college,
                title=title
            )
        except:
            return http.JsonResponse({'msg': '注册失败'})

        # 注册完毕，实现状态保持进入登录
        login(request, user)

        # 返回响应
        return http.JsonResponse({'msg': '注册成功'})


class CreateUserView(View):
    """创建用户"""

    def post(self, request):
        # 接收参数
        try:
            index = request.POST['index']
            username = request.POST['username']
            password = request.POST['password']
            name = request.POST['name']
            sex = request.POST['sex']
            role = request.POST['role']
        except:
            return http.HttpResponseForbidden('缺少必传参数')
        # 创建用户
        try:
            UserModel.objects.create_user(
                index=index,
                username=username,
                password=password,
                name=name,
                sex=sex,
                role=role
            )
        except:
            return http.JsonResponse({'msg': 'ERROR'})

        # 返回响应
        return http.JsonResponse({'msg': 'OK'})
