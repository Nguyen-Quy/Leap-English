# Generated by Django 4.0.2 on 2022-06-19 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_student_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_birth',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
