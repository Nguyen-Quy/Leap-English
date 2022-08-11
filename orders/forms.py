from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    phone = forms.CharField(max_length=20, label='Điện thoại', widget=forms.TextInput(
        attrs={'pattern': '((\([0-9]{3}\)[0-9]{9,15})|([0-9]{10,15}))',
               'title': 'Your phone number must be (xxx)xxxxxxxxx or 0xxxxxxxxx'}))
    username = forms.CharField(max_length=50, label='Tên đăng nhập')
    first_name = forms.CharField(max_length=50, label='Tên')
    last_name = forms.CharField(max_length=50, label='Họ')
    address = forms.CharField(max_length=500, label='Địa chỉ')

    class Meta:
        model = Order
        fields = ['username', 'last_name',
                  'first_name', 'email', 'phone', 'address']
