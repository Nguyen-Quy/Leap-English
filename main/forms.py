from django import forms
from . import models
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    r"((\([0-9]{3}\)[0-9]{9,15})|([0-9]{10,15}))", "Your phone number must be (xxx)xxxxxxxxx or 0xxxxxxxxx!")


class UserForm(forms.ModelForm):
    password = forms.CharField(
        max_length=150, label='Password', widget=forms.PasswordInput())
    confirm = forms.CharField(
        max_length=150, label='Confirm', widget=forms.PasswordInput())
    # set_password=password

    class Meta():
        model = models.User
        fields = ('username', 'email', 'password')


class FormContact(forms.ModelForm):
    name = forms.CharField(max_length=150, label='Name', widget=forms.TextInput(attrs={
                           'placeholder': 'Nhập tên của bạn', 'class': 'form-control fh5co_contact_text_box'}))
    phone_number = forms.CharField(max_length=20, label='Phone', validators=[phone_validator], widget=forms.TextInput(
        attrs={'placeholder': 'Số điện thoại',
               'class': 'form-control fh5co_contact_text_box',
               'pattern': '((\([0-9]{3}\)[0-9]{9,15})|([0-9]{10,15}))',
               'title': 'Số điện thoại phải có dạng (xxx)xxxxxxxxx or 0xxxxxxxxx'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'class': 'form-control fh5co_contact_text_box'}))
    subject = forms.CharField(label='Subject', widget=forms.TextInput(
        attrs={'placeholder': 'Tiêu đề', 'class': 'form-control fh5co_contact_text_box'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Điền tin nhắn', 'class': 'form-control fh5co_contacts_message'}))

    class Meta:
        model = models.Contact
        fields = '__all__'
