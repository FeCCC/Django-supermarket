# Generated by Django 3.2.4 on 2021-07-02 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0005_auto_20210701_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='unit',
            field=models.CharField(max_length=255, null=True, verbose_name='计量单位'),
        ),
    ]
