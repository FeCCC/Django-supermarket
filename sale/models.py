from django.db import models

# Create your models here.


class Sale(models.Model):
    sa_id = models.AutoField(
        primary_key=True, verbose_name='销售编号')
    g_id = models.ForeignKey('goods.Goods', on_delete=models.DO_NOTHING,
                             null=True, related_name='sa_goods_id', verbose_name='商品编号')
    s_num = models.PositiveIntegerField(verbose_name='销售数量')
    st_id = models.ForeignKey(
        'staff.Staff', on_delete=models.DO_NOTHING, null=True, verbose_name='员工编号')
    s_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='销售价格')
    s_time = models.DateTimeField(auto_now_add=True, verbose_name='销售时间')

    class Meta:
        db_table = 'sale'
        ordering = ['sa_id']
        verbose_name = '销售清单'
        verbose_name_plural = '销售清单'
