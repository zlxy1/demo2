from django.db import models
from django.contrib.auth.models import User

# 科室下拉常量
DEP_CHOICE = [
    ("班子成员", "班子成员"),
    ("退二线科级干部", "退二线科级干部"),
    ("办公室", "办公室"),
    ("党组办公室", "党组办公室"),
    ("财务股", "财务股"),
    ("人事股", "人事股"),
    ("公用事业股", "公用事业股"),
    ("工会", "工会"),
    ("行政审批股", "行政审批股"),
    ("督查大队", "督查大队"),
    ("监察大队", "监察大队"),
    ("公车办公室", "公车办公室"),
    ("环卫大队", "环卫大队"),
    ("一片区", "一片区"),
    ("二片区", "二片区"),
    ("三片区", "三片区"),
    ("四片区", "四片区"),
    ("五片区", "五片区"),
    ("六片区", "六片区"),
    ("七片区", "七片区"),
    ("清运大队", "清运大队"),
    ("油烟办", "油烟办"),
    ("市政大队", "市政大队"),
    ("垃圾中转站", "垃圾中转站"),
    ("污征办", "污征办"),
    ("管网大队", "管网大队"),
    ("数字化城管", "数字化城管"),
    ("垃圾监管办", "垃圾监管办"),
    ("供水办", "供水办"),
    ("污水办", "污水办"),
    ("公厕办", "公厕办"),
    ("渣土大队", "渣土大队"),
    ("机扫大队", "机扫大队"),
    ("广告办", "广告办"),
    ("燃气办", "燃气办"),
    ("供热办", "供热办"),
    ("综合执法局", "综合执法局"),
    ("市场中心", "市场中心"),
    ("驻村人员", "驻村人员"),
    ("乡镇综合执法大队挂职人员", "乡镇综合执法大队挂职人员"),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='upload/', default='upload/default.jpg', blank=True)
    nickname = models.CharField(max_length=30, blank=True, default='', verbose_name='昵称')
    is_admin = models.BooleanField(default=False, verbose_name='是否为管理员')
    dep = models.CharField(max_length=20, choices=DEP_CHOICE, blank=True, verbose_name='所属科室')

    class Meta:
        verbose_name = '用户详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username
