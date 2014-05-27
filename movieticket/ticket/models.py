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


class TicketType(models.Model):
    name = models.CharField("Ten loai ve", max_length=40)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Loai ve"
        verbose_name_plural = "Cac loai ve"


class Ticket(models.Model):
    price = models.IntegerField("Gia ve")
    row = models.CharField("Thu tu dong", max_length=2)
    column = models.CharField("Thu tu cot", max_length=2)
    date_sold = models.DateField("Ngay ban")
    ticket_type = models.ForeignKey(TicketType, verbose_name="Loai ve")
    schedule = models.ForeignKey(Schedule, verbose_name="Ve dat cho")

    def __unicode(self):
        return self.id

    class Meta:
        verbose_name = "Ve"
        verbose_name_plural = "Cac ve"
