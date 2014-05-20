from django.contrib import admin

from .models import MovieTheater, CinemaRoom, New


admin.site.register(MovieTheater)
admin.site.register(CinemaRoom)
admin.site.register(New)
# Register your models here.
