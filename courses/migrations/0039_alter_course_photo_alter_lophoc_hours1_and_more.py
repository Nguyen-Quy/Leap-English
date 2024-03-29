# Generated by Django 4.0.6 on 2022-07-13 03:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0038_lophoc_hinh_alter_lophoc_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='photo',
            field=models.ImageField(default='courses/images/english-time.jpg', upload_to='courses/images'),
        ),
        migrations.AlterField(
            model_name='lophoc',
            name='hours1',
            field=models.TimeField(default=datetime.datetime(2022, 7, 13, 10, 4, 50, 120035)),
        ),
        migrations.AlterField(
            model_name='lophoc',
            name='hours2',
            field=models.TimeField(default=datetime.datetime(2022, 7, 13, 10, 4, 50, 120035)),
        ),
    ]
