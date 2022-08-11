from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index.html'),
    path('about/', views.about, name='about.html'),
    path('contact/', views.contact, name='contact.html'),
    path('trainers/', views.trainers, name='trainers.html'),
]
