# -*- coding: utf-8 -*-

from django.db import models


class Genre(models.Model):
    name = models.CharField("Tên thể loại", max_length=30)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Thể loại"
        verbose_name_plural = "Các thể loại"


class Company(models.Model):
    name = models.CharField("Tên công ty sản xuất", max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Công ty sản xuất"
        verbose_name_plural = "Các công ty sản xuất"


class Actor(models.Model):
    name = models.CharField("Tên diễn viên", max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Diễn viên"
        verbose_name_plural = "Các diễn viên"


class Director(models.Model):
    name = models.CharField("Tên đạo diễn", max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Đạo diễn"
        verbose_name_plural = "Các đạo diễn"


class Presentation(models.Model):
    name = models.CharField("Tên cách chiếu phim", max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Cách chiếu phim"
        verbose_name_plural = "Các cách chiếu phim"


class MPAA(models.Model):
    name = models.CharField("Tên nhãn", max_length=20)
    meaning = models.TextField("Ý nghĩa của nhãn")
    explanation = models.TextField("Giải thích của nhãn")

    def __unicode__(self):
        return self.name


class Movie(models.Model):
    """docstring for Movie"""
    name = models.CharField("Tên phim", max_length=255)
    trailer = models.TextField("Trailer của phim")
    poster = models.TextField("Poster của phim")
    summary = models.TextField("Tóm tắt phim")
    length = models.IntegerField("Độ dài phim")
    genre = models.ManyToManyField(Genre, verbose_name="Thể loại")
    company = models.ForeignKey(Company, verbose_name="Công ty sản xuất")
    MPAA = models.ForeignKey(MPAA)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Phim"
        verbose_name_plural = "Các Phim"


class PresentationMovie(models.Model):
    begin_date = models.DateField("Ngày bắt đầu chiếu")
    end_date = models.DateField("Ngày kết thúc chiếu")
    presentation = models.ForeignKey(
        Presentation, verbose_name="Cách chiếu phim")
    movie = models.ForeignKey(Movie, verbose_name="Tên phim")

    def __unicode__(self):
        return "%s (%s)" % (self.movie, self.presentation)
