from django.contrib import admin

from .models import MovieTheater, CinemaRoom


class MovieTheaterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(MovieTheater, MovieTheaterAdmin)

admin.site.register(CinemaRoom)
# Register your models here.
