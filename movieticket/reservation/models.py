# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

from users.models import CustomUser


class Reservation(models.Model):
    total_cost = models.IntegerField(
        "Tong tien thanh toan", blank=True, null=True)
    paid = models.BooleanField("Da thanh toan?", default=False)
    date = models.DateField("Ngay dat", default=timezone.now())
    customer = models.ForeignKey(CustomUser, verbose_name="Khach hang")

    def __unicode__(self):
        return 'Reservation %s' % self.id
