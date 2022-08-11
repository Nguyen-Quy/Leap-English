# Generated by Django 4.0.2 on 2022-06-22 01:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_rename_price_course_course_price1_remove_lophoc_days_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lophoc',
            name='hours1',
            field=models.TimeField(default=datetime.datetime(2022, 6, 22, 8, 6, 13, 495775)),
        ),
        migrations.AlterField(
            model_name='lophoc',
            name='hours2',
            field=models.TimeField(default=datetime.datetime(2022, 6, 22, 8, 6, 13, 495775)),
        ),
        migrations.AlterField(
            model_name='lophoc',
            name='lophoc_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lophoc',
            name='lophoc_start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
