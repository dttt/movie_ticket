# -*- coding: utf-8 -*-

from django.db import models


class Topic(models.Model):
    text = models.CharField(u"Nội dung của mục", max_length=100)

    def __unicode__(self):
        return u'%s' % self.text

    class Meta:
        verbose_name = u"Mục"
        verbose_name_plural = u"Các mục"


class Question(models.Model):
    text = models.CharField(u"Nội dung câu hỏi", max_length=100)
    topic = models.ForeignKey(Topic, verbose_name=u"Mục câu hỏi thuộc về")

    def __unicode__(self):
        return u'%s' % self.text

    class Meta:
        verbose_name = u"Câu hỏi"
        verbose_name_plural = u"Các câu hỏi"


class Answer(models.Model):
    text = models.TextField(u"Nội dung câu hỏi")
    question = models.OneToOneField(
        Question, verbose_name=u"Mục câu hỏi thuộc về")

    def __unicode__(self):
        return u'%s' % self.text

    class Meta:
        verbose_name = u"Trả lời"
        verbose_name_plural = u"Các trả lời"
