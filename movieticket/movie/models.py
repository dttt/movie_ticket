from django.db import models


class Genre(models.Model):
    name = models.CharField("", max_length=30)


class Company(models.Model):
    name = models.CharField("", max_length=100)


class Actor(models.Model):
    name = models.CharField("", max_length=100)


class Director(models.Model):
    name = models.CharField("", max_length=100)


class Presentation(models.Model):
    name = models.CharField("", max_length=50)


class MPAA(models.Model):
    name = models.CharField("", max_length=20)
    meaning = models.TextField("")
    explanation = models.TextField("")


class Movie(models.Model):
    """docstring for Movie"""
    name = models.CharField("", max_length=255)
    trailer = models.TextField("")
    poster = models.TextField("")
    summary = models.TextField("")
    length = models.IntegerField("")
    genre = models.ManyToManyField(Genre, verbose_name="")
    company = models.ForeignKey(Company, verbose_name="")
    MPAA = models.ForeignKey(MPAA, verbose_name="")


class PresentationType(models.Model):
    avaiable_date = models.DateField("")
    presentation = models.ForeignKey(Presentation, verbose_name="")
    movie = models.ForeignKey(Movie, verbose_name="")
