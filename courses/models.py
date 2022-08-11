from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from .myfields import FieldNgayTrongTuan as ntt
import datetime
from embed_video.fields import EmbedVideoField
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Category(models.Model):
    phanloai = models.CharField(max_length=20)

    def __str__(self):
        return str(self.phanloai)


class Course(models.Model):
    ten_khoahoc = models.CharField(max_length=150)
    description = RichTextUploadingField(blank=True)
    course_price1 = models.FloatField(default=500000)
    course_price2 = models.FloatField(default=500000)
    course_start_date = models.DateField(blank=True)
    course_end_date = models.DateField(blank=True)
    photo = models.ImageField(
        upload_to="courses/images", default="courses/images/english-time.jpg")
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.ten_khoahoc)


class LopHoc(models.Model):
    ten_lop = models.CharField(max_length=100)
    hinh = models.ImageField(upload_to="courses/images",
                             default="courses/images/course-1.jpg")
    description = RichTextUploadingField(blank=True)
    lophoc_start_date = models.DateField(blank=True, null=True)
    lophoc_end_date = models.DateField(blank=True, null=True)
    price = models.FloatField(default=500000)
    discount = models.FloatField(default=0)
    days1 = ntt(max_length=50, default="Chủ Nhật", blank=True)
    days2 = ntt(max_length=50, default="Chủ Nhật", blank=True)
    days3 = ntt(max_length=50, default="Chủ Nhật", blank=True)
    hours1 = models.TimeField(default=datetime.datetime.now())
    hours2 = models.TimeField(default=datetime.datetime.now())
    course_id = models.ForeignKey(Course, on_delete=models.PROTECT)
    teacher_id = models.ForeignKey(
        "main.Teacher", on_delete=models.PROTECT)

    def __str__(self):
        return str(self.ten_lop)

    def get_price(self):
        price = int(self.price*(100-self.discount)/100)
        return price


class BaiHoc(models.Model):
    ten_bai = models.CharField(max_length=50)
    content = RichTextUploadingField(blank=True)
    lecture = EmbedVideoField(blank=True)
    lophoc_id = models.ForeignKey(LopHoc, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.ten_bai)
