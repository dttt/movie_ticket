# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'MovieTheater.description'
        db.delete_column(u'facility_movietheater', 'description')


    def backwards(self, orm):
        # Adding field 'MovieTheater.description'
        db.add_column(u'facility_movietheater', 'description',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    models = {
        u'facility.cinemaroom': {
            'Meta': {'object_name': 'CinemaRoom'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'theater': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facility.MovieTheater']"}),
            'total_column': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'total_row': ('django.db.models.fields.CharField', [], {'default': "'a'", 'max_length': '2'})
        },
        u'facility.movietheater': {
            'Meta': {'object_name': 'MovieTheater'},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'google_map': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '11'})
        }
    }

    complete_apps = ['facility']