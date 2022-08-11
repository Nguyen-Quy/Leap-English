from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import *
from courses.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(LopHoc)
admin.site.register(BaiHoc)
admin.site.register(Payment)
admin.site.register(PaymentMethod)
admin.site.register(Student)
admin.site.register(Teacher)


class BaiHocAdmin(admin.ModelAdmin):
    list_filter = ('lophoc_id',)
    list_display = ('ten_bai', 'lecture', 'lophoc_id')


class BaiHocInline(admin.TabularInline):
    model = BaiHoc
    raw_id_fields = ("ten_bai",)
    fk_name = "lophoc_id"


class LopHocAdmin(admin.ModelAdmin):
    inlines = [BaiHocInline, ]


class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass
