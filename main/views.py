from django.shortcuts import render, HttpResponse
from . import models as main_models
from courses import models as course_models
# from courses import views
from register.views import register, user_login, user_logout
from . import forms
import datetime
# from . import forms
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from mentor.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
import feedparser


# Create your views here.
# from courses.models import *


def index(request):
    now = datetime.datetime.now()
    category = course_models.Category.objects.all()
    khoahoc = course_models.Course.objects.all()
    lst_khoahoc = khoahoc[:3]
    teacher = main_models.Teacher.objects.all()
    lst_teacher = teacher[:3]

    return render(request, "main/index.html", {'lst_khoahoc': lst_khoahoc, 'lst_teacher': lst_teacher, 'category': category, 'today': now})


def about(request):
    return render(request, "main/about.html")


def trainers(request):
    teacher = main_models.Teacher.objects.all()
    lst_teacher = teacher[:3]
    return render(request, "main/trainers.html", {'lst_teacher': lst_teacher})


def subscribe(request):
    now = datetime.datetime.now()
    last_visit = request.session.get('last_visit', False)
    username = request.session.get('username', 0)
    if request.method == 'POST':
        email_address = request.POST.get("email")
        subject = 'Welcome to LEAP English website'
        message = 'Hope you enjoy!'
        recepient = str(email_address)
        # send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)

        html_content = '<h2 style="color:blue"><i>Dear Reader,</i></h2>'\
            + '<p>Welcome to <strong>LEAP English</strong> website.</p>' \
            + '<h4 style="color:red">' + message + '</h4>'

        msg = EmailMultiAlternatives(
            subject, message, EMAIL_HOST_USER, [recepient])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        # send_mail(subject, message, EMAIL_HOST_USER,
        #           [recepient], fail_silently=False)

        result = "Our email was sent to your mail box. Thank you."

        return render(request, 'main/index.html', {'today': now, 'username': username, 'last_visit': last_visit, 'result': result, })
    return render(request, 'main/index.html', {'today': now, 'username': username, 'last_visit': last_visit})


def contact(request):
    now = datetime.datetime.now()
    result = ''
    success = False
    form = forms.FormContact()
    if request.method == 'POST':
        result = "Form có post"
        form = forms.FormContact(request.POST, main_models.Contact)
        result = "Form có Contact"
        # them validation cho from
        if form.is_valid():
            result = "Form đã valid!"
            request.POST._mutable = True
            post = form.save(commit=False)
            post.name = form.cleaned_data['name']
            post.phone_number = form.cleaned_data['phone_number']
            post.email = form.cleaned_data['email']
            post.password = form.cleaned_data['subject']
            post.password = form.cleaned_data['message']
            post.save()
            result = "Cảm ơn bạn đã liên lạc. Chúng tôi sẽ phản hồi sớm nhất có thể."
            success = [True if result != '' else False]
    else:
        form = forms.FormContact()

    last_visit = request.session.get('last_visit', False)

    return render(request, "main/contact.html", {'today': now, 'form': form, 'result': result, 'success': success})
