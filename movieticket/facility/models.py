# -*- coding: utf-8 -*-

from django.utils import timezone
from django.db import models


class MovieTheater(models.Model):
    """Movie theater model"""
    name = models.CharField("Tên rạp chiếu", max_length=100)
    address = models.CharField("Địa chỉ phòng chiếu", max_length=255)
    open_time = models.TimeField("Giờ mở cửa")
    close_time = models.TimeField("Giờ đóng cửa")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Cụm rạp"
        verbose_name_plural = "Các cụm rạp"


class CinemaRoom(models.Model):
    name = models.CharField("Tên phòng chiếu", max_length=100)
    total_row = models.IntegerField("Số dòng ghế của phòng", default=1)
    total_column = models.IntegerField("Số cột ghế của phòng", default=1)
    theater = models.ForeignKey(
        MovieTheater, verbose_name='Rạp mà phòng thuộc về')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Rạp"
        verbose_name_plural = "Các rạp"


class New(models.Model):
    """Chua cac tin moi"""
    title = models.CharField("Tieu de cua tin", max_length=255)
    text = models.TextField("Noi dung chinh cua tin")
    image = models.ImageField("Anh dai dien cua tin", upload_to=u"images/news")
    created_at = models.DateTimeField("Ngay khoi tao", default=timezone.now())

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Tin tuc"
        verbose_name_plural = "Cac tin tuc"
