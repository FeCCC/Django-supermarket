# Generated by Django 3.2.4 on 2021-06-30 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0004_auto_20210630_2135'),
        ('supplier', '0002_auto_20210630_2125'),
        ('sale', '0002_auto_20210630_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='g_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sa_goods_id', to='goods.goods', verbose_name='商品编号'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='g_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sa_goods_name', to='goods.goods', verbose_name='商品名称'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='sp_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supplier.supplier', verbose_name='供货商编号'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='st_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='员工编号'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sa_goods_unit', to='goods.goods', verbose_name='计量单位'),
        ),
    ]
