# -*- coding: utf-8 -*-

from django.utils import timezone
from django.db import models
from django.core.urlresolvers import reverse


class New(models.Model):
    """Chua cac tin moi"""
    title = models.CharField(u"Tiêu đề", max_length=255)
    text = models.TextField(u"Nội dung")
    image = models.ImageField(u"Ảnh đại diện", upload_to=u"images/news")
    created_at = models.DateTimeField(u"Ngày tạo", default=timezone.now())
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('news:show', args=(self.slug,))

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = u"Tin mới"
        verbose_name_plural = u"Các tin mới"
