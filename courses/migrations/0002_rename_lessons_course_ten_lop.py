# Generated by Django 4.0.2 on 2022-06-17 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='lessons',
            new_name='ten_lop',
        ),
    ]
