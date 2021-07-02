from django.db import models

# Create your models here.
class Supplier(models.Model):
  sp_id = models.AutoField(primary_key=True,unique=True,verbose_name='供货商编号')
  sp_name = models.CharField(max_length=255, blank=False, verbose_name='供货商名称')
  address = models.CharField(max_length=255, blank=False, verbose_name='地址')
  c_person = models.CharField(max_length=255, blank=False, verbose_name='联系人')
  c_phone = models.CharField(max_length=255, blank=False, verbose_name='联系电话')

  class Meta:
        db_table = 'supplier'
        ordering = ['sp_id']
        verbose_name = '供货商'
        verbose_name_plural = '供货商'