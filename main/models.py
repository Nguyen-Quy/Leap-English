from django.db import models
from courses.models import models
import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from phone_field import PhoneField
from django.contrib.auth.models import User
# Create your models here.

# Teacher Models


class Teacher(models.Model):
    description = models.CharField(max_length=300)
    photo = models.ImageField(upload_to="main/images",
                              default="main/images/trainer-2.jpg")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return str(self.first_name)


# Student Models


class Student(models.Model):
    date_birth = models.DateField(blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    class_id = models.ForeignKey(
        "courses.LopHoc", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.first_name)


# Payment Models
class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Payment(models.Model):
    payment_date = models.DateTimeField()
    amount = models.FloatField()
    payment_method_id = models.ForeignKey(
        PaymentMethod, on_delete=models.PROTECT)
    status = models.CharField(max_length=50)
    student_id = models.ForeignKey(Student, on_delete=models.PROTECT)
    class_id = models.ForeignKey("courses.LopHoc", on_delete=models.PROTECT)

    def __str__(self):
        return self.payment_date


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True)
    subject = models.CharField(max_length=264)
    message = models.TextField()

    def __str__(self):
        return self.name + ", " + self.subject


class User(models.Model):
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=32)
    fullname = models.CharField(max_length=100, unique=False)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(
        max_length=500, unique=False, default='', blank=True)

    def __str__(self):
        return self.username
