# Generated by Django 4.0.2 on 2022-06-18 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_remove_ngayhoc_days_ngayhoc_days_delete_lst_ngay'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectWeekday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='ngayhoc',
            name='days',
        ),
        migrations.AddField(
            model_name='ngayhoc',
            name='days',
            field=models.ManyToManyField(to='courses.SelectWeekday'),
        ),
    ]
