from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.courses, name='courses'),
    path('<int:id>', views.lst_course, name='khoahoc'),
    path('course_details/<int:pk>', views.detail, name='lophoc'),
    path('registered_courses', views.registered_courses, name='registered'),

]
