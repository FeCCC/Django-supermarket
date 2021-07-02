from django.db import models

# Create your models here.


class Purchase(models.Model):
    p_id = models.AutoField(
        primary_key=True, verbose_name='进货编号')
    g_id = models.ForeignKey('goods.Goods', on_delete=models.DO_NOTHING,
                             null=True, related_name='p_goods_id', verbose_name='商品编号')
    p_num = models.PositiveIntegerField(verbose_name='进货数量')
    st_id = models.ForeignKey(
        'staff.Staff', on_delete=models.DO_NOTHING, null=True, verbose_name='员工编号')
    p_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='进货价格')
    p_time = models.DateTimeField(auto_now_add=True, verbose_name='进货时间')
    sp_id = models.ForeignKey(
        'supplier.Supplier', on_delete=models.DO_NOTHING, null=True, verbose_name='供货商编号')

    class Meta:
        db_table = 'purchase'
        ordering = ['p_id']
        verbose_name = '进货清单'
        verbose_name_plural = '进货清单'
