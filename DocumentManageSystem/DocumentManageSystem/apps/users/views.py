from django.shortcuts import render
from django.views import View
from django import http

from users.models import UserModel


# Create your views here.


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
