# Generated by Django 2.0.7 on 2018-08-09 02:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rocky', '0002_auto_20180729_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 9, 10, 34, 29, 634897), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 9, 10, 34, 29, 634897), verbose_name='更新时间'),
        ),
    ]
