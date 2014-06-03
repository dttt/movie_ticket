# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

from users.models import CustomUser


class Reservation(models.Model):
    total_cost = models.IntegerField(
        "Tổng tiền", blank=True, null=True)
    paid = models.BooleanField("Đã thanh toán?", default=False)
    date = models.DateField("Ngày đặt", default=timezone.now())
    customer = models.ForeignKey(CustomUser, verbose_name="Khách hàng")

    def __unicode__(self):
        return 'Reservation %s' % self.id
