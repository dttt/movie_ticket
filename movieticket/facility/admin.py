from django.contrib import admin

from .models import MovieTheater
from .models import CinemaRoom


admin.site.register(MovieTheater)
admin.site.register(CinemaRoom)
# Register your models here.
