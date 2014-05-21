from django.utils import timezone
from django.db import models
from django.core.urlresolvers import reverse


class New(models.Model):
    """Chua cac tin moi"""
    title = models.CharField("Tieu de cua tin", max_length=255)
    text = models.TextField("Noi dung chinh cua tin")
    image = models.ImageField("Anh dai dien cua tin", upload_to=u"images/news")
    created_at = models.DateTimeField("Ngay khoi tao", default=timezone.now())
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('news:show', args=(self.slug,))

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Tin tuc"
        verbose_name_plural = "Cac tin tuc"
