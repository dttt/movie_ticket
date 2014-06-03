# -*- coding: utf-8 -*-
from django.db import models

from facility.models import CinemaRoom
from movie.models import Version
from users.models import CustomUser
from reservation.models import Reservation


class Schedule(models.Model):
    name = models.CharField("Tên lịch", max_length=100)
    date = models.DateField("Ngày")
    begin_time = models.TimeField("Giờ bắt đầu")
    end_time = models.TimeField("Giờ kết thúc")
    room = models.ForeignKey(CinemaRoom, verbose_name="Rạp chiếu")
    movie = models.ForeignKey(Version, verbose_name="Phim được chiếu")
    creator = models.ForeignKey(CustomUser, verbose_name="Nhân viên tạo")

    def __unicode__(self):
        return "Lịch số %s" % self.id

    class Meta:
        verbose_name = "Lịch chiếu"
        verbose_name_plural = "Các lịch chiếu"


class TicketType(models.Model):
    name = models.CharField("Tên loại vé", max_length=40)
    price = models.IntegerField("Giá vé bán", null=True)
    limit = models.IntegerField("Số lượng có thể đặt", default=10)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Loại vé"
        verbose_name_plural = "Các loại vé"


class Ticket(models.Model):
    price = models.IntegerField("Giá vé", blank=True, null=True)
    row = models.CharField("Thứ tự dòng", max_length=2)
    column = models.CharField("Thứ tự cột", max_length=2)
    ticket_type = models.ForeignKey(TicketType, verbose_name="Loại vé")
    schedule = models.ForeignKey(Schedule, verbose_name="Đặt cho lịch")
    reservation = models.ForeignKey(Reservation, blank=True, null=True)

    def __unicode__(self):
        return 'Vé số %s' % self.id

    class Meta:
        verbose_name = "Vé"
        verbose_name_plural = "Các ves"
        unique_together = ('schedule', 'column', 'row')
