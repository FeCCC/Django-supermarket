from django.db import models
from django.utils import timezone

# Create your models here.


class Stock(models.Model):
    s_id = models.AutoField(
        primary_key=True, verbose_name='库存编号')
    g_id = models.ForeignKey(
        'goods.Goods', on_delete=models.DO_NOTHING, null=True, verbose_name='商品编号')
    s_num = models.PositiveIntegerField(verbose_name='库存数量')
    s_time = models.DateTimeField(auto_now_add=True, verbose_name='库存最后更新时间')
    sp_id = models.ForeignKey(
        'supplier.Supplier', on_delete=models.DO_NOTHING, null=True, verbose_name='供货商编号')

    class Meta:
        db_table = 'stock'
        ordering = ['s_id']
        verbose_name = '库存清单'
        verbose_name_plural = '库存清单'

    def save(self, *args, **kwargs):
        if not self.s_id:
            self.s_time = timezone.now()
        self.s_time = timezone.now()
        return super(Stock, self).save(*args, **kwargs)
