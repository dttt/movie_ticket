# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from facility.models import MovieTheater


class Genre(models.Model):
    name = models.CharField(u"Tên thể loại", max_length=30)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = u"Thể loại"
        verbose_name_plural = u"Các thể loại"


class Company(models.Model):
    name = models.CharField(u"Tên công ty sản xuất", max_length=100)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = u"Công ty sản xuất"
        verbose_name_plural = u"Các công ty sản xuất"


class Actor(models.Model):
    name = models.CharField(u"Tên diễn viên", max_length=100)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = u"Diễn viên"
        verbose_name_plural = u"Các diễn viên"


class Director(models.Model):
    name = models.CharField(u"Tên đạo diễn", max_length=100)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = u"Đạo diễn"
        verbose_name_plural = u"Các đạo diễn"


class Presentation(models.Model):
    name = models.CharField(u"Tên cách chiếu phim", max_length=50)
    slug = models.SlugField(max_length=20, blank=True)

    def __unicode__(self):
        return u'%s' % self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Presentation, self).save()

    class Meta:
        verbose_name = u"Cách chiếu phim"
        verbose_name_plural = u"Các cách chiếu phim"


class MPAA(models.Model):
    name = models.CharField(u"Tên nhãn", max_length=20)
    meaning = models.TextField(u"Ý nghĩa của nhãn")
    explanation = models.TextField(u"Giải thích của nhãn")

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = u"MPAA"


class Movie(models.Model):
    """docstring for Movie"""
    name = models.CharField(u"Tên phim", max_length=255)
    trailer = models.TextField(u"Trailer của phim")
    poster = models.ImageField(u"Poster của phim", upload_to=u"images/posters")
    summary = models.TextField(u"Tóm tắt phim")
    length = models.IntegerField(u"Độ dài phim")
    slug = models.SlugField(max_length=100, blank=True)
    # One to many
    company = models.ForeignKey(Company, verbose_name=u"Công ty sản xuất")
    MPAA = models.ForeignKey(MPAA)
    director = models.ForeignKey(Director, verbose_name=u"Đạo diễn")
    # Many to many
    actors = models.ManyToManyField(Actor, verbose_name=u"Các diễn viên")
    genre = models.ManyToManyField(Genre, verbose_name=u"Thể loại")

    def __unicode__(self):
        return u'%s' % self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Movie, self).save()

    class Meta:
        verbose_name = u"Phim"
        verbose_name_plural = u"Các phim"


class Version(models.Model):
    begin_date = models.DateField(u"Ngày bắt đầu chiếu")
    end_date = models.DateField(u"Ngày kết thúc chiếu")
    presentation = models.ForeignKey(
        Presentation, verbose_name=u"Cách chiếu phim")
    movie = models.ForeignKey(Movie, verbose_name=u"Tên phim")
    slug = models.SlugField(max_length=110, unique=True, blank=True)
    available_theaters = models.ManyToManyField(
        MovieTheater, blank=True, verbose_name=u"Các cụm rạp chiếu")

    def __unicode__(self):
        return u"%s (%s)" % (self.movie, self.presentation)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.presentation.slug + '-' + self.movie.slug
        super(Version, self).save()

    def get_absolute_url(self):
        return reverse('movie:show-version', args=(self.slug,))

    class Meta:
        verbose_name = u"Phiên bản"
        verbose_name_plural = u"Các phiên bản"
        unique_together = ('movie', 'presentation')
