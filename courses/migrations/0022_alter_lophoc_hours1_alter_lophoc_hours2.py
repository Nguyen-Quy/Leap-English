# Generated by Django 4.0.2 on 2022-06-22 01:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0021_alter_course_course_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lophoc',
            name='hours1',
            field=models.TimeField(default=datetime.datetime(2022, 6, 22, 8, 12, 18, 748054)),
        ),
        migrations.AlterField(
            model_name='lophoc',
            name='hours2',
            field=models.TimeField(default=datetime.datetime(2022, 6, 22, 8, 12, 18, 748054)),
        ),
    ]
