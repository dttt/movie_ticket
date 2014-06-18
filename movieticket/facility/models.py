# -*- coding: utf-8 -*-

from django.db import models


class MovieTheater(models.Model):
    """Movie theater model"""
    name = models.CharField(u"Tên rạp chiếu", max_length=100)
    address = models.CharField(u"Địa chỉ phòng chiếu", max_length=255)
    open_time = models.TimeField(u"Giờ mở cửa")
    close_time = models.TimeField(u"Giờ đóng cửa")
    latitude = models.DecimalField(
        u"Hoành độ google-map", blank=True, null=True,
        max_digits=11, decimal_places=6
    )
    longtitude = models.DecimalField(
        u"Tung độ google-maps", blank=True, null=True,
        max_digits=11, decimal_places=6
    )
    tel = models.CharField(u"Số điện thoại", max_length=11, default="0")
    description = models.TextField(u"Miêu tả", default='')
    image = models.ImageField(u"Ảnh đại diện", upload_to=u"images/theaters", default='')

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = u"Cụm rạp"
        verbose_name_plural = u"Các cụm rạp"


class CinemaRoom(models.Model):
    name = models.CharField(u"Tên phòng chiếu", max_length=100)
    total_row = models.CharField(
        u"Số dòng ghế của phòng", default="a", max_length=2)
    total_column = models.IntegerField(u"Số cột ghế của phòng", default=1)
    theater = models.ForeignKey(
        MovieTheater, verbose_name=u'Rạp mà phòng thuộc về')

    def __unicode__(self):
        return u'%s-%s-%s' % (self.name, self.theater.name, self.id)

    class Meta:
        verbose_name = u"Rạp"
        verbose_name_plural = u"Các rạp"
