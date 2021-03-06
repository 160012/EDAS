from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html

sex_fields = [
    ('男', '男'),
    ('女', '女'),
]
leader = ['张宁超', '于俊凯', '尚进', '修鸿博', '杨旭', '刘梦',
          '王洪明', '董一燃', '张源', '黄继成', '曲泰安']

dor_fields = [
    ('1号楼112', '1号楼112'),
    ('8号楼142', '8号楼142'),
    ('8号楼144', '8号楼144'),
    ('1号楼115', '1号楼115'),
    ('2号楼301', '2号楼301'),
    ('1号楼114', '1号楼114'),
    ('1号楼116', '1号楼116'),
    ('1号楼105', '1号楼105'),
    ('1号楼110', '1号楼110'),
]


class Student(AbstractUser):
    username = models.CharField(max_length=20, unique=True, verbose_name='学号')
    name = models.CharField(max_length=20, verbose_name='姓名')
    sex = models.CharField(max_length=20, choices=sex_fields, verbose_name='性别')
    phone = models.CharField(max_length=20, verbose_name='手机号码')
    qq = models.CharField(max_length=20, verbose_name='QQ号码')
    dor = models.CharField(max_length=20, choices=dor_fields, verbose_name='寝室')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '学生列表'
        verbose_name_plural = '学生列表'

    def colored_name(self):
        if self.name in leader:
            color_code = 'red'
        else:
            color_code = 'blue'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            self.name,
        )
    colored_name.short_description = '姓名'

