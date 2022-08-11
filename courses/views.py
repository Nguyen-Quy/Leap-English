from django.shortcuts import render
import datetime
from . import models
from cart.forms import CartAddProductForm
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.cart import Cart
from orders import models as order_models
from register.views import user_login, User
from django.db.models import Count
from math import ceil

# Create your views here.
category = models.Category.objects.all()
lophoc = models.LopHoc.objects.all()
khoahoc = models.Course.objects.all()
baihoc = models.BaiHoc.objects.all()

now = datetime.datetime.now()


def courses(request):
    if len(khoahoc) > 0:
        lst_lophoc = lophoc.exclude(
            course_id__isnull=True).order_by('ten_lop')

        return render(request, "courses/courses.html", context={'khoahoc': khoahoc, 'lophoc': lophoc, 'lst_lophoc': lst_lophoc, 'today': now, })

    # return render(request, "courses/courses.html", {'dc': dc, })


def lst_course(request, id):
    lst_lophoc = lophoc.filter(course_id=id).order_by('ten_lop')

    return render(request, "courses/courses.html", context={'khoahoc': khoahoc, 'lophoc': lophoc, 'lst_lophoc': lst_lophoc, 'today': now})


def detail(request, pk):
    cart_product_form = CartAddProductForm()
    select_lop = lophoc.get(pk=pk)
    lst_bai = baihoc.filter(lophoc_id=select_lop)

    return render(request, "courses/course_details.html", {'select_lop': select_lop, 'khoahoc': khoahoc, 'lst_bai': lst_bai, 'cart_product_form': cart_product_form, 'today': now})


def registered_courses(request):
    username = request.session.get('username', 0)
    if request.user.is_authenticated:
        user = request.user
    users = order_models.Order.objects.all()
    regis_user = users.filter(username=user.username)
    # print(regis_user)

    items = order_models.OrderItem.objects.all()
    regis_item = items.filter(order__in=regis_user)
    # print(regis_item)
    # print(regis_item.values('id'))

    c = lophoc.filter(id__in=regis_item.values('product_id'))
    num = regis_item.values('product_id').annotate(n=Count('product_id'))
    # print(c.values('ten_lop'))
    zipped_lst = zip(c, num)

    return render(request, "courses/registered_courses.html", {'regis_user': regis_user, 'regis_item': regis_item, 'list': zipped_lst, 'today': now})
