from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserModel(AbstractUser):
    """用户模型"""
    # 学号/工号
    index = models.IntegerField(null=False)
    # 姓名
    name = models.CharField(max_length=10, null=False)
    # 性别
    sex = models.CharField(max_length=10, null=False)
    # 身份
    role = models.CharField(max_length=10, null=False)

    class Meta:
        db_table = 'tb_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
