# -*- coding: utf-8 -*-

from django.db import models


class MovieTheater(models.Model):
    """Movie theater model"""
    name = models.CharField("Tên rạp chiếu", max_length=100)
    address = models.CharField("Địa chỉ phòng chiếu", max_length=255)
    open_time = models.TimeField("Giờ mở cửa")
    close_time = models.TimeField("Giờ đóng cửa")
    latitude = models.DecimalField(
        "Hoành độ google-map", blank=True, null=True,
        max_digits=11, decimal_places=6
    )
    longtitude = models.DecimalField(
        "Tung độ google-maps", blank=True, null=True,
        max_digits=11, decimal_places=6
    )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Cụm rạp"
        verbose_name_plural = "Các cụm rạp"


class CinemaRoom(models.Model):
    name = models.CharField("Tên phòng chiếu", max_length=100)
    total_row = models.CharField(
        "Số dòng ghế của phòng", default="a", max_length=2)
    total_column = models.IntegerField("Số cột ghế của phòng", default=1)
    theater = models.ForeignKey(
        MovieTheater, verbose_name='Rạp mà phòng thuộc về')

    def __unicode__(self):
        return self.name + '-' + self.theater.name + '-%s' % self.id

    class Meta:
        verbose_name = "Rạp"
        verbose_name_plural = "Các rạp"
