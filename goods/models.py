from django.db import models

# Create your models here.


class Goods(models.Model):
    g_id = models.AutoField(
        primary_key=True, verbose_name='商品编号')
    g_name = models.CharField(max_length=255, blank=False, verbose_name='商品名称')
    g_type = models.CharField(max_length=255, verbose_name='商品类型')
    unit = models.CharField(max_length=255, blank=False, verbose_name='计量单位')
    # p_price = models.ForeignKey(
    #     'purchase.Purchase', on_delete=models.SET_NULL, null=True, verbose_name='进货价格')
    sp_id = models.ForeignKey(
        'supplier.Supplier', on_delete=models.DO_NOTHING, null=True, verbose_name='供货商编号')

    class Meta:
        db_table = 'goods'
        ordering = ['g_id']
        verbose_name = '商品清单'
        verbose_name_plural = '商品清单'
