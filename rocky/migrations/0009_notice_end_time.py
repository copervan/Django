# Generated by Django 2.0.4 on 2018-10-03 07:21

from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ('rocky', '0008_book_introduction'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='End_time'),
        ),
    ]
