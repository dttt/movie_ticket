# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

from users.models import CustomUser


class Reservation(models.Model):
    total_cost = models.IntegerField(
        u"Tổng tiền", blank=True, null=True)
    paid = models.BooleanField(u"Đã thanh toán?", default=False)
    date = models.DateField(u"Ngày đặt", default=timezone.now())
    customer = models.ForeignKey(CustomUser, verbose_name=u"Khách hàng")

    def __unicode__(self):
        return u'Reservation %s' % self.id
