# Generated by Django 4.0.2 on 2022-06-17 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_classweekday_class_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='price',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(default='main/images/trainer-2.jpg', upload_to='main/images'),
        ),
    ]