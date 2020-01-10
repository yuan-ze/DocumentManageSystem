from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class TeacherModel(models.Model):
    """教师模型"""
    # 工号
    index = models.CharField(max_length=12, null=False)
    # 院系
    college = models.CharField(max_length=50, null=False)
    # 职称
    title = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'tb_teacher'
        verbose_name = '教师表'
        verbose_name_plural = verbose_name


class StudentModel(models.Model):
    """学生模型"""
    # 学号
    index = models.CharField(max_length=12, null=False)
    # 年级
    grade = models.IntegerField(null=False)
    # 院系
    college = models.CharField(max_length=50, null=False)
    # 专业
    major = models.CharField(max_length=50, null=False)
    # 班级
    classes = models.IntegerField(null=False)
    # 负责教师工号
    teacher = models.IntegerField(null=False)

    class Meta:
        db_table = 'tb_student'
        verbose_name = '学生表'
        verbose_name_plural = verbose_name


class UserModel(AbstractUser):
    """用户模型"""
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
