# Generated by Django 3.2.4 on 2021-06-30 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0003_auto_20210630_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='sa_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='销售编号'),
        ),
    ]
