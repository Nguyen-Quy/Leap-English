# Generated by Django 4.0.2 on 2022-06-22 14:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0022_alter_lophoc_hours1_alter_lophoc_hours2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lophoc',
            name='hours1',
            field=models.TimeField(default=datetime.datetime(2022, 6, 22, 21, 47, 48, 152884)),
        ),
        migrations.AlterField(
            model_name='lophoc',
            name='hours2',
            field=models.TimeField(default=datetime.datetime(2022, 6, 22, 21, 47, 48, 152884)),
        ),
    ]
