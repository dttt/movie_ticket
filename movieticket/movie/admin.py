from django.contrib import admin

from .models import Actor
from .models import Director
from .models import Genre
from .models import Company
from .models import Presentation
from .models import MPAA
from .models import Movie
from .models import Version
from .forms import VersionForm


admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Company)
admin.site.register(MPAA)


class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Movie, SlugAdmin)
admin.site.register(Presentation, SlugAdmin)


class VersionAdmin(admin.ModelAdmin):
    form = VersionForm

admin.site.register(Version, VersionAdmin)
