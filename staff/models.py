from django.db import models
from django.contrib.auth.models import AbstractUser


class Staff(AbstractUser):
    '''员工表'''

    # first_name = None
    # last_name = None
    sex = (
        ('male', '男'),
        ('female', '女'),
    )

    dep = (
        ('sale', '销售部门'),
        ('purchase', '采购部门'),
        ('manage', '管理部门')
    )

    st_id = models.AutoField(primary_key=True,verbose_name='员工编号')
    username = models.CharField(max_length=255, blank=False, unique=True, verbose_name='姓名')
    # password = models.CharField(max_length=255, blank=False)
    depart = models.CharField(max_length=255, choices=dep, verbose_name='部门')
    job = models.CharField(max_length=255, verbose_name='职位')
    phone = models.CharField(max_length=255, verbose_name='电话')
    gender = models.CharField(max_length=255, choices=sex, verbose_name='性别')

    USERNAME_FIELD = 'st_id'
    REQUIRED_FIELDS = ['username','depart','job', 'phone', 'gender']

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'staff'
        ordering = ['st_id']
        verbose_name = '员工'
        verbose_name_plural = '员工'
