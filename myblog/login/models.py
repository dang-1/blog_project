from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=20, blank=True, null=True, verbose_name='用户名')
    user_password = models.CharField(max_length=20, blank=True, null=True, verbose_name='密码')
    user_mail = models.CharField(max_length=20, blank=True, null=True, verbose_name='邮箱')

