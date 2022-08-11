from django.db import models
from django.utils.translation import gettext as _

ngay_trong_tuan = {
    'Thứ Hai': _(u'Thứ Hai'),
    'Thứ Ba': _(u'Thứ Ba'),
    'Thứ Tư': _(u'Thứ Tư'),
    'Thứ Năm': _(u'Thứ Năm'),
    'Thứ Sáu': _(u'Thứ Sáu'),
    'Thứ Bảy': _(u'Thứ Bảy'),
    'Chủ Nhật': _(u'Chủ Nhật'),
}


class FieldNgayTrongTuan(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = tuple(ngay_trong_tuan.items())
        kwargs['max_length'] = 8
        super(FieldNgayTrongTuan, self).__init__(*args, **kwargs)
