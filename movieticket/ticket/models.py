from django.db import models

from facility.models import CinemaRoom
from movie.models import Version
from users.models import CustomUser


class Schedule(models.Model):
    name = models.CharField("Ten lich", max_length=100)
    date = models.DateField("Ngay")
    begin_time = models.TimeField("Gio bat dau")
    end_time = models.TimeField("Gio ket thuc")
    room = models.ForeignKey(CinemaRoom, verbose_name="Phong chieu")
    movie = models.ForeignKey(Version, verbose_name="Phim chieu")
    creator = models.ForeignKey(CustomUser, verbose_name="Nhan vien tao")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Lich chieu"
        verbose_name_plural = "Cac lich chieu"
