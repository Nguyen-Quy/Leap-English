# Generated by Django 4.0.2 on 2022-06-18 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_class_price_alter_teacher_photo'),
        ('courses', '0004_course_photo_course_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='NgayHoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngay', models.CharField(max_length=8)),
            ],
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='phanloai',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='ten_lop',
            new_name='ten_khoahoc',
        ),
        migrations.CreateModel(
            name='LopHoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_lop', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.course')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='GioHoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.CharField(max_length=50)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.lophoc')),
                ('ngayhoc_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.ngayhoc')),
            ],
        ),
        migrations.CreateModel(
            name='ClassStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.lophoc')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.student')),
            ],
        ),
    ]