from django.db import models

# Create your models here.
gender_choice=[('M','男'),('F','女')]
staff_type_choice=[('正式人员','正式人员'),('环卫人员','环卫人员'),('政府购岗人员','政府购岗人员'),('公益4050人员','公益4050人员')]
work_status_choices=[('在职','在职'),('离职','离职'),('退休','退休')]
area_choice= [
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
class Staff(models.Model):
    name=models.CharField(max_length=50,verbose_name='姓名')
    gender=models.CharField(max_length=2,choices=gender_choice,verbose_name='性别')
    birth=models.DateField(verbose_name='出生日期')
    id_number=models.CharField(max_length=18,verbose_name='身份证号')
    staff_type=models.CharField(max_length=50,choices=staff_type_choice,verbose_name='人员类型')
    work_status=models.CharField(max_length=50,choices=work_status_choices,verbose_name='在职状态')
    work_area=models.CharField(max_length=50,choices=area_choice,verbose_name='所属科室')

    class Meta:
        verbose_name = "城管局员工"
        verbose_name_plural = "员工信息台账"


