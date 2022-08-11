from django.urls import path, include
from . import views

app_name = 'register'

urlpatterns = [
    path('', views.register, name='register.html'),
    path('', include('django.contrib.auth.urls')),
    path('login/', views.user_login, name='login.html'),
    path('logout/', views.user_logout, name='logout.html'),
]
