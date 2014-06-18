# -*- coding: utf-8 -*-
from django.db import models

from facility.models import CinemaRoom
from movie.models import Version
from users.models import CustomUser
from reservation.models import Reservation


class Schedule(models.Model):
    name = models.CharField(u"Tên lịch", max_length=100)
    date = models.DateField(u"Ngày")
    begin_time = models.TimeField(u"Giờ bắt đầu")
    end_time = models.TimeField(u"Giờ kết thúc")
    room = models.ForeignKey(CinemaRoom, verbose_name=u"Rạp chiếu")
    movie = models.ForeignKey(Version, verbose_name=u"Phim được chiếu")
    creator = models.ForeignKey(CustomUser, verbose_name=u"Nhân viên tạo")

    def __unicode__(self):
        return u"Lịch cho phim %s phòng %s từ %s đến %s" % (
            self.movie, self.room, self.begin_time, self.end_time)

    class Meta:
        verbose_name = u"Lịch chiếu"
        verbose_name_plural = u"Các lịch chiếu"


class TicketType(models.Model):
    name = models.CharField(u"Tên loại vé", max_length=40)
    price = models.IntegerField(u"Giá vé bán", null=True)
    limit = models.IntegerField(u"Số lượng có thể đặt", default=10)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = u"Loại vé"
        verbose_name_plural = u"Các loại vé"


class Ticket(models.Model):
    price = models.IntegerField(u"Giá vé", blank=True, null=True)
    row = models.CharField(u"Thứ tự dòng", max_length=2)
    column = models.CharField(u"Thứ tự cột", max_length=2)
    ticket_type = models.ForeignKey(TicketType, verbose_name=u"Loại vé")
    schedule = models.ForeignKey(Schedule, verbose_name=u"Đặt cho lịch")
    reservation = models.ForeignKey(Reservation, blank=True, null=True)

    def __unicode__(self):
        return u'Vé số %s' % self.id

    class Meta:
        verbose_name = u"Vé"
        verbose_name_plural = u"Các vé"
        unique_together = ('schedule', 'column', 'row')
