# Generated by Django 4.0.2 on 2022-07-05 07:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0032_alter_lophoc_hours1_alter_lophoc_hours2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lophoc',
            name='hours1',
            field=models.TimeField(default=datetime.datetime(2022, 7, 5, 14, 35, 3, 705567)),
        ),
        migrations.AlterField(
            model_name='lophoc',
            name='hours2',
            field=models.TimeField(default=datetime.datetime(2022, 7, 5, 14, 35, 3, 705567)),
        ),
    ]
