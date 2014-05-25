from django.contrib import admin
from django.db import models

from ckeditor.widgets import CKEditorWidget

from news.models import New


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

admin.site.register(New, NewsAdmin)
