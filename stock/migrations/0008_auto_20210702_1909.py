# Generated by Django 3.2.4 on 2021-07-02 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0007_alter_goods_sp_id'),
        ('stock', '0007_remove_stock_st_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='g_name',
        ),
        migrations.AlterField(
            model_name='stock',
            name='g_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='goods.goods', verbose_name='商品编号'),
        ),
    ]
