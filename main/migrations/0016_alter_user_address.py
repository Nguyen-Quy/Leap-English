# Generated by Django 4.0.2 on 2022-07-05 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_user_fullname_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]
