# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'New.begin_date'
        db.add_column(u'news_new', 'begin_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 6, 21, 0, 0)),
                      keep_default=False)

        # Adding field 'New.end_date'
        db.add_column(u'news_new', 'end_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 6, 21, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'New.begin_date'
        db.delete_column(u'news_new', 'begin_date')

        # Deleting field 'New.end_date'
        db.delete_column(u'news_new', 'end_date')


    models = {
        u'news.new': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'New'},
            'begin_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 6, 21, 0, 0)'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 6, 21, 0, 0)'}),
            'end_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 6, 21, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['news']