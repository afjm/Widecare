from django.db import models
from django.urls import reverse


# Create your models here.

class Position(models.Model):
    name = models.CharField(max_length=20, verbose_name='岗位名称')
    description = models.TextField(verbose_name='岗位描述')
    requirement = models.TextField(verbose_name='任职要求')
    location = models.CharField(max_length=20, verbose_name='工作地点')
    salary = models.CharField(max_length=20, verbose_name='薪资范围')
    is_on = models.BooleanField(verbose_name='启用', default=True)
    comment = models.TextField(blank=True, verbose_name='备注')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hr:position_detail', args=str(self.id))

    class Meta:
        ordering = ['name']


class Staff(models.Model):
    DP_CHOICES = ((0, '财务'), (1, '服务'), (2, '销售'), (3, '人事'),)
    SEX_CHOICES = (('M', '男'), ('F', '女'),)
    name_en = models.CharField(max_length=20, verbose_name='Name')
    name_cn = models.CharField(max_length=20, verbose_name='姓名')
    sex = models.CharField(max_length=5, verbose_name='性别', default='M', choices=SEX_CHOICES)
    department = models.IntegerField(verbose_name='部门', choices=DP_CHOICES)
    position = models.ForeignKey(Position, verbose_name='职位')
    email = models.EmailField()
    cellphone = models.CharField(max_length=20, verbose_name='手机')
    is_on = models.BooleanField(verbose_name='在职', default=True)
    phone = models.CharField(blank=True, max_length=20, verbose_name='电话')
    address = models.CharField(blank=True, max_length=100, verbose_name='住址')
    qq = models.CharField(blank=True, max_length=20, verbose_name='QQ')
    wechat = models.CharField(blank=True, max_length=20, verbose_name='微信')
    resume = models.FileField(blank=True, verbose_name='简历')
    comment = models.TextField(blank=True, verbose_name='备注')

    def __str__(self):
        return self.name_en

    def get_absolute_url(self):
        return reverse('hr:staff_detail', args=str(self.id))

    class Meta:
        ordering = ['name_en']
