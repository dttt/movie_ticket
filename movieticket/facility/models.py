from django.db import models


class MovieTheater(models.Model):
    """Movie theater model"""
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    open_time = models.TimeField()
    close_time = models.TimeField()
