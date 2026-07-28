from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    avatar=models.ImageField(upload_to='upload/', default='upload/default.png', blank=True)
    nickname=models.CharField(max_length=30,blank=True,default='',verbose_name='昵称')

    class Meta:
        verbose_name='用户详情'