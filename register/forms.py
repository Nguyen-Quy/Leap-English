from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
# from django.contrib.auth.models import User
from django.db import models
from django import forms


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='Tên đăng nhập', widget=forms.TextInput(
    ), help_text='Cao nhất 150 ký tự, gồm chữ cái, số và các dấu @/./+/-/_')
    fullname = forms.CharField(
        max_length=100, widget=forms.TextInput(), label='Họ tên')
    email = forms.EmailField(widget=forms.TextInput())
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(
    ), label='Mật khẩu', help_text="<ul><li>Mật khẩu không được trùng với thông tin cá nhân của bạn.</li><li>Mật khẩu gồm ít nhất 8 ký tự.</li><li>Mật khẩu không chứa toàn ký tự số.</li></ul>")
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(
    ), label='Xác nhận mật khẩu', help_text='Nhập lại mật khẩu.')
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
                            'pattern': '((\([0-9]{3}\)[0-9]{9,15})|([0-9]{10,15}))', 'title': 'Số điện thoại phải có dạng: (xxx)xxxxxxxxx or 0xxxxxxxxx'}), label='Số điện thoại')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'fullname', 'email',
                  'phone', 'password1', 'password2']
