# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse


class MovieTheater(models.Model):
    """Movie theater model"""
    name = models.CharField(u"Tên rạp chiếu", max_length=100, unique=True)
    address = models.TextField(u"Địa chỉ phòng chiếu", max_length=255)
    google_map = models.TextField(u"URL google map")
    tel = models.CharField(u"Số điện thoại", max_length=11, default="0")
    image = models.ImageField(
        u"Ảnh đại diện", upload_to=u"images/theaters", default='')
    slug = models.SlugField(max_length=255, unique=True, null=True)

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('facility:theater-show', args=(self.slug,))

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
